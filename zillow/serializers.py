from rest_framework import serializers

from .models import Property


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'zillow_id',
            'area_unit',
            'address',
            'bathrooms',
            'bedrooms',
            'city',
            'home_size',
            'home_type',
            'last_sold_date',
            'last_sold_price',
            'link',
            'price',
            'property_size',
            'rent_price',
            'rentzestimate_amount',
            'rentzestimate_last_updated',
            'state',
            'tax_value',
            'tax_year',
            'year_built',
            'zestimate_amount',
            'zestimate_last_updated',
            'zipcode'
        ]
