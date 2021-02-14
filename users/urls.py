from django.urls import path
from .views import SignIn, SignUp, index, SignOut

urlpatterns = [
    path('', index, name='index'),
    path('signIn', SignIn.as_view(), name="signIn"),
    path('signUp', SignUp.as_view(), name='signUp'),
    path('signOut', SignOut.as_view())
]
