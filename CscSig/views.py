from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.conf.urls import url, include


def index(request):
    return render(request, "CscSig/index.html")