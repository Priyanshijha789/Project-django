from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientAdmissionForm
from .models import PatientAdmission
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def admit_patient(request):
    if request.method == 'POST':
        form = PatientAdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient admitted successfully.")
            return redirect('staff:admissions_list')
    else:
        form = PatientAdmissionForm()
    return render(request, 'staff/admit_patient.html', {'form': form})
@login_required
def admissions_list(request):
    admissions = PatientAdmission.objects.all().order_by('-admission_date')
    return render(request, 'staff/admissions_list.html', {'admissions': admissions})
from django.utils import timezone

@login_required
def discharge_patient(request, admission_id):
    admission = get_object_or_404(PatientAdmission, id=admission_id)

    if admission.status == 'Admitted':
        admission.status = 'Discharged'
        admission.discharge_date = timezone.now().date()
        admission.save()
        messages.success(request, f"{admission.patient.user.username} discharged successfully.")
    else:
        messages.warning(request, "Patient already discharged.")

    return redirect('staff:admissions_list')
from .forms import BillForm
from .models import Bill

@login_required
def create_bill(request):
    if request.user.user_type not in ['staff', 'admin']:
        return redirect('login')

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.issued_by = request.user
            bill.save()
            messages.success(request, "Bill created successfully.")
            return redirect('staff:bill_list')
    else:
        form = BillForm()

    return render(request, 'staff/create_bill.html', {'form': form})


@login_required
def bill_list(request):
    if request.user.user_type not in ['staff', 'admin']:
        return redirect('login')

    bills = Bill.objects.all().order_by('-date_issued')
    return render(request, 'staff/bill_list.html', {'bills': bills})
