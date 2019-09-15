"""WindManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
#from turbines.views import BaseView, LoginView, TurbinesView#, include
#from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='home'), name='logout'),
    url(r'^admin/', admin.site.urls),
    url('', TemplateView.as_view(template_name='turbines/home.html'), name='home'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),#, include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='turbines/home.html'), name='home'), # new
]'''
# WindManager/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    #path('', include('pages.urls')),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    path('admin/', admin.site.urls),
    url('', TemplateView.as_view(template_name='turbines/home.html'), name='home'),
]