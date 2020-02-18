from django.shortcuts import render
from aviata.models import Route, Flight
from aviata.forms import RouteForm

def index(request):
    return render(request, 'index.html', {'form': RouteForm()})

