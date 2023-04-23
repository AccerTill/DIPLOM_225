from django.contrib import admin
from .models import Team

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    # поле только для чтения



admin.site.register(Team, TeamAdmin)


