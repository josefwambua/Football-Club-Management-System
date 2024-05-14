from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FootballClub, CEO, Contributor, Coach, Player, Fan

def home(request):
    # Fetch data from the models
    football_clubs = FootballClub.objects.all()
    ceos = CEO.objects.all()
    contributors = Contributor.objects.all()
    coaches = Coach.objects.all()
    players = Player.objects.all()
    fans = Fan.objects.all()

    # Pass data to the template
    return render(request, 'home.html', {
        'football_clubs': football_clubs,
        'ceos': ceos,
        'contributors': contributors,
        'coaches': coaches,
        'players': players,
        'fans': fans,
    })