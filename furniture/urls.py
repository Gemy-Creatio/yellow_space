
from django.urls import path
from furniture.views import (
WoodBlogDetailView ,
BlogList ,
BlogCatList



)

urlpatterns = [
    path('all/blog' , BlogList , name='blog-list'),
    path('blog/<int:pk>' , WoodBlogDetailView.as_view() , name='blog-detail'),
    path('category/blog/<int:pk>' , BlogCatList , name='blog-cat-detail'),


]
