from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    

    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
]
