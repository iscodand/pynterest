from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from users.forms import RegisterForm, LoginForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


# TO-DO: fix register user (is not registering correctly)
# TO-DO: add error messages (is not registering correctly)

def register(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get("password"))
            new_user.save()
            messages.success(request, "User registered successfully!")
            return redirect('login')

        else:
            for value in form.errors.values():
                messages.error(request, f'{value}')

    form = RegisterForm()
    context = {'form': form}

    return render(request, 'users/register.html', context)


# TO-DO: fix authentication

def login(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        
            user = auth.authenticate(request, username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            
            else:
                messages.error(request, 'Incorrect user or password.')
                return redirect('login')

    context = {'form': form}

    return render(request, 'users/login.html', context)


def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect('login')


@login_required(login_url='users/login')
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/user.html')
