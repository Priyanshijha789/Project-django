from django.urls import path
from .views import patient_dashboard, update_patient_profile
from . import views
app_name = 'patients'

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name="dashboard"),
    path('update-profile/',views.update_patient_profile, name="update_profile"),
]
