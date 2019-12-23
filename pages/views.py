from django.shortcuts import render,redirect
from accounts.models import User
from accounts.forms import UserForm,LoginForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from pages.models import LetterModel,SecretSanta
from pages.forms import LetterForm
import random

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
    santainfo = {}
    person = request.user.get_username()
    santa = request.user.email
    players = SecretSanta.objects.all()
    for player in players:
        if player.santa == santa:
            santainfo['player'] = player.player
            santainfo['letter'] = player.text

    return render(request, 'homepage.html', {'person':person,"santainfo":santainfo})


@login_required(login_url="login page")
def logoutView(request):
    if request.GET:
        logout(request)
        return redirect('login page')

    return render(request, 'homepage.html', {})

def secretSantaView(request):

    base = {}
    array = []
    newArray = []
    arrayPerson = []
    arraySanta = []
    resultDict = {}

    def addPerson(name, surname, email):
        base[len(base) + 1] = [name, surname, email]


    def Result():
        for id, personInfo in base.items():
            array.append(personInfo[2])

        random.shuffle(array)

        while array:
            if (len(array) % 2 == 0):
                people = random.sample(array, 2)
                newArray.append(people)
                array.remove(people[0])
                array.remove(people[1])

            else:
                array.append("დაელოდეთ ახალ მოთამაშეს")
                people = random.sample(array, 2)
                newArray.append(people)
                array.remove(people[0])
                array.remove(people[1])

            for couple in newArray:
                resultDict[couple[0]] = couple[1]
                arrayPerson.append(couple[0])
                arraySanta.append(couple[1])

            while arrayPerson:
                person = random.choice(arrayPerson)
                santa = random.choice(arraySanta)
                resultDict[santa] = person
                arrayPerson.remove(person)
                arraySanta.remove(santa)

        return resultDict

    players = User.objects.all()
    letters = LetterModel.objects.all()

    letterDict = {}

    for lett in letters:
        letterDict[lett.author.email] = lett.letter


    for player in players:
        addPerson(player.name, player.surname, player.email)

    Result()

    SecretSanta.objects.all().delete()

    for santa,gamer in resultDict.items():
        try:
            SecretSanta(santa=santa, player=gamer, text=letterDict[gamer]).save()
        except (KeyError):
            continue



    return render(request, 'homepage.html', {"resultbase":resultDict,"letterDict":letterDict})





