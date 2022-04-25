from django.db import models
from ckeditor.fields import RichTextField


class FAQ(models.Model):
    question_ar = models.CharField(max_length=255, blank=True , null=True)
    question_en = models.CharField(max_length=255, blank=True , null=True)
    answer_ar = RichTextField(null=True)
    answer_en = RichTextField(null=True)
    is_show = models.BooleanField(null=True , blank=True , default=False)

    def __str__(self):
        return self.answer_ar
