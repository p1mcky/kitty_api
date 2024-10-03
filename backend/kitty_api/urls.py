from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views
from .yasg import urlpatterns as doc_url


router = routers.DefaultRouter()
router.register(r'kitties', views.KittyViewSet)
router.register(
    r'kitties/(?P<kitty_id>\d+)/rating',
    views.KittyRatingView,
    basename='rating'
)
router.register(r'breeds', views.BreedViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_url
