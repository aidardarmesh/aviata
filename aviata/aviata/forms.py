from django import forms
from aviata.models import Route

class RouteForm(forms.Form):
    choices = [(route.pk, f"{route.from_code} -> {route.to_code}") for route in Route.objects.all()]
    route = forms.ChoiceField(choices=choices)

