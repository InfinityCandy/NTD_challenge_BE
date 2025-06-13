from rest_framework.viewsets import ModelViewSet
from planets_connector.models import Planet
from planets_connector.serializers import PlanetSerializer


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
