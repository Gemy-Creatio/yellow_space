from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from solo.models import SingletonModel
from django.db import models
from django.templatetags.static import static


class Homepage(SingletonModel):
    homepage_background = models.ImageField(upload_to='backgrounds/', null=True)
    header_en = RichTextField(null=True , help_text="Intro Header [English]")
    subheader_en = models.CharField(null=True, blank=True, max_length=255 , help_text="Content in Intro [English]")
    btn_text_en = models.CharField(null=True, blank=True, max_length=255, help_text="Button Text in Intro [Arabic]")
    header_ar = RichTextField(null=True , help_text="Intro Header [Arabic]")
    subheader_ar = models.CharField(null=True, blank=True, max_length=255 , help_text="Content in Intro [Arabic]")
    btn_text_ar = models.CharField(null=True, blank=True, max_length=255 , help_text="button in Intro Text [Arabic]")
    btn_color = ColorField(help_text="Button Color in Intro")
    category_title_en = models.CharField(null=True, blank=True, max_length=255 , help_text="Category Tiltles for blogs [English]")
    category_description_en = RichTextField(null=True, help_text="Category Description for blogs [English]")
    furniture_title_en = models.CharField(null=True, blank=True, max_length=255)
    furniture_description_en = RichTextField(null=True)
    category_title_ar = models.CharField(null=True, blank=True, max_length=255, help_text="Category Tiltles for blogs [Arabic]")
    category_description_ar = RichTextField(null=True , help_text="Category Description for blogs [Arabic]")
    furniture_title_ar = models.CharField(null=True, blank=True, max_length=255)
    furniture_description_ar = RichTextField(null=True)
    mobile = models.CharField(max_length=20)
    other_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    address_en = RichTextField(null=True , help_text="Address [English]")
    address_ar = RichTextField(null=True , help_text="Address [Arabic]")
    why_us_title_en = models.CharField(null=True, blank=True, max_length=255, help_text="Why Us Tiltle [English]")
    why_us_description_en =  RichTextField(null=True , help_text="Why us Description [English]")
    why_us_title_ar = models.CharField(null=True, blank=True, max_length=255, help_text="Why Us Tiltle [Arabic]")
    why_us_description_ar =  RichTextField(null=True , help_text="Why us Description [Arabic]")
    first_reason_en = models.CharField(null=True, blank=True, max_length=255, help_text="First Reason [English]")
    first_reason_description_en =  RichTextField(null=True , help_text="First reason Description[English]")
    first_reason_ar = models.CharField(null=True, blank=True, max_length=255, help_text="First Reason [Arabic]")
    first_reason_description_ar =  RichTextField(null=True , help_text="First reason Description[Arabic]")
    second_reason_en = models.CharField(null=True, blank=True, max_length=255, help_text="Second Reason [English]")
    second_reason_description_en =  RichTextField(null=True , help_text="Second reason Description[English]")
    second_reason_ar = models.CharField(null=True, blank=True, max_length=255, help_text="Second Reason [Arabic]")
    second_reason_description_ar =  RichTextField(null=True , help_text="Second reason Description[Arabic]")
    third_reason_en = models.CharField(null=True, blank=True, max_length=255, help_text="Third Reason [English]")
    third_reason_description_en =  RichTextField(null=True , help_text="Third reason Description[English]")
    third_reason_ar = models.CharField(null=True, blank=True, max_length=255, help_text="Third Reason [Arabic]")
    third_reason_description_ar =  RichTextField(null=True , help_text="Third reason Description[Arabic]")
    @property
    def image_url(self):
        if self.homepage_background and hasattr(self.homepage_background, 'url'):
             return self.homepage_background.url
        else:
            return static("assets/img/home1.jpeg")
    class Meta(SingletonModel.Meta):
        pass

    def __str__(self):
        return f"{self.email}"
    def faqs(self):
        from .faq_model import FAQ
        return FAQ.objects.order_by('-pk').filter(is_show=True)[:4]
    def categories(self):
        from projects.models import ProjectTypes
        return ProjectTypes.objects.all()
    def staff_members(self):
        from .staff_model import Staff
        return Staff.objects.all()
    def blogs(self):
        from furniture.models.wood_information_model import WoodInformation
        return WoodInformation.objects.order_by('-publication_date').filter(is_ready=True)[:4]
    def furniture(self):
        from furniture.models.furniture_model import Furniture
        return Furniture.objects.order_by('-offer_value').filter(is_for_offer=True)[:4]
