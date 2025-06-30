import logging
from requests.exceptions import RequestException, Timeout
import requests
from planets_connector.models import Planet
from django.core.management.base import BaseCommand

URL = "https://swapi-graphql.netlify.app/graphql?query=query+Query+%7BallPlanets%7Bplanets%7Bname+population+terrains+climates%7D%7D%7D"


class Command(BaseCommand):
    help = "Consumes the third party planets API and inserts the data into the DB"

    def handle(self, *args, **options):
        try:
            response = requests.get(URL, timeout=10)
            response.raise_for_status()

        except Timeout:
            self.stderr.write(self.style.ERROR("Request timed out."))
            return

        except RequestException as e:
            self.stderr.write(self.style.ERROR(f"Request failed: {str(e)}"))
            return

        try:
            data = response.json()
            planets = data.get("data", {}).get(
                "allPlanets", {}).get("planets", [])

            if not planets:
                raise ValueError("No planets found in response.")

            for planet in planets:
                try:
                    name = planet["name"]

                    if not name:
                        raise ValueError(
                            "Missing 'name' field in planet data.")

                    Planet.objects.get_or_create(
                        name=name,
                        population=planet["population"],
                        terrains=planet["terrains"],
                        climates=planet["climates"]

                    )

                except (KeyError, TypeError, ValueError) as e:
                    self.stderr.write(self.style.WARNING(
                        f"Skipping invalid planet data: {planet}. Reason: {e}"
                    ))

            self.stdout.write(
                self.style.SUCCESS(
                    f"{len(planets)} planet(s) processed successfully."
                )
            )

        except (ValueError, KeyError, TypeError) as e:
            self.stderr.write(
                self.style.ERROR(
                    f"Failed to parse response JSON. Error: {str(e)}"
                )
            )
