from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','date_joined','last_login','is_active')
    # como apareceran los campos en las tablas del administrador


    list_display_link = ('email','first_name','last_name','username')
    # cuando le demos click a estos campos nos llevara a su detalle del usuario

    readonly_fields = ('last_login','date_joined')
    # para ponerle campos solo de lectura es decir que solo se pueden leer y no editar

    ordering = ('-date_joined',)
    # ordenamiento

    filter_horizontal=()
    list_filter = ()
    fieldsets = ()






# Register your models here.
admin.site.register(Account, AccountAdmin)
