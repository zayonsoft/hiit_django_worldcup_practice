from django.shortcuts import render, redirect
from django.http import HttpResponse
from worldcupapp.models import Student
from django.contrib import messages


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


def student(request, pk):
    student = Student.objects.get(id=pk)
    context = {"student": student}
    return render(request, "view-student.html", context)


def add_student(request):
    if request.method == "POST":
        matric_number = request.POST.get("matric_number")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        middle_name = request.POST.get("middle_name")
        year = request.POST.get("year")
        course = request.POST.get("course")

        if not (
            matric_number
            and first_name
            and last_name
            and middle_name
            and year
            and course
        ):
            messages.error(request, "Fill in all fields")
            return redirect("add_students")

        Student.objects.create(
            matric_number=matric_number,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            year=year,
            course=course,
        )
        messages.success(request, "Student added successfully")
        return redirect("students")

    return render(request, "add-student.html")


def gotoGoogle(request):
    return redirect("https://google.com")


def my_users(request):
    return HttpResponse("<h1>My Users are here </h1>")
