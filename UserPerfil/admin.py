from django.contrib import admin
from UserPerfil.models import UserProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'Setor', 'Gestor', 'funcao', 'image')
	search_fields = ["user"]
admin.site.register(UserProfile, UserAdmin)