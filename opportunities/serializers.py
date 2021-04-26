from rest_framework import serializers
from .models import Opportunity, Technology

class TechnologySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='technology.username')

    class Meta:
        model = Technology
        fields = [
            'name',
            'created_by'
        ]

class OpportunitySerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by_opportunities.username')
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Opportunity
        fields = [
            'name', 
            'description',
            'account', 
            'stage', 
            'slug', 
            'source', 
            'priority', 
            'technology', 
            'category', 
            'currency', 
            'amount',
            'EDC', 
            'contacts', 
            'closed_on', 
            'closed_by', 
            'assigned_to', 
            'created_by'
        ]