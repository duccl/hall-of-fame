from django.urls import path
from .views import *
urlpatterns = [
    path('',SignUpView.as_view(),name='sign-up'),
    path('login/',CustomLoginView.as_view(),name='login'),
]
