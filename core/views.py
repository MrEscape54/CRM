from django.views.generic import TemplateView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class HomeView(TemplateView):
    template_name = "core/home.html"

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'accounts': reverse('account-list', request=request, format=format),
        'parent-accounts': reverse('parent-account-list', request=request, format=format)

        #TODO: Add the rest of api_urls
    })

