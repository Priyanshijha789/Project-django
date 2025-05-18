from django.urls import path
from .views import doctor_dashboard, patient_dashboard, admin_dashboard, receptionist_dashboard, staff_dashboard, redirect_dashboard
app_name = 'dashboard'
urlpatterns = [
    path('', redirect_dashboard, name="redirect_dashboard"),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/', patient_dashboard, name='patient_dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('receptionist/', receptionist_dashboard, name='receptionist_dashboard'),
    path('staff/', staff_dashboard, name='staff_dashboard'),
]
