from django.db import models


class Property(models.Model):
    zillow_id = models.CharField(max_length=30, db_index=True)
    link = models.URLField()

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=3)
    zipcode = models.CharField(max_length=10)

    year_built = models.PositiveSmallIntegerField(null=True)
    home_type = models.CharField(max_length=50)
    home_size = models.PositiveIntegerField(null=True)
    property_size = models.PositiveIntegerField(null=True)
    area_unit = models.CharField(max_length=10)
    bathrooms = models.FloatField(null=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)

    tax_value = models.DecimalField(max_digits=15, decimal_places=2)
    tax_year = models.PositiveSmallIntegerField()

    last_sold_date = models.DateField(null=True)
    last_sold_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    rentzestimate_last_updated = models.DateField(null=True)
    rentzestimate_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    zestimate_last_updated = models.DateField(null=True)
    zestimate_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
