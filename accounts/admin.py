from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('role', 'team',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {'fields': ('first_name','last_name','role', 'team',)}),
    )
    list_display = ['username', 'email', 'last_name','first_name','role', 'team',]

admin.site.register(CustomUser, CustomUserAdmin)



