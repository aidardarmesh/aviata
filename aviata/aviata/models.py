from django.db import models

class Route(models.Model):
    from_code = models.CharField(max_length=10)
    to_code = models.CharField(max_length=10)
