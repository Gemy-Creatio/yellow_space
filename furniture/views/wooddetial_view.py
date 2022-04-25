from django.views.generic import DetailView
from furniture.models.wood_information_model import WoodInformation


class WoodBlogDetailView(DetailView):
    model = WoodInformation
    template_name = 'furniture/blog/detail/detail.html'