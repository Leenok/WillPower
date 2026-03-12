from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('workout_list/', views.workout_list, name='workout_list'),
]