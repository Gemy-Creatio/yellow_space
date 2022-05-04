from ordered_model.admin import OrderedModelAdmin
from django.contrib import admin
from ..models import ProjectTypes



@admin.register(ProjectTypes)
class ProjectTypesAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
