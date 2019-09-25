from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

