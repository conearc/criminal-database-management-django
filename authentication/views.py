from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def LoginView(request):
    f = LoginForm()
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(user)
            else:
                messages.error(request, 'The form is invalid.')
    return render(request, 'login.html', {'form': f})


def login2(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return redirect('home')
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login1.html', context)


def RegisterView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="register.html",
                          context={"form": form})

    form = SignUpForm
    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


def HomePageView(request):
    if request.user.is_staff:
        return render(request, 'home.html')
    return render(request, 'home1.html')


def LoginHomePageView(request):
    return render(request, 'homepage.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")
