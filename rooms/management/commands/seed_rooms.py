import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command seed rooms."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="how many room you make?",
        )
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 10),
                "price": lambda x: random.randint(5000, 15000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        houserules = room_models.HouseRule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,15)}.jpeg",
                )

            for item in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.amenities.add(item)
            for item in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.facility.add(item)
            for item in houserules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    room.house_rule.add(item)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms Created"))
