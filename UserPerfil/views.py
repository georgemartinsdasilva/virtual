from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserPerfil.models import UserProfile


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

args = UserProfile.objects.all()
@login_required(login_url="login/")
def home(request):
    return render(request,'home.html', {'dado': args})