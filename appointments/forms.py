from django import forms
from .models import Appointment
from accounts.models import CustomUser

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type="doctor"),
        required=True,
        empty_label="Select Doctor",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    patient = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type="patient"),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'age', 'date', 'time', 'gender', 'medical_history']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def save(self, commit=True, user=None):
        appointment = super().save(commit=False)
        if user:
            if user.user_type == "receptionist" and self.cleaned_data.get("patient"):
                appointment.patient = self.cleaned_data["patient"]
            else:
                appointment.patient = user 
        if commit:
            appointment.save()
        return appointment
