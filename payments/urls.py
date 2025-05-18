from django.urls import path
from . import views

urlpatterns = [
    path('make-payment/', views.make_payment, name='make_payment'),
    path('invoices/', views.view_invoices, name='view_invoices'),
]
