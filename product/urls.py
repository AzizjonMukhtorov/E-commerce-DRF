from django.urls import path, include

from rest_framework import routers

from .views import CategoryViewSet, BrandViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
