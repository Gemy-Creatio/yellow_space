from django_extensions.db.fields import AutoSlugField
from ordered_model.models import OrderedModel
from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from  projects.models import ProjectTypes
from django.templatetags.static import static


class Furniture(OrderedModel):
    name_ar = RichTextField(null=True, help_text='Name of Furniture')
    name_en = RichTextField(null=True, help_text='Name of Furniture')
    slug = AutoSlugField(populate_from="name_en")
    description_1_en = RichTextField(null=True, help_text='Description of Wood Type')
    description_2_en = RichTextField(null=True, help_text='Description of Materials type')
    description_3_en = RichTextField(null=True, help_text='Description ')
    description_1_ar = RichTextField(null=True, help_text='Description of Wood Type')
    description_2_ar = RichTextField(null=True, help_text='Description of Materials type')
    description_3_ar = RichTextField(null=True, help_text='Description ')
    size = models.CharField(null=True, blank=True, max_length=255, help_text='Dimensions of Item ')
    code = models.CharField(null=True, blank=True, max_length=255, unique=True, help_text='Code For Furniture Item')
    picture_1 = models.ImageField(upload_to='furniture', help_text='first Image of item',null=True, blank=True)
    picture_2 = models.ImageField(upload_to='furniture', help_text='second Image of item', null=True, blank=True)
    picture_3 = models.ImageField(upload_to='furniture', help_text='third Image of item', null=True, blank=True)
    picture_4 = models.ImageField(upload_to='furniture', help_text='fourth Image of item', null=True, blank=True)
    is_for_offer = models.BooleanField(null=True, blank=True)
    offer_value = models.SmallIntegerField(null=True, blank=True)
    color = ColorField(null=True)
    catgeory = models.ForeignKey(ProjectTypes, on_delete=models.CASCADE , related_name='types')
    date_added = models.DateField(auto_now_add=True, null=True)
    @property
    def picture_1_url(self):
        if self.picture_1 and hasattr(self.picture_1, 'url'):
             return self.picture_1.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    @property
    def picture_2_url(self):
        if self.picture_2 and hasattr(self.picture_2, 'url'):
             return self.picture_2.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    @property
    def picture_3_url(self):
        if self.picture_3 and hasattr(self.picture_3, 'url'):
             return self.picture_3.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    @property
    def picture_4_url(self):
        if self.picture_4 and hasattr(self.picture_4, 'url'):
             return self.picture_4.url
        else:
            return static("assets/img/YS logo F-01.jpg")

    def __str__(self):
        return f'{self.name_ar} , {self.code} '
