from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command tells that she loves me."

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you wnat me to tell you that I love you?",
        )
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        amenities = [
            "Microwave",
            "Outdoor pool",
            "Outdoor tennis",
            "Shopping Mall",
            "Restaurant",
            "Shower",
            "Smake detector",
            "Sofa",
            "Sterao",
            "Swimming pool",
            "Tolilet",
            "Towels",
            "TV",
        ]

        for name in amenities:
            Amenity.objects.create(name=name)
        self.stdout.write(self.style.SUCCESS("Amenities Created"))
