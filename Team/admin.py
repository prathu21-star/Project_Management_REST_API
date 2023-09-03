import django
from django.contrib import admin
from Team.models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display= ['id', 'Teamname', 'description', 'creationtime', 'admin', 'display_members']

