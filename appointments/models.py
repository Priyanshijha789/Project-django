from django.db import models
from accounts.models import CustomUser
class Appointment(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patient_appointments")
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="doctor_appointments")
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")], null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
