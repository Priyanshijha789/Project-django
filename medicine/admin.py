from django.contrib import admin
from .models import Medicine, MedicineRequest, CartItem, Order, OrderItem

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # changed 'quantity' to 'stock'
    search_fields = ('name',)

@admin.register(MedicineRequest)
class MedicineRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'doctor__username')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'medicine', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'ordered_at', 'is_paid')  # replaced 'status' with 'is_paid'
    list_filter = ('is_paid',)
    search_fields = ('user__username', 'id')
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'medicine', 'quantity')
