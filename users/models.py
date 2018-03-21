from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	Setor = models.CharField(max_length=30)
	Gestor = models.CharField(max_length=30)
	funcao = models.CharField(max_length=30)

