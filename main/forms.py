from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Customer_registration


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'message', 'email']


class Customer_registrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    first_name= forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']   # default form in django user registrration creation
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer_registration
        fields = ['first_name', 'last_name', 'email', 'city', 'phone_number', 'profile_picture']