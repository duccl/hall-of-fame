from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/<str:username>/',DashBoardView.as_view(),name='dashboard'),
    path('',HallsView.as_view(),name='home'),
    path('hall/<int:hall_id>/',HallDetailView.as_view(),name='hall'),
    path('new_hall/',HallCreateView.as_view(),name='new_hall'),
    path('update_hall/<int:hall_id>/',HallUpdateView.as_view(),name='update_hall'),
    path('delete_hall/<int:hall_id>/',HallDeleteView.as_view(),name='delete_hall'),
    path('<int:hall_id>/addvideo/',CreateVideoView.as_view(),name='add_video'),
    path('video/search',search_videos,name='video_search'),
    path('delete_video/<int:video_id>/',VideoDeleteView.as_view(),name='delete_video'),
]
