from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from django.db import models
from django.templatetags.static import static


class AboutPage(SingletonModel):
    title_ar = models.CharField(null=True , blank=True , max_length=255)
    title_en = models.CharField(null=True , blank=True , max_length=255)
    content_ar = RichTextField()
    content_en = RichTextField()
    background = models.ImageField(upload_to='backgrounds/', null=True)
    video_url = models.URLField(null=True , blank=True)
    class Meta(SingletonModel.Meta):
        pass
    def faqs(self):
        from .faq_model import FAQ
        return FAQ.objects.order_by('-pk').filter(is_show=True)
    def categories(self):
        from projects.models import ProjectTypes
        return ProjectTypes.objects.all()
    @property
    def image_url(self):
        if self.background and hasattr(self.background, 'url'):
             return self.background.url
        else:
            return static("assets/img/YS logo F-01.jpg")
    def __str__(self):
        return f"{self.title_ar}"