from django.shortcuts import render, redirect
from .models import Room, RoomBooking
from .forms import RoomBookingForm
from patients.models import Patient  # adjust based on your setup
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def book_room(request):
    patient = Patient.objects.get(user=request.user)
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.patient = patient
            booking.save()
            booking.room.is_available = False
            booking.room.save()
            messages.success(request, "✅ Room booked successfully!")
            return redirect('book_room')  
    else:
        form = RoomBookingForm()
    return render(request, 'rooms/book_room.html', {'form': form})

@login_required
def my_bookings(request):
    patient = Patient.objects.get(user=request.user)
    bookings = RoomBooking.objects.filter(patient=patient)
    return render(request, 'rooms/my_bookings.html', {'bookings': bookings})
