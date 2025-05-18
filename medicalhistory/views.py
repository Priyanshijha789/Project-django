from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalHistory
from .forms import MedicalHistoryForm
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required

@login_required
def add_medical_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    doctor = request.user.doctor_profile
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.patient = patient
            history.doctor = doctor
            history.save()
            return redirect('dashboard:doctor_dashboard')
    else:
        form = MedicalHistoryForm()
    return render(request, 'medicalhistory/add_history.html', {'form': form, 'patient': patient})

@login_required
def view_medical_history(request):
    if hasattr(request.user, 'patient_profile'):
        histories = MedicalHistory.objects.filter(patient=request.user.patient_profile)
    elif hasattr(request.user, 'doctor_profile'):
        histories = MedicalHistory.objects.filter(doctor=request.user.doctor_profile)
    else:
        histories = []
    return render(request, 'medicalhistory/history_list.html', {'histories': histories})
