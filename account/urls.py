from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('user/add/', AddUserView.as_view(), name='add_user'),
]
