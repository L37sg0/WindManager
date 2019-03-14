from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class BaseView(TemplateView):
    template_name = 'turbines/index.html'
class LoginView(TemplateView):
    template_name = 'turbines/login.html'
class TurbinesView(TemplateView):
    template_name = 'turbines/turbines.html'