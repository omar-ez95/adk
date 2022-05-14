from django.db import models

# Create your models here.
CATEGORY_TYPES = ((1,'dryer'),(2,'washing'))

class Washing(models.Model):
    name = models.CharField(max_length=30)
    on = models.BooleanField(default=False)
    type = models.IntegerField(choices=CATEGORY_TYPES, default=1)


class Dry(models.Model):
    name = models.CharField(max_length=30)
    on = models.BooleanField(default=False)