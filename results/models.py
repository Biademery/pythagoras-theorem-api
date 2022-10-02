from django.db import models

class Result(models.Model):
    c = models.FloatField()
    a = models.FloatField()
    b = models.FloatField()

