from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TeamForm
from .models import Team
from django.utils import timezone

# только для зарегистрированных пользователей.
from django.contrib.auth.decorators import login_required


# Create your views here.



def home(request):
    return render(request, 'team/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'team/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentteam')

            except IntegrityError:
                return render(request, 'team/signupuser.html',
                              {'form': UserCreationForm(),
                               'error':'Такое имя пользователя уже '
                                       'существует. Задайте новое.'})

        else:
            return render(request, 'team/signupuser.html',
                          {'form': UserCreationForm(),
                           'error':'Пароли не совпадают.'})



def loginuser(request):
    if request.method == "GET":
        return render(request, 'team/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        # если пользователя не существует
        if user is None:
            return render(request, 'team/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




# -----ФОРМА ОТПРАВЛЯЕТСЯ МЕТОДОМ POST !!!!
@login_required
def currentteam(request):
    teams = Team.objects.filter(user = request.user, date_completed__isnull =True)
    return render(request, 'team/currentteam.html', {'teams': teams})




# for user  -----------
@login_required
def createteam(request):
    if request.method == 'GET':
        return render(request, 'team/createteam.html', {'form': TeamForm()})
    else:
        try:
            form = TeamForm(request.POST)
            new_team = form.save(commit=False)
            new_team.user = request.user
            new_team.save()
            return redirect('currentteam')
        except ValueError:
            return render(request, 'team/createteam.html',
                          {'form': TeamForm(), 'error': 'Переданы неверные данные.'
                                                        ' Попробуйте еще раз.'})

@login_required
def viewteam(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == "GET":
        form = TeamForm(instance = team)
        return render(request, 'team/viewteam.html', {'team': team, 'form': form})
    else:
        try:
            form = TeamForm(request.POST, instance = team)
            form.save()
            return redirect('currentteam')
        except ValueError:
            return render(request, 'team/viewteam.html',
                          {'team': team, 'form': form, 'error': 'Неверные данные'})



@login_required
def completeteam(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk, user=request.user)
    if request.method == 'POST':
        team.date_completed = timezone.now()
        team.save()
        return redirect('currentteam')


@login_required
def deleteteam(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk, user=request.user)
    if request.method == 'POST':
        team.delete()
        return redirect('currentteam')


@login_required
def completedteam(request):
    teams = Team.objects.filter(user = request.user,
                                date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'team/completedteam.html', {'teams': teams})







