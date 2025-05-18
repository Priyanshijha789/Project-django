from django.urls import path
from .views import doctor_dashboard, approve_appointment, reject_appointment
from . import views
app_name = 'doctors'

urlpatterns = [
    path('dashboard/', doctor_dashboard, name='dashboard'),
    path('appointment/<int:appointment_id>/approve/', approve_appointment, name='approve'),
    path('appointment/<int:appointment_id>/reject/', reject_appointment, name='reject'),
    path('admissions/', views.doctor_admissions, name='doctor_admissions'),
    path('admissions/request-discharge/<int:admission_id>/', views.request_discharge, name='request_discharge'),


]
