from django.shortcuts import reverse
from django.views.generic import CreateView
from main.forms import ContactForm
from main.models import Contact

class ContactView(CreateView):
    form_class = ContactForm
    model = Contact
    template_name = 'main/contactpage/contact.html'
    def get_success_url(self):
        return reverse('home-page')