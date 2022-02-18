from django.contrib import admin
from ..models.contact_model import Contact


@admin.register(Contact)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)