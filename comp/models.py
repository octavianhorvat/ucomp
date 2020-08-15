from django.db import models
from postgres_composite_types import CompositeType


class LicencePlate(models.Model):
    licence_plate = models.CharField(max_length=60)
    insurance = models.DateField()
    address = models.CharField(max_length=60)
    created_at = models.DateField()
    updated_at = models.DateField()
    # image = db.relationship("Image", backref="licenceplate", lazy=True)

    def __str__(self):
        return f"{self.id}: {self.licence_plate}"


class Image(models.Model):
    description = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.licence_plate}"


class Complaint(models.Model):
    description = models.CharField(max_length=500)
    image = models.ManyToManyField(
        Image, blank=True, related_name="complaints")
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f"{self.id}: {self.licence_plate}"
