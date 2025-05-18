from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm
from appointments.models import Appointment
from datetime import date

@login_required
def patient_dashboard(request):
    patients = Patient.objects.select_related('user').all()

    appointments = Appointment.objects.filter(patient=request.user).order_by('-date')
    total_appointments = appointments.count()
    upcoming_appointments = appointments.filter(status="Approved").count()  # Upcoming = Approved
    completed_appointments = appointments.filter(status="Completed").count()
    cancelled_appointments = appointments.filter(status="Rejected").count()  # Cancelled = Rejected

    context = {
        'appointments': appointments,
        'total_appointments': total_appointments,
        'upcoming_appointments': upcoming_appointments,
        'completed_appointments': completed_appointments,
        'cancelled_appointments': cancelled_appointments,
        'patient_name': request.user 
    }
    
    return render(request, 'dashboard/patient_dashboard.html', context)


@login_required
def update_patient_profile(request):
    patient = get_object_or_404(Patient, user=request.user)  
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard:patient_dashboard')
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'patients/update_profile.html', {'form': form})

