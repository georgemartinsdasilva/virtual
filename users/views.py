from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from users.models import UserProfile
import re

def user_login(request):
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                   
                    return render(request, "CscSig/index.html", {'Gestor' : UserProfile.objects.filter(user=user).values('Gestor')})
                else:
                    return HttpResponse("user is not active")
            else:
                return HttpResponse("Invalid Login")
        else:
            return HttpResponse("Not valid form")
    else:
        user_form = UserLoginForm()
        return render(request, "users/login.html", {"user_form": user_form})





