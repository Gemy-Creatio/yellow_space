from django_extensions.db.fields import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ordered_model.models import OrderedModel
from django.templatetags.static import static
from django.urls import reverse
from django.db import models


class Category(OrderedModel):
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    slug = AutoSlugField(populate_from="name_en")
    picture = models.ImageField(upload_to="category/")
    image_webp = ImageSpecField(source="picture", format="WEBP", options={"quality": 100})
    image_thumb = ImageSpecField(
        source="picture",
        options={"quality": 90},
    )
    image_thumb_png = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(380, 380)],
        format="PNG",
        options={"quality": 90},
    )
    image_thumb_webp = ImageSpecField(
        source="picture",
        processors=[ResizeToFill(380, 380)],
        format="WEBP",
        options={"quality": 90},
    )

    def image_url(self):
        return self.picture.url if self.picture else static("images/category/category.png")

    def image_webp_url(self):
        return (
            self.image_webp.url
            if self.picture
            else static("images/category/category.png")
        )

    def image_thumb_webp_url(self):
        return (
            self.image_thumb_webp.url
            if self.picture
            else static("images/category/category.png")
        )

    def image_thumb_png_url(self):
        return (
            self.image_thumb_png.url
            if self.picture
            else static("images/category/category.png")
        )

    def image_thumbnail_url(self):
        return (
            self.image_thumb.url
            if self.picture
            else static("images/category/category.png")
        )

    def __str__(self):
        return f"category name is :{self.name_ar}"
