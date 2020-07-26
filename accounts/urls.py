from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',SignUpView.as_view(),name='sign-up'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
]
