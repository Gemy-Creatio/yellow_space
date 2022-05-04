from django.views.generic import DetailView
from furniture.models.furniture_model import Furniture
from ..models import ProjectTypes
from main.models.projectspage_model import Projectspage

class ProjectDetailView(DetailView):
    model = Furniture
    template_name = 'projects/detail/detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args,**kwargs)
        context['cats'] = ProjectTypes.objects.all()
        context['content'] = Projectspage.get_solo()
        return context