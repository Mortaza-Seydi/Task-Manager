from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.db.models import Q


class Boards(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            data = {"user": user,
                    "first": user.username[0],
                    "other_users": User.objects.filter(~Q(username=user.username)).all()
                    }
            return render(request, 'boards.html', data)
        else:
            return redirect('signIn')

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        else:
            name = request.POST['name']
            description = request.POST['description']
            details = request.POST['details']
            owner = request.user.id
            user_ids = request.POST['user_ids']

            print(name, description, details, owner, user_ids)
            # members = models.ForeignKey(Board, on_delete=models.CASCADE)
