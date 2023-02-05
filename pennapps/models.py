from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)
    firstName = models.CharField(max_length=30, default="first", verbose_name="First_name")
    lastName = models.CharField(max_length=30, default="last", verbose_name="Last_name")

class Application(models.Model):
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]

    school = models.CharField(max_length=50, default="", verbose_name="School")
    year = models.CharField(max_length=30, default="", verbose_name="Year")
    major = models.CharField(max_length=50, default="", verbose_name="Major")
    phone_number = models.CharField(max_length=20, default="", verbose_name="Phone_number")
    birthday = models.CharField(max_length=20, default="", verbose_name="Birthday")

    q1 = models.TextField(default='', verbose_name="Q1_answer")
    q2 = models.TextField(default='', verbose_name="Q2_answer")

    first_hackathon = models.CharField(max_length=30, default="", verbose_name="First_hackathon")
    team_member_1 = models.EmailField(default='', verbose_name="Team_member_1")
    team_member_2 = models.EmailField(default='', verbose_name="Team_member_2")
    team_member_3 = models.EmailField(default='', verbose_name="Team_member_3")

    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default='', null=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="PROC")

    def __str__(self):
        return f"{self.applicant} {self.status}"