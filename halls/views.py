from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class DashBoardView(LoginRequiredMixin,ListView):
    template_name = "halls/dashboard.html"
    login_url = 'accounts:login'
    model = Hall
    context_object_name = 'halls'
    def get_queryset(self):
        return Hall.objects.filter(author__username = self.kwargs["username"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs["username"]
        return context
    
class HallsView(ListView):
    template_name = "halls/home.html"
    login_url = 'accounts:login'
    model = Hall
    context_object_name = 'halls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Halls"
        return context
