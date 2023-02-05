from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pennapps.models import Applicant, Application


@login_required()
def index(request):
    return render(request, 'pennapps/index.html')


@login_required()
def application(request):
    return render(request, 'pennapps/application.html')


def login(request):
    return render(request, 'pennapps/login.html')


def signup(request):
    return render(request, 'pennapps/signup.html')


def createUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        password = request.POST['password']

        user = Applicant.objects.create_user(username=username, password=password, email=email,
                                             firstName=firstName, lastName=lastName)

        user.save()
        messages.success(request, 'Account created.')
        return redirect('/')

    else:
        return render(request, 'signup.html')


def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('/index/')
        else:
            messages.error(request, 'Invalid login')
            return redirect('/login/')

    else:
        return render(request, 'login.html')


def signOut(request):
    auth.logout(request)
    messages.success(request, 'Signed out.')
    return redirect('/')


def submitApplication(request):
    if request.method == 'POST':
        school = request.POST['school']
        year = request.POST['year']
        major = request.POST['major']
        phone_number = request.POST['phone_number']
        birthday = request.POST['birthday']
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        first_hackathon = request.POST['first_hackathon']
        team_member_1 = request.POST['team_member_1']
        team_member_2 = request.POST['team_member_2']
        team_member_3 = request.POST['team_member_3']
        applicant = request.user


        app = Application(school=school, year=year, major=major, phone_number=phone_number, birthday=birthday,
                          q1=q1, q2=q2, first_hackathon=first_hackathon, team_member_1=team_member_1,
                          team_member_2=team_member_2, team_member_3=team_member_3, applicant=applicant,
                          status="PROC"
                          )

        app.save()

        messages.success(request, 'Application saved.')
        return redirect('/index/')

    else:
        return render(request, 'application.html')
