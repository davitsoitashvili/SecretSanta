from django.shortcuts import render,redirect
from accounts.models import User
from accounts.forms import UserForm,LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from pages.models import LetterModel
from pages.forms import LetterForm

def registerView(request):
    form = UserForm()
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("letter page")

    return render(request,'register.html',{'registerform':form})

def loginView(request):
    form = LoginForm()

    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home page")


    return render(request, 'login.html', {"loginform":form})


@login_required(login_url="login page")
def letterView(request):
    form = LetterForm()
    user = request.user

    if request.POST:
        form = LetterForm(request.POST)
        if form.is_valid():
            LetterModel(author=user, letter=form.cleaned_data['letter']).save()
            return redirect("home page")


    return render(request, 'letter.html', {'letterform':form})

@login_required(login_url="login page")
def homepageView(request):
    person = request.user.get_username()
    return render(request, 'homepage.html', {'person':person})


@login_required(login_url="login page")
def logoutView(request):
    if request.GET:
        logout(request)
        return redirect('login page')

    return render(request, 'homepage.html', {})


