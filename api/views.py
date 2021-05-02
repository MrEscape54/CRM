from rest_framework import viewsets
from rest_framework import permissions
from django.utils.text import slugify

from accounts.models import Account, ParentAccount
from accounts.serializers import AccountSerializer, ParentAccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, 
                        slug=slugify(serializer.validated_data['name']))


class ParentAccountViewSet(viewsets.ModelViewSet):
    queryset = ParentAccount.objects.all()
    serializer_class = ParentAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user, 
                        slug=slugify(serializer.validated_data['name']))

    
