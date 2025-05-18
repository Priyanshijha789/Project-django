# medicine/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import *
def is_admin(user):
    return user.is_superuser
def manage_medicine(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine/admin_manage_medicine.html', {'medicines': medicines})
def add_medicine(request):
    form = MedicineForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('manage_medicine')
    return render(request, 'medicine/add_medicine.html', {'form': form})
def doctor_requests(request):
    requests = MedicineRequest.objects.filter(status='Pending')
    return render(request, 'medicine/doctor_requests.html', {'requests': requests})
def approve_request(request, req_id):
    req = get_object_or_404(MedicineRequest, id=req_id)
    req.status = 'Approved'
    req.save()
    return redirect('doctor_requests')

# ---------------- Doctor -------------------

@login_required
def request_medicine(request):
    form = MedicineRequestForm(request.POST or None)
    if form.is_valid():
        med = form.save(commit=False)
        med.doctor = request.user
        med.save()
        return redirect('dashboard:doctor_dashboard')
    return render(request, 'medicine/request_medicine.html', {'form': form})

# ---------------- Patient -------------------

@login_required
def medicine_store(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine/store.html', {'medicines': medicines})

@login_required
def add_to_cart(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    item, created = CartItem.objects.get_or_create(user=request.user, medicine=medicine)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'medicine/cart.html', {'cart_items': cart_items, 'total': total})
from payments.models import Payment
from payments.views import generate_invoice_pdf  # reuse your function
from django.core.files.base import ContentFile

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        is_paid = True if payment_method == 'cod' else False

        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            payment_method=payment_method,
            is_paid=is_paid,
            status='paid' if is_paid else 'pending'
        )

        for item in cart_items:
            OrderItem.objects.create(order=order, medicine=item.medicine, quantity=item.quantity)
            item.medicine.stock -= item.quantity
            item.medicine.save()
            item.delete()

        # Create a payment entry
        payment = Payment.objects.create(
            patient=request.user,
            order=order,
            amount=total
        )

        # Generate PDF Invoice
        pdf = generate_invoice_pdf(payment)
        payment.invoice_pdf.save(f'invoice_{payment.id}.pdf', ContentFile(pdf.getvalue()))
        payment.save()

        return render(request, 'medicine/order_success.html', {'order': order})

    return render(request, 'medicine/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'medicine/order_history.html', {'orders': orders})
from django.contrib.auth.decorators import login_required
from .models import Medicine, MedicineRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

@login_required
def staff_requests(request):
    if request.user.user_type != "staff":
        return redirect('login')
    requests = MedicineRequest.objects.filter(status='Pending')
    return render(request, 'medicine/staff_requests.html', {'requests': requests})

@login_required
def staff_approve_request(request, req_id):
    if request.user.user_type != "staff":
        return redirect('login')
    req = get_object_or_404(MedicineRequest, id=req_id)
    req.status = 'Approved'
    req.save()
    messages.success(request, 'Request approved successfully!')
    return redirect('staff_requests')

@login_required
def update_stock(request, med_id):
    if request.user.user_type != "staff":
        return redirect('login')
    medicine = get_object_or_404(Medicine, id=med_id)
    if request.method == "POST":
        new_stock = int(request.POST.get("stock"))
        medicine.stock = new_stock
        medicine.save()
        messages.success(request, 'Stock updated!')
        return redirect('dashboard:staff_dashboard')
    return render(request, 'medicine/update_stock.html', {'medicine': medicine})
@login_required
def staff_reject_request(request, req_id):
    if request.user.user_type != "staff":
        return redirect('login')
    req = get_object_or_404(MedicineRequest, id=req_id)
    req.status = 'Rejected'
    req.save()
    messages.error(request, 'Request rejected.')
    return redirect('dashboard:staff_requests')
