from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES_FOR_SIGNUP = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES_FOR_SIGNUP,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data['user_type']
        if commit:
            user.save()
        return user

