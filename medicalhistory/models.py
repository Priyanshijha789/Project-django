from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True, null=True)
    visit_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.visit_date}"
