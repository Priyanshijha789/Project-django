from django.db import models
from patients.models import Patient  # adjust this import based on your app
# or from accounts.models import User if using a custom model

class Room(models.Model):
    ROOM_TYPES = (
        ('General', 'General'),
        ('Private', 'Private'),
        ('ICU', 'ICU'),
    )
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_number} - {self.room_type}"

class RoomBooking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Booked', 'Booked'), ('Discharged', 'Discharged')], default='Booked')

    def __str__(self):
        return f"{self.patient} - {self.room}"
