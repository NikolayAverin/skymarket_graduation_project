from django.urls import include, path
from rest_framework import routers
from ads.views import AdViewSet
from ads.views import AdsListApiView

ads_router = routers.SimpleRouter()
ads_router.register(r"ads", AdViewSet)

ads_router.register("ads", AdViewSet, basename="ads")


urlpatterns = [
    path("", include(ads_router.urls)),
    path("ads/me/", AdsListApiView.as_view(), name="me_ads")
]
