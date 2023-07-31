from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, resolve, Resolver404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from accounts.forms import SignUpForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')

    else:
        return redirect('/')

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
