from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accounts/logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

