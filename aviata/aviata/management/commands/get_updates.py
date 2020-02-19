from django.core.management.base import BaseCommand, CommandError
from aviata.models import Route, Flight
import datetime, requests, random
import concurrent.futures

class Command(BaseCommand):
    def valid_booking(self, token):
        CHECK_URL = 'https://booking-api.skypicker.com/api/v0.1/check_flights?'
        params = {
            'v': 2,
            'booking_token': token,
            'bnum': 1,
            'pnum': 1,
            'currency': 'USD',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' + str(random.randint(0, 100)),
            'Content-Type': 'application/json; charset=utf-8',
        }
        try:
            resp = requests.get(url=CHECK_URL, headers=headers, params=params)
            data = resp.json()
        except Exception as e:
            print(resp.headers, e)
            return False

        return data['flights_checked']

    def handle(self, *args, **options):
        Flight.objects.all().delete()
        DAYS = 30
        DATA_URL = 'https://api.skypicker.com/flights?'
        routes = Route.objects.all()
        cur_date = datetime.datetime.today()
        dates = [cur_date + datetime.timedelta(days=x) for x in range(DAYS)]

        def get_flights(route):
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
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36' + str(random.randint(0, 100)),
                    'Content-Type': 'application/json; charset=utf-8',
                }

                try:
                    resp = requests.get(url=DATA_URL, headers=headers, params=params)
                    data = resp.json()
                except Exception as e:
                    print(resp.headers, e)
                    continue

                for choice in data['data']:
                    if self.valid_booking(choice['booking_token']) and choice['availability']['seats']:
                        flight = Flight(
                            route=route,
                            booking_token=choice['booking_token'],
                            price=choice['price'],
                            time=datetime.datetime.fromtimestamp(choice['dTimeUTC']),
                            airline=', '.join(choice['airlines']),
                            duration=choice['fly_duration'],
                            seats=choice['availability']['seats']
                        )
                        flight.save()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(routes)) as executor:
            executor.map(get_flights, routes)

        print('Updating flights is finished.')
