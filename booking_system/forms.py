from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from booking_system.models import Customer,Accountant,User
from .widgets import XDSoftDateTimePickerInput

class CustomerSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email = email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        
        return user

class AccountantSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = User.objects.get(email = email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
       
        return user

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class AccountantForm(ModelForm):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
    class Meta:
        model = Accountant
        fields = ['gender','citizenship','country_residence','tax_regulation_specialty','hour_rate','date']
        exclude = ['user']
    