from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.home, name='home'),
    path('workout_list/', views.workout_list, name='workout_list'),
    # Все маршруты аутентификации Django
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
