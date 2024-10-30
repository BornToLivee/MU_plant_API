from datetime import datetime

from rest_framework import viewsets,status
from rest_framework.response import Response

from plant.models import Plant
from plant.serializers import (
    PlantUpdateSerializer, 
    PlantListSerializer, 
    PlantCreateSerializer
)


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PlantCreateSerializer
        if self.action == 'update':
            return PlantUpdateSerializer
        return PlantListSerializer
    
    def update(self, request, *args, **kwargs):
        plant = self.get_object()
        last_watered_date = request.data.get('last_watered_date')

        if not last_watered_date:
            return Response({"detail": "Last watered date is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            last_watered_date = datetime.strptime(last_watered_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"detail": "Invalid date format, expected YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        if last_watered_date > datetime.now().date():
            return Response({"detail": "Last watered date cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)

        plant.last_watered_date = last_watered_date
        plant.save()

        return Response({"detail": "Last watered date updated successfully."}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
