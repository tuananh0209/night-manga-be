from django.urls import path

from users.api import views

urlpatterns = [
    path("", views.TestView.as_view(), name="me"),
    path("register/", views.UserRegisterCustomView.as_view(), name="user-register"),
    path("login/", views.UserLoginCustomView.as_view(), name="user-login"),
]
