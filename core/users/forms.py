from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-input', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistartionForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'Last ame'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'example@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-input', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-input', 'placeholder':'Re-enter Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class UserProfile(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'Last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'login-input', 'placeholder':'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'login-input', 'placeholder':'example@gmail.com'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'image-field'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'image']

        # widgets = {

        #     'first_name': forms.TextInput(attrs={'class':'name-input'}, ),
        #     'last_name': forms.TextInput(attrs={'class':'name-input'}, ),
        #     'username': forms.TextInput(attrs={'class':'name-input'}, ),
        #     'email': forms.TextInput(attrs={'class':'name-input'}, ),
            
        # }