from django.contrib import admin
from solo.admin import SingletonModelAdmin
from ..models.contact_model import (
    ContactPage ,
    Contact
)


@admin.register(Contact)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)



@admin.register(ContactPage)
class ContactPageContentAdmin(SingletonModelAdmin):
    list_display = ('__str__',)