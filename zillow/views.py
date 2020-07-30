from rest_framework import viewsets, permissions
from rest_framework.schemas import AutoSchema

from .models import Property
from .permissions import APIKeyPermission
from .serializers import PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a paginated list of Zillow properties.

    retrieve:
    Return the specific Zillow property.

    create:
    Create (and return) a Zillow property.

    update:
    Update (and return) an existing Zillow property.

    partial_update:
    Partially update (and return) an existing Zillow property.

    delete:
    Remove an existing Zillow property.
    """
    schema = AutoSchema()
    queryset = Property.objects.all().order_by('-zillow_id')
    serializer_class = PropertySerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'delete']:
            permission_classes = [APIKeyPermission]
            return [permission() for permission in permission_classes]

        return super().get_permissions()

    def get_queryset(self):
        qs = self.queryset

        price_max = self.request.query_params.get('price_max')
        if price_max is not None:
            qs = qs.filter(price__lte=price_max)

        price_min = self.request.query_params.get('price_min')
        if price_min is not None:
            qs = qs.filter(price__gte=price_min)

        # other filters here

        return qs