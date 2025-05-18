from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('admissions/add/', views.admit_patient, name='admit_patient'),
    path('admissions/', views.admissions_list, name='admissions_list'),  # for listing
    path('admissions/discharge/<int:admission_id>/', views.discharge_patient, name='discharge_patient'),
    path('billing/create/', views.create_bill, name='create_bill'),
    path('billing/', views.bill_list, name='bill_list'),

]
