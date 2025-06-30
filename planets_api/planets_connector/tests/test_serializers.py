from django.test import TestCase
from planets_connector.models import Planet
from planets_connector.serializers import PlanetSerializer


class PlanetSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            "name": "Super Earth",
            "mass": 8000000000,
            "terrains": "Rocks and stones",
            "climate": "Very dry"
        }
        serializer = PlanetSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], "Super Earth")

    def test_invalid_serializer_missing_fields(self):
        data = {
            "mass": 8000000000,
            "terrains": "Rocks and stones",
            "climate": "Very dry"
        }
        serializer = PlanetSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)
