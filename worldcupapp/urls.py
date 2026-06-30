from django.urls import path
from worldcupapp import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("about", views.about),
    path("google", views.gotoGoogle),
    path("users", views.my_users),
]
