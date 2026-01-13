from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department", "designation", "is_active")
    search_fields = ("name", "email", "department")
    list_filter = ("department", "is_active")
