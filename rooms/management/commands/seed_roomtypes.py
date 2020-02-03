from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    help = "This command seed roomtype."

    def handle(self, *args, **options):
        roomtypes = ["Hotel room", "Shared room", "Private room", "Entire place"]

        for roomtype in roomtypes:
            RoomType.objects.create(name=roomtype)
        self.stdout.write(self.style.SUCCESS(f"{len(roomtypes)} RoomTypes Created"))
