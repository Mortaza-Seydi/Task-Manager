from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Task, Project
from django.http import JsonResponse
import json, random


class Projects(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        list = []

        for p in projects:
            if p.owner == user or user.id in p.get_members():
                list.append(p)

        data = {"user": user,
                "first": user.username[0],
                "other_users": User.objects.filter(~Q(username=user.username)).all(),
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
                task.save()
            else:
                response = JsonResponse({"error": "You Do Not Have Permission"})
                response.status_code = 403
                return response

        response = JsonResponse({"message": "OK"})
        response.status_code = 200
        return response
