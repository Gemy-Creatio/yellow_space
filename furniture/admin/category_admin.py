from ordered_model.admin import OrderedModelAdmin
from django.contrib import admin
from ..models.category_model import Category



@admin.register(Category)
class CategoryAdmin(OrderedModelAdmin):
    list_display = ("__str__",)
