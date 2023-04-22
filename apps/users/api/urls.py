from django.urls import path

from users.api import views

urlpatterns = [
    path("", views.TestView.as_view(), name="me"),
]
