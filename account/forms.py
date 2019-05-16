from account.models import Profile
from django.contrib.auth.models import User
from django import forms
from registration.forms import RegistrationFormUniqueEmail

'''class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input',}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-input',}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-input', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']'''


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input',}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    phone = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'form-input',}))

    class Meta:
        model = Profile
        fields = ['image', 'phone']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].label = False


class UserRegisterForm(RegistrationFormUniqueEmail):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input',}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    company = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input',}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input',}))
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-input', }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
