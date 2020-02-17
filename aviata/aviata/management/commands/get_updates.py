from django.core.management.base import BaseCommand, CommandError
from aviata.models import Route
import datetime, requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Flight.objects.clear()
        DAYS = 30
        DATA_URL = 'https://api.skypicker.com/flights?'
        CHECK_URL = 'https://booking-api.skypicker.com/api/v0.1/check_flights'
        routes = Route.objects.all()
        cur_date = datetime.datetime.today()
        dates = [cur_date + datetime.timedelta(days=x) for x in range(DAYS)]
        
        for date in dates:
            str_date = date.strftime("%d/%m/%Y")
            
            params = {
                'fly_from': 'ALA',
                'fly_to': 'TSE',
                'partner': 'picky',
                'date_from': str_date,
                'date_to': str_date,
            }
            data = requests.get(url=DATA_URL, params=params).json()
            print(data)
        
