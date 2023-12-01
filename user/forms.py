from django import forms
from user.models import User_Model, Address
from django.contrib.auth.forms import UserChangeForm

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'apartment_number', 'zip_code']

class UserProfileForm(UserChangeForm):
    address = AddressForm()

    class Meta:
        model = User_Model
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'username', 'password']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User_Model
        fields = ['first_name', 'last_name', 'date_of_birth',
                  'email', 'username', 'password',]


class AddressRegistrationForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'apartment_number', 'zip_code']
