from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from task_manager.models import Project, Task, User


class ProjectInfo:
    def __init__(self, project):
        self.name = project.name
        all_tasks = project.task_set.all()

        self.t = 0
        self.d = 0
        self.i = 0
        self.o = 0

        for task in all_tasks:
            if task.status == 'T':
                self.t = self.t + 1

            elif task.status == 'D':
                self.d = self.d + 1

            elif task.status == 'I':
                self.i = self.i + 1

            elif task.status == 'O':
                self.o = self.o + 1

        all_tasks = self.t + self.d + self.i + self.o

        if all_tasks != 0:
            self.progress = int((self.o * 100) / all_tasks)
        else:
            self.progress = 0


class UserInfo:
    def __init__(self, user):
        self.user = user
        self.todo = 0
        self.doing = 0
        self.done = 0
        self.progress = 0

    def analyze_project(self, project):
        all_tasks = project.task_set.all()
        for task in all_tasks:
            if task.assigned_to == self.user:
                if task.status == 'T':
                    self.todo = self.todo + 1

                elif task.status == 'D':
                    self.doing = self.doing + 1

                elif task.status == 'I':
                    self.doing = self.doing + 1

                elif task.status == 'O':
                    self.done = self.done + 1

        all_tasks = self.todo + self.doing + self.done

        if all_tasks != 0:
            self.progress = int((self.done * 100) / all_tasks)
        else:
            self.progress = 0


class UserInProject:
    def __init__(self, user, project):
        self.u_info = UserInfo(user)
        self.name = project.name
        self.u_info.analyze_project(project)


class Report(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        p_info_list = []
        u_info = UserInfo(user)
        user_in_projects = []

        for p in projects:
            if p.owner == user or user.id in p.get_members():
                p_info = ProjectInfo(p)
                u_info.analyze_project(p)
                p_info_list.append(p_info)
                user_in_projects.append(UserInProject(user, p))

        data = {"user": user,
                "first": user.username[0],
                "p_info": p_info_list,
                "u_info": u_info,
                "u_in_p": user_in_projects,
                'time': datetime.today()
                }
        return render(request, 'report.html', data)
