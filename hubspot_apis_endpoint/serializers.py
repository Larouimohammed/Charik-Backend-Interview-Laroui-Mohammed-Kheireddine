from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class DealSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = '__all__'