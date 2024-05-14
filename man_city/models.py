from django.db import models

class FootballClub(models.Model):
    name = models.CharField(max_length=100)
    foundation_date = models.DateField()
    stadium = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_average_player_age(self):
        total_age = sum(player.age for player in self.players.all())
        if self.players.count() > 0:
            return total_age / self.players.count()
        else:
            return 0

    def get_coaches_count(self):
        return self.coaches.count()

    def get_ceo_name(self):
        if self.ceo:
            return self.ceo.name
        else:
            return "Unknown"

    def get_contributors_count(self):
        return self.contributors.count()

    def get_fans_count(self):
        return self.fans.count()

class CEO(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.OneToOneField(FootballClub, on_delete=models.CASCADE, related_name='ceo')

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name='contributors')

class Coach(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name='coaches')

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.IntegerField()
    club = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name='players')

class Fan(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    club = models.ForeignKey(FootballClub, on_delete=models.CASCADE, related_name='fans')