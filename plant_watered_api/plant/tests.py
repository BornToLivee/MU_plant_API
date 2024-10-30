from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from plant.models import Plant


class PlantViewTestCase(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(
            name='Test Plant',
            species='Test Species',
            water_frequency_days=5,
            last_watered_date='2024-10-01'
        )
        self.url = reverse('plant-detail', args=[self.plant.id])

    def test_update_last_watered_date(self):
        data = {'last_watered_date': '2024-10-10'}
        response = self.client.put(self.url, data, content_type='application/json')
        self.plant.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.plant.last_watered_date, datetime.strptime('2024-10-10', '%Y-%m-%d').date())

    def test_update_invalid_last_watered_date(self):
        response = self.client.patch(self.url, {}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_future_update_last_watered_date(self):
        data = {'last_watered_date': '2027-10-10'}
        response = self.client.patch(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
