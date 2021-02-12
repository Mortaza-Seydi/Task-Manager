from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        data = {"user": request.user,
                "first": request.user.username[0]
                }
        return render(request, 'boards.html', data)
    else:
        return redirect('signIn')


