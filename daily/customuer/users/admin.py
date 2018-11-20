from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Team


class TeamInline(admin.TabularInline):
    model = Team

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'nick_name', 'team']
    fields = ['nick_name', 'team', 'password']
    inline = [TeamInline,]

class TeamAdmin(admin.ModelAdmin):
    model = Team
    fields = ['team_name', 'team_deps']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Team, TeamAdmin)
