from rest_framework import viewsets

from plant.models import Plant
from plant.serializers import PlantListSerializer, PlantCreateSerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PlantCreateSerializer
        return PlantListSerializer
