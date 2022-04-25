from django.contrib import admin
from ..models.about_model import AboutPage
from solo.admin import SingletonModelAdmin


@admin.register(AboutPage)
class AboutPageAdmin(SingletonModelAdmin):
    list_display = ('__str__',)