"""hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appointments.views import (
    appointment_success, book_appointment,approve_appointment,reject_appointment
)
from . import views  # Importing views from current directory
from medicalhistory.views import add_medical_history,view_medical_history
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Account related URLs
    path('dashboard/', include('dashboard.urls')),  # Dashboard URLs
    path('book/', book_appointment, name='book_appointment'),
    path('success/', appointment_success, name='appointment_success'),
    path('doctors/', include('doctors.urls')),
    path('patients/', include('patients.urls')),  # Patient-related URLs
    path('', views.home, name='home'),  # Home Page
    path('appointments/',include('appointments.urls')),
    path('payments/', include('payments.urls')),
    path('rooms/', include('rooms.urls')),
    path('medicine/', include('medicine.urls')),
    path('history/',include('medicalhistory.urls')),
    path('receptionist/', include('receptionist.urls', namespace='receptionist')),
    path('staff/',include('staff.urls',namespace='staff')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



