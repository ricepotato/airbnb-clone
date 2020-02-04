from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):
    help = "This command seend house rules."

    def handle(self, *args, **options):
        houserules = [
            "No Smoking",
            "No loud noise, music, or parties",
            "Not suitable for pets",
            "Smoking allowd on Balcony",
            "Please Remove Shoes/ Boots on entry",
            "Only One Parking Space provided",
            "Please be respectful after 10pm",
            "No Parties or events",
        ]

        for name in houserules:
            HouseRule.objects.create(name=name)
        self.stdout.write(self.style.SUCCESS(f"{len(houserules)} Houserules Created"))
