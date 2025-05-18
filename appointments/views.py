from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm

def book_appointment(request):
    # Only authenticated users can book appointments
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to book an appointment.")
        return redirect("home")

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            # For patients: they can book only their own appointments
            if request.user.user_type == "patient":
                appointment.patient = request.user
            # For receptionists: they can book for other patients
            elif request.user.user_type == "receptionist":
                # receptionist selects the patient while booking
                if not form.cleaned_data.get('patient'):
                    messages.error(request, "Please select a patient.")
                    return render(request, "appointments/book_appointment.html", {"form": form})
            appointment.save()
            messages.success(request, "Appointment booked successfully! Do you want to book another?")
            return redirect("appointment_success")
    else:
        form = AppointmentForm()

    return render(request, "appointments/book_appointment.html", {"form": form})

def appointment_success(request):
    return render(request, "appointments/success.html")

def patient_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != "patient":
        return redirect("home")
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, "dashboard/patient_dashboard.html", {"appointments": appointments})

def doctor_dashboard(request):
    if not request.user.is_authenticated or request.user.user_type != "doctor":
        return redirect("home")
    appointments = Appointment.objects.filter(doctor=request.user)
    return render(request, "dashboard/doctor_dashboard.html", {"appointments": appointments})

def approve_appointment(request, appointment_id):
    if not request.user.is_authenticated or request.user.user_type != "doctor":
        return redirect("home")

    appointment = Appointment.objects.get(id=appointment_id, doctor=request.user)
    appointment.status = "approved"
    appointment.save()
    messages.success(request, "Appointment approved.")
    return redirect("doctor_dashboard")

def reject_appointment(request, appointment_id):
    if not request.user.is_authenticated or request.user.user_type != "doctor":
        return redirect("home")

    appointment = Appointment.objects.get(id=appointment_id, doctor=request.user)
    appointment.status = "rejected"
    appointment.save()
    messages.error(request, "Appointment rejected.")
    return redirect("doctor_dashboard")
