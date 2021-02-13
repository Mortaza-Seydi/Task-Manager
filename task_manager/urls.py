from django.urls import path
from .views import Boards, Tasks

urlpatterns = [
    path('', Boards.as_view(), name='boards'),
    path('t', Tasks.as_view(), name='tasks')
]
