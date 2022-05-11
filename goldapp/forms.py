from django import forms

from .models import ContactUs
from django.forms import widgets

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'email' : widgets.EmailInput(attrs={'class': 'form-control required-entry validate-email','placeholder': 'E-mail ünvanınız'} ),
            'telephone': widgets.TextInput(attrs={'class': 'form-control', 'value': '+994'}),
            'message': widgets.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 30, 'style': 'line-height: 1.5rem', 'placeholder': 'Müraciətiniz'} ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print(first_name)
        if len(first_name) < 2:
            raise forms.ValidationError("Adınızı düzgün daxil edin.")
        return first_name

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        print(telephone)
        if len(telephone) < 10 or len(telephone) > 20:
            raise forms.ValidationError("Telefon nömrənizi düzgün daxil edin.")
        return telephone
        