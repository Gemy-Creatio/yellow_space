from django.contrib import admin
from ..models.faq_model import FAQ


@admin.register(FAQ)
class FAQPageAdmin(admin.ModelAdmin):
    list_display = ('__str__',)