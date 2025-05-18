from django.urls import path
from .views import (
    book_appointment, appointment_success,
    approve_appointment, reject_appointment
)

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('success/', appointment_success, name='appointment_success'),
    path('approve/<int:appointment_id>/', approve_appointment, name='approve_appointment'),
    path('reject/<int:appointment_id>/', reject_appointment, name='reject_appointment'),
]
