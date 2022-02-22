from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

en_label_dict = {
        "lang" : "English", "ltitle" : "Admin Login", "lfhead1" : "Admin Login", "username" : "Username", "password" : "Password", "login" : "Login", "rtitle" : "Register Admin", "rhead1" : "Register Admin", 'signup' : 'SignUp'
}

fn_label_dict = {
    "lang" : "Finnish", "ltitle" : "Järjestelmänvalvojan kirjautuminen", "lfhead1" : "Järjestelmänvalvojan kirjautuminen", "username" : "Käyttäjätunnus", "password" : "Salasana", "login" : "Kirjaudu sisään", "rtitle" : "Rekisteröidy Admin", "rhead1" : "Rekisteröidy Admin", 'signup' : 'Kirjaudu'
}

def setLang(request):
    if request.COOKIES.get('language'):
        lang = request.COOKIES['language']
    else:
        lang = "en"

    if lang == "fn":
        label_dict = fn_label_dict
    else:
        label_dict = en_label_dict
    return label_dict

def register(request):
    label_dict = setLang(request)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists. Please Try Another.')
            else:
                obj = form.save(commit=True)
                obj.save()
                login(request, obj)
                return redirect('dashboard_url')
        else:
            messages.error(request, 'Invalid Registeration Form.')
    else:
        form = UserCreationForm()
    return render(request, r'adminUserApp\register.html', {"label" : label_dict, "form": form})

def login_user(request):
    """
    [
        login page rendered here.
        setLang function is used to set the language label dict to be used in template.
    ]

    Returns:
        [renders webpage]: [
            renders html page with context having the language label dict.
        ]
    """
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password = raw_password)
            if user is not None:
                login(request, user)
                label_dict =setLang(request)                
                return redirect('dashboard_url')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form = AuthenticationForm()
    label_dict = setLang(request)
    return render(request, r'adminUserApp\login.html', {"label": label_dict, 'form' : form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Your account logout succefully.')
    return redirect('dashboard_url')