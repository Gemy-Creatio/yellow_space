from django_extensions.db.fields import AutoSlugField
from ordered_model.models import OrderedModel
from django.templatetags.static import static
from django.db import models
from ckeditor.fields import RichTextField


class ProjectTypes(OrderedModel):
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    content_ar = RichTextField()
    content_en = RichTextField()
    slug = AutoSlugField(populate_from="name_en")
    picture = models.ImageField(upload_to="proj-icons/")
   
    def image_url(self):
        return self.picture.url if self.picture else static("assets/img/logo.png")


    def __str__(self):
        return f"category name is :{self.name_ar}"
