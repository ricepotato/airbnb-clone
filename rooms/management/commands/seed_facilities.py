from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command seend facilities."

    def handle(self, *args, **options):
        facilities = [
            "Private enterance",
            "Paid parking on premeises",
            "Paid parking off premeises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for name in facilities:
            Facility.objects.create(name=name)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created"))
