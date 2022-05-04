from django.contrib import admin
from ..models.staff_model import Staff


@admin.register(Staff)
class StaffPageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)