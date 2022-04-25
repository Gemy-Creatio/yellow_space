
from django.views.generic import ListView
from furniture.models.wood_information_model import  WoodInformation
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from main.models.blogpage_model import Blogpage
from furniture.models.category_model import Category

def BlogList(request):
    cats = Category.objects.all()
    blog_content = Blogpage.get_solo()
    blogs = WoodInformation.objects.filter(is_ready=True).order_by('-publication_date')
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'furniture/blog/list/bloglist.html', context={"blogs": page_obj , "blog_content":blog_content , "cats":cats})
