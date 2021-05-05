from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.utils.text import slugify

from accounts.models import Account, ParentAccount
from accounts.serializers import AccountSerializer, ParentAccountSerializer

from contacts.models import Contact
from contacts.serializers import ContactSerializer

from opportunities.models import Opportunity, Technology
from opportunities.serializers import OpportunitySerializer, TechnologySerializer


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


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        full_name = f'{serializer.validated_data["first_name"]} {serializer.validated_data["last_name"]}'
        serializer.save(created_by=self.request.user, 
                        slug=slugify(full_name))


class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, 
                        slug=slugify(serializer.validated_data['name']))

        
class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)