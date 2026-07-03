from django.urls import path
from worldcupapp import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("students", views.students, name="students"),
    path("students/<str:pk>", views.student, name="student"),
    path("add_students", views.add_student, name="add_students"),
    path("my_page/service", views.services, name="service"),
    path("contact", views.contact, name="contact"),
    path("about", views.about),
    path("google", views.gotoGoogle),
    path("users", views.my_users),
]
