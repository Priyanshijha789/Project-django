from django.db import models
from django.conf import settings
from medicine.models import Order  # make sure this import is valid

class Payment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    invoice_pdf = models.FileField(upload_to='invoices/', blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} - ₹{self.amount} (Order #{self.order.id if self.order else 'N/A'})"
