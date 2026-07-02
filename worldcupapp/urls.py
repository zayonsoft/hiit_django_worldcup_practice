from django.urls import path
from worldcupapp import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("students", views.students),
    path("my_page/service", views.services, name="service"),
    path("contact", views.contact, name="contact"),
    path("about", views.about),
    path("google", views.gotoGoogle),
    path("users", views.my_users),
]
