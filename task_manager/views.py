from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.username)
    else:
        return redirect('signIn')
