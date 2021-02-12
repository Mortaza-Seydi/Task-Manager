from django.urls import path
from .views import Boards

urlpatterns = [
    path('', Boards.as_view(), name='boards'),
]
