from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h1>My ABOUT PAGE!!!!!</h1>")


def gotoGoogle(request):
    return redirect("https://google.com")


def my_users(request):
    return HttpResponse("<h1>My Users are here </h1>")
