from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from zillow import views

router = routers.DefaultRouter()
router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='Zillow Data')),
]

