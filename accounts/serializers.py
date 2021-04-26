from rest_framework import serializers
from .models import Account, ParentAccount

class AccountSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.username')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Account
        fields = [
            'name', 
            'country', 
            'industry', 
            'parent_account', 
            'status', 
            'address', 
            'website', 
            'description', 
            'is_active', 
            'slug',
            'contacts', 
            'assigned_to',
            'created_by',
        ]

class ParentAccountSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = ParentAccount
        fields = ['id', 'name', 'slug', 'created_by']
