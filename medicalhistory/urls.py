from django.urls import path
from . import views

app_name = 'medicalhistory'

urlpatterns = [
    path('add/<int:patient_id>/', views.add_medical_history, name='add_history'),
    path('view/', views.view_medical_history, name='view_history'),
]