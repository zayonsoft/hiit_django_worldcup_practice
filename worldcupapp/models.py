from django.db import models

# Create your models here.


class Student(models.Model):
    matric_number = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.year}"
