from django.shortcuts import get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
from .api import Api
login_url = 'accounts:login'

def search_videos(request):
    search_form = SearchVideoForm(request.GET)
    return Api().listVideos(search_form)

class DashBoardView(LoginRequiredMixin,ListView):
    template_name = "halls/dashboard.html"
    login_url = login_url
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
    login_url = login_url
    model = Hall
    context_object_name = 'halls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All Halls"
        return context

class HallDetailView(LoginRequiredMixin,DetailView):
    model = Hall
    template_name = "halls/detail_hall.html"
    slug_url_kwarg = 'hall_id'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["videos"] = Video.objects.filter(hall=self.get_object())
        return context
    

class HallCreateView(LoginRequiredMixin,CreateView):
    model = Hall
    template_name = "halls/create_hall.html"
    login_url = login_url
    fields = ('title','description',)
    def form_valid(self,form):
        hall = form.save(commit = False)
        user = get_object_or_404(User,pk=self.request.user.pk)
        hall.author = user
        hall.save()
        return HttpResponseRedirect(reverse('halls:hall',kwargs={'hall_id':hall.id}))

class HallUpdateView(LoginRequiredMixin,UpdateView):
    model = Hall
    template_name = "halls/update_hall.html"
    login_url = login_url
    fields = ('title','description',)
    slug_url_kwarg = 'hall_id'
    slug_field = 'id'

    def get_success_url(self):
        return reverse('halls:hall',kwargs=self.kwargs)

class HallDeleteView(LoginRequiredMixin,DeleteView):
    model = Hall
    template_name = "halls/delete_hall.html"
    login_url = login_url
    slug_url_kwarg = 'hall_id'
    slug_field = 'id'

    def get_success_url(self):
        return reverse('halls:home')

class CreateVideoView(LoginRequiredMixin,CreateView):
    model = Video
    template_name = "halls/create_video.html"
    login_url = login_url
    fields = ('url',)

    def __init__(self):
        self.search_form = SearchVideoForm()
        super().__init__()

    def form_valid(self, form):
        video = form.save(commit=False)
        video.save(hall_id = self.kwargs.get('hall_id'))
        return HttpResponseRedirect(reverse('halls:hall',kwargs={'hall_id':self.kwargs.get('hall_id')}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hall_id"] = self.kwargs.get('hall_id')
        context["hall_name"] = get_object_or_404(Hall,pk=self.kwargs.get('hall_id')).title
        context['search_form'] = self.search_form
        return context
    