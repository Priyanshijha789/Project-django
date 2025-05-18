from django import forms
from .models import PatientAdmission

class PatientAdmissionForm(forms.ModelForm):
    class Meta:
        model = PatientAdmission
        fields = ['patient', 'doctor', 'room_number']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
from .models import Bill
from django import forms

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'amount', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
