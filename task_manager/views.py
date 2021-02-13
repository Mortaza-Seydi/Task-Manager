from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Board, Task, Project
from users.models import Profile
from django.http import JsonResponse


class Boards(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        list = []

        for p in projects:
            if p.owner == user or user in p.members.members.all():
                list.append(p)

        data = {"user": user,
                "first": user.username[0],
                "other_users": User.objects.filter(~Q(username=user.username)).all(),
                "projects": list
                }
        return render(request, 'boards.html', data)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        name = request.POST['name']
        description = request.POST['desc']
        details = request.POST['details']
        owner = request.user
        user_ids = request.POST.getlist('users', [])

        proj = Project(name=name, description=description, details=details, owner=owner, members=br)
        proj.save()

        for id in user_ids:
            proj.members.members.add(id)

        return redirect('boards')


class Tasks(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("signIn")

        proj = Project.objects.filter(id=id).first()
        user = request.user
        data = {"user": user,
                "first": user.username[0],
                "other_users": proj.members.members.all(),
                "tasks": proj.task_set.all()
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

        if status in ['D', 'B', 'L']:
            if user == task.project.owner:
                task.status = status
                task.save()
            else:
                response = JsonResponse({"error": "You Do Not Have Permission"})
                response.status_code = 403
                return response
        else:
            task.status = status
            task.save()

        response = JsonResponse({"message": "OK"})
        response.status_code = 200
        return response
