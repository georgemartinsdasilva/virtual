from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from UserPerfil.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('UserPerfil.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
]