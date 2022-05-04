from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from django.templatetags.static import static

class Blogpage(SingletonModel):
    background_image = models.ImageField(null=True ,  upload_to='background/')
    title_en = models.CharField(max_length=255,null=True , blank=True)
    title_ar = models.CharField(max_length=255,null=True , blank=True)
    content_en = RichTextField(max_length=255,null=True)
    content_ar = RichTextField(max_length=255,null=True)
    def blogs(self):
        from furniture.models.wood_information_model import WoodInformation
        return WoodInformation.objects.order_by('-publication_date').filter(is_ready=True)[:4]
    @property
    def image_url(self):
        if self.background_image and hasattr(self.background_image, 'url'):
             return self.background_image.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    class Meta(SingletonModel.Meta):
        pass
