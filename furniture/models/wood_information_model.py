from django_extensions.db.fields import AutoSlugField
from ordered_model.models import OrderedModel
from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class WoodInformation(OrderedModel):
    wood_name_en = models.CharField(max_length=255, blank=True, null=True, help_text='Name of Wood')
    wood_name_ar = models.CharField(max_length=255, blank=True, null=True, help_text='Name of Wood')
    slug = AutoSlugField(populate_from="wood_name_en")
    description_1_en = RichTextField(null=True)
    description_2_en = RichTextField(null=True)
    description_3_en = RichTextField(null=True)
    description_4_en = RichTextField(null=True)
    description_1_ar = RichTextField(null=True)
    description_2_ar = RichTextField(null=True)
    description_3_ar = RichTextField(null=True)
    description_4_ar = RichTextField(null=True)
    image_1 = models.ImageField(upload_to='woods/')
    image_2 = models.ImageField(upload_to='woods/', null=True)
    image_3 = models.ImageField(upload_to='woods/', null=True)
    color = ColorField(null=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.wood_name
