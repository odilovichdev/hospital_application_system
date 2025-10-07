from django.urls import path

from apps.users.api import (
    AddEmployeeCreateAPIView,
    EmployeeListAPIView,
    LoginAPIView,
    ProfileAPIView,
    RegisterAPIView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),

    path('add-employee',
         AddEmployeeCreateAPIView.as_view(), name='add-employee'),
    path('employees',
         EmployeeListAPIView.as_view(), name='employees'),
]