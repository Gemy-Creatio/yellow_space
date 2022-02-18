
from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name':'الأسم',
            'phone':'الهاتف',
            'email':'البريد الألكترونى',
            'address':'العنوان',

        }
