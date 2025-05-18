from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.core.files.base import ContentFile
import io

def generate_invoice_pdf(payment):
    template = render_to_string('payments/invoice_template.html', {'payment': payment})
    pdf_file = io.BytesIO()
    pisa.CreatePDF(io.StringIO(template), dest=pdf_file)
    return pdf_file

def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.patient = request.user
            payment.save()

            pdf = generate_invoice_pdf(payment)
            payment.invoice_pdf.save(f'invoice_{payment.id}.pdf', ContentFile(pdf.getvalue()))
            payment.save()

            return redirect('view_invoices')
    else:
        form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'form': form})

def view_invoices(request):
    invoices = Payment.objects.filter(patient=request.user)
    return render(request, 'payments/view_invoices.html', {'invoices': invoices})
