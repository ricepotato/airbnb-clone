from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command seend amenities."

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
