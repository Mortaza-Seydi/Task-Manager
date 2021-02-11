from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'boards.html')
    else:
        return redirect('signIn')
