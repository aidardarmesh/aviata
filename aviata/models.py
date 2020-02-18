from django.db import models

class Route(models.Model):
    from_code = models.CharField(max_length=10)
    to_code = models.CharField(max_length=10)

class Flight(models.Model):
    route = models.ForeignKey('Route', on_delete=models.CASCADE)
    booking_token = models.TextField()
    price = models.FloatField()
    time = models.DateTimeField()
    airline = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    seats = models.IntegerField()
