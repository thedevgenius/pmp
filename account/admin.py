from django.contrib import admin
from .models import User, Team, TeamMember, Designation
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'email']

admin.site.register(User, UserAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Team, TeamAdmin)

admin.site.register(TeamMember)

admin.site.register(Designation)