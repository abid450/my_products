from django import forms
from django.contrib.auth.models import User
from .models import Products_M
class product_contact(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'floatingInput', 'placeholder': 'Name'}))
    email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'email'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'floatingInput', 'placeholder': 'Phone Number'}))
    title = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id':'floatingInput', 'col':32, 'row':4,  'placeholder': 'Title'}))
    
    class Meta:
        model = Products_M
        fields = ['name','email_address','phone_number', 'title']

    def clean_email_address(self):
        email_address = self.cleaned_data.get('email_address')

        if Products_M.objects.filter(email_address__iexact=email_address).exists():
            raise forms.ValidationError('This Email Already Exist.')
        return email_address
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if Products_M.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('This Phone Number Already Exist.')
        
        elif len(phone_number) != 11:
            raise forms.ValidationError('Please Enter your Correct Number.')
        return phone_number