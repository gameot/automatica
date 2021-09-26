from rest_framework.routers import DefaultRouter

from .views import ShopViewSet

router = DefaultRouter()
router.register(prefix='', viewset=ShopViewSet, basename='shops')

urlpatterns = router.urls
