from django.db import models

# Create your models here.
class EPLPlayer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    team = models.IntegerField(null=True)
    goals_scored = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    total_points = models.IntegerField(null=True)
    points_per_game = models.FloatField(null=True)
    selected_by_percent = models.FloatField(null=True)
    now_cost = models.IntegerField(null=True)
    minutes = models.IntegerField(null=True)

    