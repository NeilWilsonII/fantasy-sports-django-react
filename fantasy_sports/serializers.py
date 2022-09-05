from rest_framework import serializers
from .models import EPLPlayer

class EPLSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPLPlayer
        fields = ('first_name', 'last_name', 'team', 'goals_scored', 'assists', 'total_points',\
            'points_per_game', 'selected_by_percent', 'now_cost', 'minutes')



