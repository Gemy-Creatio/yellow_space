
from django.urls import path
from furniture.views import (
WoodBlogDetailView ,
BlogList
)

urlpatterns = [
    path('all/blog' , BlogList , name='blog-list'),
    path('blog/<int:pk>' , WoodBlogDetailView.as_view() , name='blog-detail'),


]
