from django.urls import path
from . import views
from .views import manage_medicine

urlpatterns = [
    path('store/', views.medicine_store, name='medicine_store'),
    path('add-to-cart/<int:medicine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),

    path('request/', views.request_medicine, name='request_medicine'),

    path('admin/manage_medicine/', manage_medicine, name='manage_medicine'),
    path('admin/add-medicine/', views.add_medicine, name='add_medicine'),
    path('admin/doctor-requests/', views.doctor_requests, name='doctor_requests'),
    path('admin/approve-request/<int:req_id>/', views.approve_request, name='approve_request'),
    path('staff/requests/', views.staff_requests, name='staff_requests'),
    path('staff/approve/<int:req_id>/', views.staff_approve_request, name='staff_approve_request'),
    path('staff/update/<int:med_id>/', views.update_stock, name='update_stock'),
    path('staff/reject/<int:req_id>/', views.staff_reject_request, name='staff_reject_request'),

]
