from django.urls import path
from main.views import (
    HomePageView ,
    ContactView ,
    AboutPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('contact', ContactView.as_view(), name='contact-page'),
    path('about', AboutPageView.as_view(), name='about-page')

]
