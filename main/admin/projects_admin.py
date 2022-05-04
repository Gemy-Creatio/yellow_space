from django.contrib import admin
from ..models.projectspage_model import Projectspage
from solo.admin import SingletonModelAdmin


@admin.register(Projectspage)
class ProjectspageAdmin(SingletonModelAdmin):
    list_display = ('__str__',)