from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from task_manager.models import Project, Task, User


class Report(View):
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
        return render(request, 'report.html', data)
