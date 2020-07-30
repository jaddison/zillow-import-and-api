from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from rest_framework import permissions

ZILLOW_API_KEY = getattr(settings, 'ZILLOW_API_KEY', None)
if ZILLOW_API_KEY is None:
    raise ImproperlyConfigured(f"ZILLOW_API_KEY is required")


class APIKeyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.META.get('HTTP_ZILLOW_API_KEY') == ZILLOW_API_KEY
