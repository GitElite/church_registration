from django.db import connection
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Member
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


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


def delete_rows(request):
    if request.method == 'POST':
        selected_rows = request.POST.getlist('row_checkbox')
        table_name = 'members_member'
        
        with connection.cursor() as cursor:
            for row_id in selected_rows:
                if row_id:
                    cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", [row_id])

        messages.success(request, f'Successfully deleted {len(selected_rows)} row(s).')
        return HttpResponseRedirect(reverse('manage_database'))
    else:
        return HttpResponseRedirect(reverse('manage_database'))

def home(request):
    return render(request, 'members/home.html', {})


def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    
    if request.method == 'POST':
        member.surname = request.POST['surname']
        member.other_name = request.POST['other_name']
        member.primary_phone_number = request.POST['primary_phone_number']
        member.whatsapp_phone_number = request.POST['whatsapp_phone_number']
        member.place_of_residence = request.POST['place_of_residence']
        member.work_place = request.POST['work_place']
        member.date_of_birth = request.POST['date_of_birth']
        member.missional_community = request.POST['missional_community']
        member.save()

        return redirect('manage_database')
    
    context = {
        'member': member,
    }

    return render(request, 'members/update_member.html', context)


def update_rows(request):
    if request.method == 'POST':
        member_id = request.POST['member_id']
        return redirect('update_member', member_id=member_id)