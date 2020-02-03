from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command tells that she loves me."

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you wnat me to tell you that I love you?",
        )
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        times = options.get("times")
        for _ in range(0, int(times)):
            # print("i love you")
            self.stdout.write(self.style.SUCCESS("I love you"))
            self.stdout.write(self.style.ERROR("I love you"))
            self.stdout.write(self.style.WARNING("I love you"))
        # print(args, options)

