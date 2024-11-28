from django.urls import path
from .views import *

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('members/', MyMembers.as_view(), name='members'),
    path('member/add/', AddUserView.as_view(), name='add_member'),
]
