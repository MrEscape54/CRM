from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='contact_created_by.username')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Contact
        fields = [
            'first_name', 
            'last_name', 
            'location', 
            'slug', 
            'email', 
            'phone', 
            'source', 
            'vendor', 
            'position', 
            'is_lead',
            'is_active', 
            'created_by'
        ]