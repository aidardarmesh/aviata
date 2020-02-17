from django.core.management.base import BaseCommand, CommandError
from aviata.models import Route, Flight
import datetime, requests

class Command(BaseCommand):
    def valid_booking(self, token):
        CHECK_URL = 'https://booking-api.skypicker.com/api/v0.1/check_flights'
        params = {
            'v': 2,
            'booking_token': token,
            'bnum': 1,
            'pnum': 1,
            'currency': 'USD',
        }
        data = requests.get(url=CHECK_URL, params=params).json()

        return data['flights_checked']

    def handle(self, *args, **options):
        Flight.objects.all().delete()
        DAYS = 30
        DATA_URL = 'https://api.skypicker.com/flights?'
        routes = Route.objects.all()
        cur_date = datetime.datetime.today()
        dates = [cur_date + datetime.timedelta(days=x) for x in range(DAYS)]
        
        for route in routes:
            for date in dates:
                str_date = date.strftime("%d/%m/%Y")
                print(route.from_code + " - " + route.to_code + " " + str_date)
                
                params = {
                    'fly_from': route.from_code,
                    'fly_to': route.to_code,
                    'partner': 'picky',
                    'date_from': str_date,
                    'date_to': str_date,
                }
                data = requests.get(url=DATA_URL, params=params).json()

                for choice in data['data']:
                    if self.valid_booking(choice['booking_token']) and choice['availability']:
                        flight = Flight(
                            route=route,
                            booking_token=choice['booking_token'],
                            price=choice['price'],
                            time=choice['dTimeUTC'],
                            airline=', '.join(choice['airlines']),
                            duration=choice['fly_duration'],
                            seats=choice['availability']
                        )
                        flight.save()
        
        print('Updating flights is finished.')
