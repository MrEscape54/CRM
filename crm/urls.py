from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    #Apps
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('opportunities/', include('opportunities.urls')),
    path('tasks/', include('tasks.urls')),


    #APIs
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
