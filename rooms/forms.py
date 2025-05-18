from django import forms
from .models import RoomBooking

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['room']
