from django.urls import path

from blog import views

urlpatterns = [
    path("home/", views.PostView.as_view(), name="home")
]