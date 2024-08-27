from rest_framework import serializers
from .models import Contact,Deal,Association


class ContactSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    firstname = serializers.CharField(max_length=100,required=True)
    lastname = serializers.CharField(max_length=100)
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class DealSerializer(serializers.Serializer):
    dealname = serializers.CharField(max_length=100,required=True)
    class Meta:
        model = Deal
        fields = '__all__'
        
        

class AssociationSerializer(serializers.Serializer):
    dealname = serializers.CharField(max_length=100,required=True)
    contact_first_name=serializers.CharField(max_length=100)
    contact_last_name=serializers.CharField(max_length=100)
    class Meta:
        model = Association 
        fields = '__all__'