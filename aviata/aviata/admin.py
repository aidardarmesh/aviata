from django.contrib import admin
from aviata.models import Route

class RouteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Route, RouteAdmin)
