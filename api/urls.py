from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('accounts', views.AccountViewSet)
router.register('parents', views.ParentAccountViewSet)


urlpatterns = [
    path("", include(router.urls))
]