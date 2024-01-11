from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
