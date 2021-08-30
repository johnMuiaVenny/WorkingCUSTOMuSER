from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('first_name', 'last_name', 'username', 'email',)
    list_filter = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff')
    ordering = ('-pk',)
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'email', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields':('first_name', 'last_name', 'username', 'email', 'user_type')}),
        ('Permissions', {'fields':('is_active', 'is_staff')}),
        ('Personal', {'fields':('about',)})
    )

    add_fieldsets = (
        (None, {'classes':('wide'), 'fields':('username', 'email', 'password1', 'password2')}),
    )

admin.site.register(NEWUSER, UserAdminConfig)
admin.site.register(TEACHER)
admin.site.register(STUDENT)
admin.site.register(PARENT)
admin.site.site_header = 'JOHN MUIA VENN'
