from django import forms
from django.contrib.auth.models import User
from shoppingCart.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class userLogin(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': ' USERNAME'}) )
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder': ' PASSWORD'}))


class userSignup(forms.ModelForm):
    password = forms.CharField(max_length=50, widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
    # first_name = forms.CharField(max_length=50, label="First Name")
    # last_name = forms.CharField(max_length=50, label="Last Name")
    # username = forms.CharField(max_length=50, label="Desired Username")
    # password = forms.CharField(max_length=50, label="Password")
    # email = forms.EmailField( label="Email")

class userSignup_profile(forms.ModelForm):
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'PASSWORD'}))
    #phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'pincode')
    # phone = forms.CharField(max_length=10, label="Mobile No. : +91 ")
    # address = forms.CharField(max_length=200, label="Address", widget=forms.Textarea)
    # pincode = forms.IntegerField()
