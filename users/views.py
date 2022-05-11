from email import message
from django.shortcuts import redirect, render

from django.contrib.auth import get_user_model, login, logout
from django.db import transaction
from django.contrib import messages
from users.models import *
from users.forms import *

# Create your views here.
User = get_user_model()


def register_user(request):
    if request.method == 'POST' and 'register' in request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = User(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone = form.cleaned_data['phone'],
                    email=form.cleaned_data['email'],
                )
                user.set_password(form.cleaned_data['password'])
                user.save()
            return redirect('login')
            # print('Qeydiyyat uğurla tamamlandı.')
        print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            login(request, user)
            return redirect('goldapp:index')
        print(form.errors)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')