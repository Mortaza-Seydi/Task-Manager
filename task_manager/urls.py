from django.urls import path
from .views import Projects, Tasks, ManegeTasks, MangeProject

urlpatterns = [
    path('', Projects.as_view(), name='boards'),
    path('<id>', Tasks.as_view(), name='tasks'),
    path('<id>/delete', MangeProject.as_view()),
    path('<id>/task', ManegeTasks.as_view())
]
