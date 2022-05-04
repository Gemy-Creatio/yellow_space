from django.db import models
from django.templatetags.static import static


class Staff(models.Model):
    name_ar = models.CharField(max_length=255, blank=True , null=True)
    namr_en = models.CharField(max_length=255, blank=True , null=True)
    title_en = models.CharField(max_length=255, blank=True , null=True)
    title_ar = models.CharField(max_length=255, blank=True , null=True)
    pic = models.ImageField(null=True , blank=True ,upload_to='staff_pic/')
    instagram_url = models.URLField(null=True , blank=True)
    facebook_url = models.URLField(null=True , blank=True)
    twitter_url = models.URLField(null=True , blank=True)
    linkedin_url = models.URLField(null=True , blank=True)
    @property
    def pic_url(self):
        if self.pic and hasattr(self.pic, 'url'):
             return self.pic.url
        else:
            return static("assets/img/user.png")
    @property
    def data_os(self):
        return self.pk * 100

    def __str__(self):
        return f"{self.namr_en} {self.title_en}"