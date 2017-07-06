from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_model


# class Location(models.Model):
#     # 'name' can also represent address value
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255, null=True, blank=True)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     is_hometown = models.BooleanField(default=False)
#     zip_code = models.CharField(max_length=255, null=True, blank=True)
#     point = models.PointField(srid=4326, null=True, blank=True)
#     objects = models.GeoManager()
#
#     class Meta:
#         verbose_name = "Location"
#         verbose_name_plural = "Locations"
#
#     def __unicode__(self):
#         return self.name

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
