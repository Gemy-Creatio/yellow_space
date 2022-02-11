from django.contrib import admin
from ..models.homepgae_content import Homepage
from solo.admin import SingletonModelAdmin


@admin.register(Homepage)
class HomePageAdmin(SingletonModelAdmin):
    list_display = ('__str__',)
