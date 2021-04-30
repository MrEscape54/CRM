from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('account', views.AccountViewSet)
router.register('parent-account', views.ParentAccountViewSet)


urlpatterns = [
    path("", include(router.urls))
]