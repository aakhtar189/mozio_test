from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_model

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)


class Polygon(gis_model.Model):
    supplier = gis_model.ForeignKey(Supplier, null=True, blank=True)
    name = gis_model.CharField(max_length=255)
    price = gis_model.FloatField(max_length=255, default=0.0)
    point = gis_model.PointField(srid=4326, null=True, blank=True)
    objects = gis_model.GeoManager()
