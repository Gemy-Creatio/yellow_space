from furniture.models.furniture_model import  Furniture
from django.core.paginator import Paginator
from django.shortcuts import render
from main.models.projectspage_model import Projectspage
from ..models import ProjectTypes


def ProjectList(request):
    cats = ProjectTypes.objects.all()
    projects = Furniture.objects.all().order_by('-date_added')
    paginator = Paginator(projects, 8)
    proj_content = Projectspage.get_solo()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects/list/projectlist.html', context={"projects": page_obj , "cats":cats , "content":proj_content})