from django.shortcuts import render
from aviata.models import Route, Flight
from aviata.forms import RouteForm
import datetime

def index(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            till_date = date + datetime.timedelta(days=1)
            route = Route.objects.get(pk=form.cleaned_data['route'])
            flights = Flight.objects.filter(route=route, time__range=[date, till_date])

            return render(request, 'flights.html', {'flights': flights})

    return render(request, 'index.html', {'form': RouteForm()})

