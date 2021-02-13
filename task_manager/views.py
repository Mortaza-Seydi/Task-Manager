from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Board, Task, Project


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
            print(request.POST)
            name = request.POST['name']
            description = request.POST['desc']
            details = request.POST['details']
            owner = request.user
            user_ids = request.POST.getlist('users', [])

            print(name, details, description, owner, user_ids)

            br = Board()
            br.save()
            for id in user_ids:
                br.members.add(id)

            proj = Project(name=name, description=description, details=details, owner=owner, members=br)
            proj.save()

            return redirect('boards')


class Tasks(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            data = {"user": user,
                    "first": user.username[0],
                    }
            return render(request, 'tasks.html', data)
