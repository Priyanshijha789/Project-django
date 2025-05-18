from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from patients.models import Patient
from accounts.models import CustomUser
from django.utils import timezone
from django.contrib import messages

@login_required
def receptionist_dashboard(request):
    if request.user.user_type != 'receptionist':
        return redirect('login')

    today = timezone.now().date()
    appointments_today = Appointment.objects.filter(date__date=today)

    stats = [
        ("Today's Appointments", appointments_today.count(), '#0d6efd'),
        ("Approved Appointments", appointments_today.filter(status='Approved').count(), '#0a58ca'),
        ("Pending Appointments", appointments_today.filter(status='Pending').count(), '#0b5ed7'),
        ("Rejected Appointments", appointments_today.filter(status='Rejected').count(), '#31d2f2'),
    ]

    context = {
        'stats': stats,
        'approved_count': stats[1][1],
        'pending_count': stats[2][1],
        'rejected_count': stats[3][1],
    }
    return render(request, 'receptionist/receptionist_dashboard.html', context)

@login_required
def today_appointments(request):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')
    today = timezone.now().date()
    appointments = Appointment.objects.filter(date__date=today)
    return render(request, 'receptionist/today_appointments.html', {'appointments': appointments})

@login_required
def approve_appointment(request, appointment_id):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Approved"
    appointment.save()
    messages.success(request, "Appointment approved successfully!")
    return redirect('receptionist:today_appointments')

@login_required
def reject_appointment(request, appointment_id):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "Rejected"
    appointment.save()
    messages.error(request, "Appointment rejected.")
    return redirect('receptionist:today_appointments')

@login_required
def add_patient(request):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = generate_random_password()

        user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type='patient')
        Patient.objects.create(user=user, age=age, gender=gender)

        messages.success(request, f"Patient {username} added successfully! Password: {password}")
        return redirect('receptionist:add_patient')

    return render(request, 'receptionist/add_patient.html')
from patients.models import Patient

@login_required
def patient_list(request):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')

    patients = Patient.objects.select_related('user').all()
    return render(request, 'receptionist/patient_list.html', {'patients': patients})
from django.shortcuts import get_object_or_404
from patients.models import Patient
from accounts.models import CustomUser

@login_required
def edit_patient(request, patient_id):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')

    patient = get_object_or_404(Patient, id=patient_id)
    user = patient.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        user.save()
        patient.save()
        messages.success(request, 'Patient updated successfully!')
        return redirect('receptionist:patient_list')

    return render(request, 'receptionist/edit_patient.html', {'patient': patient})
    

@login_required
def delete_patient(request, patient_id):
    if request.user.user_type not in ['receptionist', 'admin']:
        return redirect('login')

    patient = get_object_or_404(Patient, id=patient_id)
    patient.user.delete()  # Delete linked user also
    patient.delete()
    messages.success(request, 'Patient deleted successfully!')
    return redirect('receptionist:patient_list')
