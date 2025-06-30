from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from planets_connector.models import Planet


class PlanetAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.planet = Planet.objects.create(
            name="Super Earth",
            population=8000000000,
            terrains="Rocks and stones",
            climates="Dry"
        )
        self.list_url = reverse("planet-list")
        self.detail_url = reverse('planet-detail', args=[self.planet.id])

    def test_list_planets(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_planet(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Super Earth")

    def test_create_planet(self):
        data = {
            "name": "Widows Harbor",
            "population": 8000000000,
            "terrains": "Mountais",
            "climates": "Wet"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Planet.objects.count(), 2)

    def test_create_planet_invalid(self):
        data = {
            "population": 8000000000,
            "terrains": "Plains",
            "climates": "Cold"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_planet(self):
        data = {
            "name": "Updated Widows Harbor",
            "climates": "Very Wet"
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.planet.refresh_from_db()
        self.assertEqual(self.planet.name, "Updated Widows Harbor")
        self.assertEqual(self.planet.climates, "Very Wet")

    def test_delete_planet(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Planet.objects.count(), 0)

    def test_retrieve_nonexistent_planet(self):
        endpoit = reverse('planet-detail', args=[9999])
        response = self.client.get(endpoit)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_planet_missing_fields(self):
        response = self.client.post(self.list_url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
