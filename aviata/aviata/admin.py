from django.contrib import admin
from aviata.models import Route, Flight

class RouteAdmin(admin.ModelAdmin):
    pass

class FlightAdmin(admin.ModelAdmin):
    pass

admin.site.register(Route, RouteAdmin)
admin.site.register(Flight, FlightAdmin)
