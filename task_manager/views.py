import datetime
import json
import random

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from reports.models import ProjectInfo
from .models import Task, Project


class Projects(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        list = []

        for p in projects:
            if p.owner == user or user.id in p.get_members():
                list.append(ProjectInfo(p))

        data = {"user": user,
                "first": user.username[0],
                "other_users": User.objects.filter(~Q(id=user.id)).all(),
                "projects": list,
                }
        return render(request, 'projects.html', data)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        name = request.POST['name']
        description = request.POST['desc']
        details = request.POST['details']
        owner = request.user
        user_ids = request.POST.getlist('users', [])

        ids = []
        for id in user_ids:
            ids.append(int(id))

        n = random.randint(1, 7)
        pf_url = f'/media/project-logos/{n}.png'

        proj = Project.objects.create(name=name, description=description, details=details, owner=owner,
                                      members=json.dumps(ids), profile_photo=pf_url)
        proj.save()

        return redirect('boards')


class MangeProject(View):
    def post(self, request, id):
        Project.objects.filter(id=id).delete()

        response = JsonResponse({"message": "OK"})
        response.status_code = 200
        return response


class Tasks(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("signIn")

        proj = Project.objects.filter(id=id).first()
        user = request.user
        users = User.objects.filter(Q(id__in=proj.get_members()) | Q(id=proj.owner.id))
        data = {"user": user,
                "first": user.username[0],
                "other_users": users,
                "tasks": proj.task_set.all(),
                'proj': proj,
                "can_add": user == proj.owner
                }
        return render(request, 'tasks.html', data)

    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('signIn')

        name = request.POST['name']
        description = request.POST['desc']
        assigned_to = request.POST['users']
        status = 'T'
        end_time = request.POST['date']

        task = Task(name=name, description=description, assigned_to_id=assigned_to, status=status,
                    end_time=end_time, project_id=id)
        task.save()

        return redirect('tasks', id=id)


class ManegeTasks(View):
    def post(self, request, id):
        if not request.user.is_authenticated:
            response = JsonResponse({"error": "Invalid User"})
            response.status_code = 403
            return response

        user = request.user

        type = request.POST['type']
        if type == 'edit_status':
            task_id = request.POST['task_id']
            status = request.POST['board_id']

            task = Task.objects.filter(id=task_id).first()

            if status in ['O', 'B', 'L'] or task.status in ['O', 'B', 'L']:
                if user == task.project.owner:
                    task.status = status
                    task.save()

                else:
                    response = JsonResponse({"error": "You Do Not Have Permission"})
                    response.status_code = 403
                    return response
            else:
                if user == task.assigned_to or user == task.project.owner:
                    task.status = status
                    if status == 'D':
                        task.start_time = datetime.datetime.today().date()
                    task.save()
                else:
                    response = JsonResponse({"error": "You Do Not Have Permission"})
                    response.status_code = 403
                    return response

            response = JsonResponse({"message": "OK"})
            response.status_code = 200
            return response

        if type == 'edit_end_time':

            task_id = request.POST['task_id']
            end_time = request.POST['new_end_time']

            task = Task.objects.filter(id=task_id).first()

            if user == task.project.owner:
                task.end_time = end_time
                task.save()

                response = JsonResponse({"message": "OK"})
                response.status_code = 200
                return response

            else:
                response = JsonResponse({"error": "You Do Not Have Permission"})
                response.status_code = 403
                return response
