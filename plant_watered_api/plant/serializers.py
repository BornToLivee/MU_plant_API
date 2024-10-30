from rest_framework import serializers
from plant.models import Plant


class PlantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['id', 'name', 'species', 'water_frequency_days', 'last_watered_date']


class PlantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['name', 'species', 'water_frequency_days', 'last_watered_date']


class PlantUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ['last_watered_date']