from django_extensions.db.fields import AutoSlugField
from ordered_model.models import OrderedModel
from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from furniture.models.category_model import Category
from django.templatetags.static import static

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
    is_ready = models.BooleanField(null=True , blank=True , default=False)
    publication_date = models.DateField(null=True, auto_now_add=True)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , related_name='cats')
    @property
    def image_1_url(self):
        if self.image_1 and hasattr(self.image_1, 'url'):
             return self.image_1.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    @property
    def image_2_url(self):
        if self.image_2 and hasattr(self.image_2, 'url'):
             return self.image_2.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    @property
    def image_3_url(self):
        if self.image_3 and hasattr(self.image_3, 'url'):
             return self.image_3.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.wood_name_en
