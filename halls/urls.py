from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/<str:username>/',DashBoardView.as_view(),name='dashboard'),
    path('',HallsView.as_view(),name='home'),
    path('hall/<int:hall_id>/',HallDetailView.as_view(),name='hall')
]
