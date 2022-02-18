
from django.urls import path
from furniture.views.woodblog_view import BlogList

urlpatterns = [
    path('all/blog' , BlogList , name='blog-list')

]
