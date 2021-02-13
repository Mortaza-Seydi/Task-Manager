from django.urls import path
from .views import Boards, Tasks, ManegeTasks

urlpatterns = [
    path('', Boards.as_view(), name='boards'),
    path('<id>', Tasks.as_view(), name='tasks'),
    path('<id>/task', ManegeTasks.as_view())
]
