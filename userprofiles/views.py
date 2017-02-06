from django.contrib.auth import login as login_django
from django.shortcuts import render

from userprofiles.forms import EmailAuthenticationForm
from .forms import UserCreationEmailForm


def signup(request):
    template = 'signup.html'
    form = UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }

    return render(request, template, context)


def login(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login_django(request, form.get_user())

    return render(request, 'signin.html', {'form': form})