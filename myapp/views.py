from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q


# Create your views here.

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="user":
                    user = User_registration.objects.get(email=email)
                    request.session["email"] = email
                    request.session["id"] = user.id
                    return redirect('/user_home')
                
                elif user.usertype=="staff":
                    user = Staff_registration.objects.get(email=email)
                    if user.approvel:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/staff_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')


    return render(request,"login.html")

def user_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        usertype=request.POST['usertype']
        email=request.POST['email']
        password=request.POST['password']
        id_card=request.FILES['id_card']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="user")
        log.save()

        regi=User_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            usertype=usertype,
            id_card=id_card,
            email=email,
            profile_picture=profile_picture,
            login_id=log
        )
        regi.save()
        messages.info(request,"Registration successful,You can login now")

    return render(request,"user_registration.html")

def staff_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        id_card=request.FILES['id_card']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="staff")
        log.save()

        regi=Staff_registration.objects.create(
            name=name,
            address=address,
            contact=contact,
            email=email,
            id_card=id_card,
            profile_picture=profile_picture,
            login_id=log
        )
        regi.save()
        messages.info(request,"Registration successful,Wait admin approvel")

    return render(request,"staff_registration.html")




####################### ADMIN ############################

def admin_home(request):

    return render(request,"admin/admin_home.html")

####################### STAFF ############################
####################### USER ############################
