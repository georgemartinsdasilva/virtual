from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

