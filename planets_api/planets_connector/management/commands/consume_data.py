import requests
from planets_connector.models import Planet
from django.core.management.base import BaseCommand

URL = "https://swapi-graphql.netlify.app/graphql?query=query+Query+%7BallPlanets%7Bplanets%7Bname+population+terrains+climates%7D%7D%7D"


class Command(BaseCommand):
    help = "Consumes the third party planets API and inserts the data into the DB"

    def handle(self, *args, **options):
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            planets = data["data"]["allPlanets"]["planets"]

            for planet in planets:
                Planet.objects.get_or_create(
                    name=planet["name"],
                    population=planet["population"],
                    terrains=planet["terrains"],
                    climates=planet["climates"]
                )

            self.stdout.write(self.style.SUCCESS(
                "Planets data successfully saved!")
            )

        else:
            self.stdout.write(self.style.ERROR(
                f"Error: {response.status_code}")
            )
