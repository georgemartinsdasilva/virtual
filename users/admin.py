from django.contrib import admin
from users.models import UserProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ('user', 'Setor', 'Gestor', 'funcao')
	search_fields = ["user"]
admin.site.register(UserProfile, UserAdmin)
