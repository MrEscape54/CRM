from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Homepage
    path("", views.HomeView.as_view(), name="home"),

    #Apps
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
