from django.urls import path
from . import views

app_name = 'receptionist'

urlpatterns = [
    path('dashboard/', views.receptionist_dashboard, name='dashboard'),
    path('appointments/', views.today_appointments, name='today_appointments'),
    path('appointments/approve/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('appointments/reject/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),


]
