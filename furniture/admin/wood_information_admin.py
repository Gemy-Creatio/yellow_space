from furniture.models.wood_information_model import WoodInformation
from ordered_model.admin import OrderedModelAdmin
from django.contrib import admin


@admin.register(WoodInformation)
class WoodInformation(OrderedModelAdmin):
    list_display = ("__str__",)