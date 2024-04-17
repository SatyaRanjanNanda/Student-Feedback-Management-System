from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name

class Faculty(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Feedback(models.Model):
    teacher = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,null=True)
    clarity = models.IntegerField()
    engagement = models.IntegerField()
    approachability = models.IntegerField()
    management = models.IntegerField()
    fairness = models.IntegerField()
    encouragement = models.IntegerField()
    organization = models.IntegerField()
    teaching = models.IntegerField()
    satisfaction = models.IntegerField()
    message=models.TextField(null=True)

    def __str__(self):
        return self.teacher


class Admin_Dashboard(models.Model):
    total_students = models.IntegerField(default=0)
    total_faculties = models.IntegerField(default=0)
    total_feedback = models.IntegerField(default=0)

    def __str__(self):
        return str(self.total_students)
