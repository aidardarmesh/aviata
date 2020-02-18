from django.shortcuts import render
from aviata.models import Route, Flight

def index(request):
    routes = Route.objects.all()
    context = {
        'routes': routes,
    }
    
    return render(request, 'index.html', context)

