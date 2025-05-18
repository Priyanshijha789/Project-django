from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from accounts.models import CustomUser
from datetime import date
from patients.models import Patient
from patients.forms import PatientForm
from django.db.models import Sum, Count
from payments.models import Payment
from medicine.models import Medicine,MedicineRequest
@login_required
def doctor_dashboard(request):
    if not hasattr(request.user, 'doctor_profile'):
        return redirect('login')

    appointments = Appointment.objects.filter(doctor=request.user)
    
    # Fix doctor name display
    doctor_name = f"{request.user.first_name} {request.user.last_name}".strip()
    if not doctor_name:
        doctor_name = request.user.username or "Doctor"

    context = {
        'total_appointments': appointments.count(),
        "approved_count": appointments.filter(status="Approved").count(),
        "pending_count": appointments.filter(status="Pending").count(),
        "rejected_count": appointments.filter(status="Rejected").count(),
        "appointments": appointments,
        "doctor_name": doctor_name 
    }

    return render(request, 'dashboard/doctor_dashboard.html', context)

@login_required
def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    if appointment.status == "Pending": 
        appointment.status = "Approved"
        appointment.save()
    return redirect('doctor_dashboard')

@login_required
def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    if appointment.status == "Pending":
        appointment.status = "Rejected"
        appointment.save()
    return redirect('doctor_dashboard')

@login_required
def patient_dashboard(request):
    if not hasattr(request.user, 'patient_profile'):
        return redirect('login')
    # Fetch all appointments for the logged-in patient
    appointments = Appointment.objects.filter(patient=request.user).order_by('-date')
    patient_name = f"{request.user.first_name} {request.user.last_name}".strip()
    if not patient_name:  # Fallback if first/last name is missing
        patient_name = request.user.username
    # Get today's date
    today = date.today()

    # Separate upcoming and past appointments
    upcoming_appointments = appointments.filter(date__gte=today, status="Approved")
    past_appointments = appointments.filter(date__lt=today, status="Completed")

    # Count appointments based on their status
    total_appointments = appointments.count()
    cancelled_appointments = appointments.filter(status="Rejected").count()  

    context = {
        'appointments': appointments,
        'upcoming_appointments': upcoming_appointments.count(),
        'past_appointments': past_appointments.count(),
        'cancelled_appointments': cancelled_appointments,
        'total_appointments': total_appointments,
        'patient_name': patient_name
    }

    return render(request, 'dashboard/patient_dashboard.html', context)
from doctors.models import Doctor
from patients.models import Patient
from appointments.models import Appointment
from rooms.models import RoomBooking
from django.db.models import Count

@login_required
def admin_dashboard(request):
    if request.user.user_type != "admin":
        return render(request, 'dashboard/error.html', {"message": "Unauthorized access!"})

    total_appointments = Appointment.objects.count()
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    total_payments = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    total_people_paid = Payment.objects.values('patient').distinct().count()
    recent_payments = Payment.objects.select_related('patient').order_by('-date')[:5]
    room_booking_data = RoomBooking.objects.values('patient__user__username').annotate(booking_count=Count('id'))
    total_rooms_booked = RoomBooking.objects.count()
    patients_booked = RoomBooking.objects.values('patient__user__username').distinct()
    total_medicines = Medicine.objects.count()
    pending_requests = MedicineRequest.objects.filter(status='Pending').count()
    
    return render(request, 'dashboard/admin_dashboard.html', {
        'admin_name': request.user.get_full_name() or request.user.username,
        'total_appointments': total_appointments,
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'doctors': doctors,
        'patients': patients,
        'total_payments': total_payments,
        'total_people_paid': total_people_paid,
        'recent_payments': recent_payments,
        'room_booking_data': room_booking_data,
        'total_rooms_booked': total_rooms_booked,
        'patients_booked': patients_booked,
        'total_medicines': total_medicines,
        'pending_requests': pending_requests,
        
    })
@login_required
def redirect_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_doctor():
            return redirect('doctor_dashboard')
        elif request.user.is_patient():
            return redirect('patient_dashboard')
        elif request.user.user_type == "admin":
            return redirect('admin_dashboard')
        elif request.user.user_type == "staff":
            return redirect('staff_dashboard')
        elif request.user.user_type == "receptionist":
            return redirect('receptionist_dashboard')
    return redirect('login')
from django.utils import timezone

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
    return render(request, 'dashboard/receptionist_dashboard.html', context)


from django.shortcuts import render
from payments.models import Payment 
from patients.models import Patient
from django.db.models import Sum
from medicalhistory.models import MedicalHistory  

@login_required
def staff_dashboard(request):
    patients = Patient.objects.all()
    medicines = Medicine.objects.all()
    return render(request, 'dashboard/staff_dashboard.html', {'medicines': medicines})
