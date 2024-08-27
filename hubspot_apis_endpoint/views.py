import requests,json 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_contact_id_by_name,get_deal_id_by_name,get_all_contacts,get_deals_for_contact


# Hubspot APIS Endpoint 

HUBSPOT_API_ENDPOINT_CREATE_CONTACTS = "https://api.hubapi.com/crm/v3/objects/contacts"
HUBSPOT_API_ENDPOINT_CREATE_DEALS="https://api.hubapi.com/crm/v3/objects/deals"
HUBSPOT_API_ENDPOINT_ASSOCIATE_CONTACT_DEALS ="https://api.hubapi.com/crm/v3/associations/deal/contact/batch/create"


# Views Api handler 
class ContactView(APIView):
    
    # create contact
    def post(self, request):  
        if request.method == 'POST':
            headers = {
            "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
            "Content-Type": "application/json"
            }
            request_body = json.loads(request.body)
            
            contact_data={
            "properties": {
                    "email": request_body.get('email'),
                    "firstname": request_body.get('firstname'),
                    "lastname": request_body.get('lastname'),
                    "phone": request_body.get('phone'),
                    "jobtitle": request_body.get('jobtitle'),
                    "company": request_body.get('company'),
                    "website": request_body.get('website'),
                }
            
            }
            response = requests.post(HUBSPOT_API_ENDPOINT_CREATE_CONTACTS, json=contact_data, headers=headers)

            if response.status_code == 201:

                return Response({"message": "Contact created successfully"}, status=201)

            else:
                return Response({"error": response.json()}, status=response.status_code)

    
        return Response({"error": "Invalid request method"}, status=400)
  
    # get lsit of all contact with associated deals
    def get(self,request):
        if request.method == 'GET':
            headers = {
            "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
            "Content-Type": "application/json"
            }
            try:
                contacts = get_all_contacts(custom_headers=headers)
        
                contacts_with_deals = []
            
                for contact in contacts:
                    contact_id = contact.get('id')
                    deals = get_deals_for_contact(contact_id,custom_headers=headers)
                    contact_data = {
                    "contact_id": contact_id,
                    "firstname": contact.get('properties', {}).get('firstname'),
                    "lastname": contact.get('properties', {}).get('lastname'),
                    "email": contact.get('properties', {}).get('email'),
                    "deals": deals
                    }
                    contacts_with_deals.append(contact_data)
                
                return Response(contacts_with_deals, status=200)
        
            except Exception as e:
                return Response({"error": str(e)}, status=500)
          

# Deals view handler 
class DealView(APIView):
     
    # create delas  
    def post(self, request):  
        
        if request.method == 'POST':
            request_body = json.loads(request.body)
            headers = {
                "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
                "Content-Type": "application/json"
            }
            deal_data = {
            "properties": {
                "dealname": request_body.get('dealname'),
                }
            }
            response = requests.post(HUBSPOT_API_ENDPOINT_CREATE_DEALS, json=deal_data, headers=headers)

            if response.status_code == 201:
                return Response({"message": "Deal created successfully"})
            else:
                return Response({"error": response.json()}, status=response.status_code)

        return Response({"error": "Invalid request method"}, status=400)
    
# Association views handler
class AssociationView(APIView):
    # associate contact with deals
    def post(self, request):  
    
        if request.method == 'POST':
            request_body = json.loads(request.body)
            headers = {
            "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
            "Content-Type": "application/json"
            }
            
            deal_name=request_body.get('dealname')
            contact_first_name=request_body.get('contact_first_name')
            contact_last_name=request_body.get('contact_last_name')
        
            deal_id=get_deal_id_by_name(deal_name,custom_headers=headers)
            contact_id=get_contact_id_by_name(first_name=contact_first_name,last_name=contact_last_name,custom_headers=headers)
            data = {
                "inputs": [
                {
                    "from": {
                        "id": deal_id
                    },
                    "to": {
                        "id": contact_id
                    },
                    "type": "deal_to_contact" 
                }
            ]
            }
            response = requests.post(HUBSPOT_API_ENDPOINT_ASSOCIATE_CONTACT_DEALS, json=data, headers=headers)

            if response.status_code == 201:
                return Response({"message": "Deal and Contact are Associated"})
            else:
                return Response({"error": response.json()}, status=response.status_code)

        return Response({"error": "Invalid request method"}, status=400)





