from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from django.templatetags.static import static

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ContactPage(SingletonModel):
    head_ar = models.CharField(max_length=255 , null=True , blank=True)
    head_en = models.CharField(max_length=255 , null=True , blank=True)
    description_en = RichTextField()
    description_ar = RichTextField()
    background = models.ImageField(null=True ,  upload_to='background/')
    @property
    def image_url(self):
        if self.background and hasattr(self.background, 'url'):
             return self.background.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    class Meta(SingletonModel.Meta):
        pass
