from Team.models import Team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'Teamname', 'description', 'creationtime', 'admin', 'members']

class TeamGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['Teamname', 'description', 'creationtime', 'admin']

class TeamPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'Teamname', 'description', 'creationtime', 'admin']