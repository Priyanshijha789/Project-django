from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__username', 'specialization')
    actions = ['approve_selected']

    def approve_selected(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected doctors approved successfully.")
    approve_selected.short_description = "Approve selected doctors"
