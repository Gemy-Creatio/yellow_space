from django.views import View

from main.models import Homepage
from django.shortcuts import render


class HomePageView(View):
    def get(self, request):
        home_content = Homepage.get_solo()
        return render(request, 'main/homepage/homepage.html', {"content": home_content})
