"""
User's views
"""
from django.shortcuts import render, redirect
from django.contrib import messages

from user.forms import RegisterForm


def register(request):
    """Register a new user in the system."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            messages.success(request, 'User created successful.')
            return redirect('user:login')

        else:
            for error in form.errors.values():
                messages.error(request, error)

    form = RegisterForm()
    context = {'form': form}

    return render(request, 'user/register.html', context)


def login(request):
    """Authenticate and login registered users."""
    return render(request, 'user/login.html')