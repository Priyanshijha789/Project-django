from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from doctors.models import Doctor 

@login_required
def doctor_dashboard(request):
    try:
        doctor = request.user.doctor_profile
    except Doctor.DoesNotExist:
        return redirect('login')
    if not doctor.is_approved:
        return render(request, 'doctors/not_approved.html') 
    appointments = Appointment.objects.filter(doctor=request.user)

    # Appointment stats
    total_appointments = appointments.count()
    approved_count = appointments.filter(status="Approved").count()
    pending_count = appointments.filter(status="Pending").count()
    rejected_count = appointments.filter(status="Rejected").count()

    return render(request, 'doctors/doctor_dashboard.html', {
        'total_appointments': total_appointments,
        "approved_count": approved_count,
        "pending_count": pending_count,
        "rejected_count": rejected_count,
        "appointments": appointments,  
    })


@login_required
def approve_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    appointment.approved = True
    if appointment.status == "Pending":
        appointment.status = "Approved"
        appointment.save()
    return redirect('dashboard:doctor_dashboard')


@login_required
def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    if appointment.status == "Pending":
        appointment.status = "Rejected"
        appointment.save()
    return redirect('dashboard:doctor_dashboard')
from staff.models import PatientAdmission
from django.contrib.auth.decorators import login_required

@login_required
def doctor_admissions(request):
    if not hasattr(request.user, 'doctor_profile'):
        return redirect('login')
    admissions = PatientAdmission.objects.filter(doctor=request.user.doctor_profile, status="Admitted")
    return render(request, 'doctors/my_admissions.html', {'admissions': admissions})

@login_required
def request_discharge(request, admission_id):
    admission = get_object_or_404(PatientAdmission, id=admission_id, doctor=request.user.doctor_profile)

    # Prevent duplicate request
    if not DischargeRequest.objects.filter(admission=admission, status="Pending").exists():
        DischargeRequest.objects.create(admission=admission, doctor=admission.doctor)
        messages.success(request, "Discharge request submitted.")
    else:
        messages.warning(request, "Request already submitted.")

    return redirect('doctor_admissions')

