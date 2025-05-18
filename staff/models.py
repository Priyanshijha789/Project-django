from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from accounts.models import CustomUser

# 🏥 Patient Admission
class PatientAdmission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    room_number = models.CharField(max_length=10)
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("Admitted", "Admitted"), ("Discharged", "Discharged")], default="Admitted")

    def __str__(self):
        return f"{self.patient.user.username} - Room {self.room_number}"


# 🧪 Lab Report
class LabReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)  # e.g., Blood Test, X-Ray
    description = models.TextField()
    report_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.report_type} - {self.patient.user.username}"


# 💳 Billing
class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    date_issued = models.DateField(auto_now_add=True)
    issued_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Bill - {self.patient.user.username} - ₹{self.amount}"
class DischargeRequest(models.Model):
    admission = models.ForeignKey(PatientAdmission, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")], default="Pending")

    def __str__(self):
        return f"{self.admission.patient.user.username} - {self.status}"
