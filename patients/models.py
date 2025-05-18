from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="patient_profile"
    )
    age = models.PositiveIntegerField(default=0) 
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        default='Other'
    )

    def __str__(self):
        return self.user.username