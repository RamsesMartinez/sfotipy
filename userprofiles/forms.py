from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationEmailForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe el email")
        return email


class EmailAuthenticationForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        user_or_email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email_or_username=user_or_email, password=password)

        if self.user_cache is None:
            raise forms.ValidationError('Usuario Incorrecto')
        elif not self.user_cache.is_active:
            raise forms.ValidationError('Usuario inactivo')
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
