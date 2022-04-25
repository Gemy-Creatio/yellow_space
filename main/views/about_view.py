from django.views import View

from main.models import (
    AboutPage ,
    FAQ
)
from django.shortcuts import render


class AboutPageView(View):
    def get(self, request):
        about_content = AboutPage.get_solo()
        faqs = FAQ.objects.filter(is_show=True)
        return render(request, 'main/aboutpage/about.html', {"content": about_content , "faqs": faqs})


