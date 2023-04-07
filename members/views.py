from django.db import connection
from django.shortcuts import render, redirect
from .models import Member
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login


def select_location(request):
    return render(request, 'members/select_location.html', {})


def login(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']

            user = authenticate(username=user_name, password=user_password)

            if user is not None:
                print("Auth succeeded")
                auth_login(request, user)
                return redirect('select_location')
            else:
                context['form'] = form
                context['error_message'] = 'Username/Password is incorrect'
                print("Auth failed")
        else:
            context['form'] = form
            context['error_message'] = 'Please correct the errors below.'
            print("Form is invalid")
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, 'members/login.html', context)


def add_member(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        other_name = request.POST.get('other_name')
        primary_phone_number = request.POST.get('primary_phone_number')
        whatsapp_phone_number = request.POST.get('whatsapp_phone_number')
        place_of_residence = request.POST.get('place_of_residence')
        work_place = request.POST.get('work_place')
        date_of_birth = request.POST.get('date_of_birth')
        missional_community = request.POST.get('missional_community')
        profession = request.POST.get('profession')

        m = Member(Surname=surname, Other_name=other_name, Primary_phone_number=primary_phone_number,
                    Whatsapp_phone_number=whatsapp_phone_number, Place_of_residence=place_of_residence,
                    Work_place=work_place, Date_of_birth=date_of_birth, Missional_Community=missional_community)
        m.save()

        return redirect('home')
        
    return render(request, 'members/add_member.html', {})


def manage_database(request):
    table_name = 'members_member'
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
        columns = [col[0] for col in cursor.description]
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
    return render(request, 'members/manage_database.html', {'columns': columns, 'rows': rows})



def home(request):
    return render(request, 'members/home.html', {})