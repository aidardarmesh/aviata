from django import forms
from aviata.models import Route

class DateInput(forms.DateInput):
    input_type = 'date'

class RouteForm(forms.Form):
    choices = [(route.pk, f"{route.from_code} -> {route.to_code}") for route in Route.objects.all()]
    route = forms.ChoiceField(choices=choices)
    date = forms.DateField(widget=DateInput())

