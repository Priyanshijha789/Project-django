from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = EmailAuthenticationForm

    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'doctor':
            return reverse_lazy('dashboard:doctor_dashboard')
        elif user.user_type == 'patient':
            return reverse_lazy('dashboard:patient_dashboard')
        elif user.user_type == 'staff':
            return reverse_lazy('dashboard:staff_dashboard')
        elif user.user_type == 'receptionist':
            return reverse_lazy('dashboard:receptionist_dashboard')
        else:
            return reverse_lazy('dashboard:admin_dashboard')

class CustomSignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')
