from operator import mod
from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField

class Blogpage(SingletonModel):
    background_image = models.ImageField(null=True ,  upload_to='background/')
    title_en = models.CharField(max_length=255,null=True , blank=True)
    title_ar = models.CharField(max_length=255,null=True , blank=True)
    content_en = RichTextField(max_length=255,null=True)
    content_ar = RichTextField(max_length=255,null=True)
    class Meta(SingletonModel.Meta):
        pass
