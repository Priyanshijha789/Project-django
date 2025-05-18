from django import forms
from .models import Medicine, MedicineRequest

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price', 'stock', 'image']

class MedicineRequestForm(forms.ModelForm):
    class Meta:
        model = MedicineRequest
        fields = ['name', 'reason']
