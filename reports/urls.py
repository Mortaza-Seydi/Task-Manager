from django.urls import path
from .views import Report

urlpatterns = [
    path('', Report.as_view()),

]
