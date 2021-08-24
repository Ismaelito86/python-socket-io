from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IsmaViewSet

router = DefaultRouter()
router.register('aspirantes', IsmaViewSet, basename='aspirantes')

urlpatterns = [
    path('',include(router.urls)),
]