from django.core.management.base import BaseCommand, CommandError
from aviata.models import Route

class Command(BaseCommand):
    def handle(self, *args, **options):
        routes = Route.objects.all()

        for route in routes:
            print(route.from_code, route.to_code)
