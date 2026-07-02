from django.shortcuts import render, redirect
from django.http import HttpResponse
from worldcupapp.models import Student


# Create your views here.
def home(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "service.html")


def about(request):
    return HttpResponse("<h1>My ABOUT PAGE!!!!!</h1>")


def students(request):
    students = Student.objects.all()
    context = {"students": students, "programmer_name": "Favour"}
    return render(request, "students.html", context)


def gotoGoogle(request):
    return redirect("https://google.com")


def my_users(request):
    return HttpResponse("<h1>My Users are here </h1>")
