from django.views.generic import DetailView
from furniture.models.wood_information_model import WoodInformation
from furniture.models.category_model import Category
from main.models.blogpage_model import Blogpage
class WoodBlogDetailView(DetailView):
    model = WoodInformation
    template_name = 'furniture/blog/detail/detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(WoodBlogDetailView, self).get_context_data(*args,**kwargs)
        context['cats'] = Category.objects.all()
        context['content'] = Blogpage.get_solo()
        return context