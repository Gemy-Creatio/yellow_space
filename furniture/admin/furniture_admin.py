from furniture.models.furniture_model import Furniture
from ordered_model.admin import OrderedModelAdmin
from django.contrib import admin


@admin.register(Furniture)
class FurnitureAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
