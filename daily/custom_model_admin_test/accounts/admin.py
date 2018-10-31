from django.contrib import admin
from .models import CustomUser, Team

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'nick_name', 'level', 'team_in')

class TeamInline(admin.TabularInline):
    model = CustomUser.team_in.through

class TeamAdmin(admin.ModelAdmin):
    inlines = [
            TeamInline,
            ]

admin.site.register(CustomUser, UserAdmin,)
admin.site.register(Team, TeamAdmin)
