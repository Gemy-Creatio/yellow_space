from django.contrib import admin
from ..models.blogpage_model import Blogpage
from solo.admin import SingletonModelAdmin


@admin.register(Blogpage)
class BlogPageAdmin(SingletonModelAdmin):
    list_display = ('__str__',)