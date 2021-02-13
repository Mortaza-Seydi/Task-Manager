from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Board, Task, Project
from users.models import Profile


class Boards(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            data = {"user": user,
                    "first": user.username[0],
                    "other_users": User.objects.filter(~Q(username=user.username)).all(),
                    "projects": Project.objects.filter(owner_id=user.id),
                    }
            return render(request, 'boards.html', data)
        else:
            return redirect('signIn')

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        else:
            name = request.POST['name']
            description = request.POST['desc']
            details = request.POST['details']
            owner = request.user
            user_ids = request.POST.getlist('users', [])

            br = Board()
            br.save()

            for id in user_ids:
                br.members.add(id)

            proj = Project(name=name, description=description, details=details, owner=owner, members=br)
            proj.save()

            return redirect('boards')


class Tasks(View):
    def get(self, request, id):
        proj = Project.objects.filter(id=id).first()
        if request.user.is_authenticated:
            user = request.user
            data = {"user": user,
                    "first": user.username[0],
                    "other_users": User.objects.all(),
                    "tasks": proj.task.all()
                    }
            return render(request, 'tasks.html', data)
        else:
            return redirect("signIn")

    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('signIn')

        else:
            name = request.POST['name']
            description = request.POST['desc']
            assigned_to = request.POST['users']
            status = 'T'
            end_time = request.POST['date']

            task = Task(name=name, description=description, assigned_to_id=assigned_to, status=status,
                        end_time=end_time)
            task.save()

            proj = Project.objects.filter(id=id).first()
            proj.task.add(task)

            return redirect('tasks', id=id)