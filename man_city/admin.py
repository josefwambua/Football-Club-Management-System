from django.contrib import admin
from .models import FootballClub, CEO, Contributor, Coach, Player, Fan

# Define custom admin classes with list display
class FootballClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date', 'stadium')

class CEOAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'club')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'age', 'club')

class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'age', 'club')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'age', 'club')

class FanAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'club')

# Register your models with custom admin classes
admin.site.register(FootballClub, FootballClubAdmin)
admin.site.register(CEO, CEOAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Fan, FanAdmin)