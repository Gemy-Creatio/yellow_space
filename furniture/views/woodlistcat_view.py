
from furniture.models.wood_information_model import WoodInformation
from furniture.models.category_model import Category
from main.models import Blogpage
from django.core.paginator import Paginator
from django.shortcuts import render

def BlogCatList(request , pk ):
    cat = Category.objects.get(pk=pk)
    blog_content = Blogpage.get_solo()
    blogs = WoodInformation.objects.filter(is_ready=True , category = cat).order_by('-publication_date')
    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'furniture/blog/blogcatlist/list.html', context={"object_list": page_obj , "content":blog_content , "cat":cat})