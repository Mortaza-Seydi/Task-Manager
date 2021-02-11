from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        print("wowo")
    else:
        return redirect('signIn')


class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            print("wOWOW")
        else:
            return render(request, 'auth.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('/some/url/')
            print("eoe")
            return

        else:
            response = JsonResponse({"error": "Invalid Credential"})
            response.status_code = 403
            return response


class SignUp(View):
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)


