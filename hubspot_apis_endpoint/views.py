import requests,json 
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .utils import get_contact_id_by_name,get_deal_id_by_name,get_all_contacts,get_deals_for_contact


def create_contact(request):
    if request.method == 'POST':
        url = "https://api.hubapi.com/crm/v3/objects/contacts"
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

        response = requests.post(url, json=contact_data, headers=headers)

        if response.status_code == 201:
            print("Contact {data[email]} are created succesfully")
            return JsonResponse({"message": "Contact created successfully"}, status=201)
        else:
            print("Contact {data[email]} failled to created")
            return JsonResponse({"error": response.json()}, status=response.status_code)
    
    return JsonResponse({"error": "Invalid request method"}, status=400)
 
        
        
def create_deal(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        url = "https://api.hubapi.com/crm/v3/objects/deals"
        headers = {
            "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
            "Content-Type": "application/json"
        }
        deal_data = {
            "properties": {
                "dealname": request_body.get('dealname'),
            }
        }
        response = requests.post(url, json=deal_data, headers=headers)

        if response.status_code == 201:
            return JsonResponse({"message": "Deal created successfully"})
        else:
            return JsonResponse({"error": response.json()}, status=response.status_code)

    return JsonResponse({"error": "Invalid request method"}, status=400)
    
    
def contact_deal_associate(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        url = "https://api.hubapi.com/crm/v3/associations/deal/contact/batch/create"
        headers = {
            "Authorization": f"Bearer {settings.HUBSPOT_TOKEN}",
            "Content-Type": "application/json"
        }
        deal_name=request_body.get('dealname')
        contact_first_name=request_body.get('contact_first_name')
        contact_last_name=request_body.get('contact_last_name')
        
        deal_id=get_deal_id_by_name(deal_name,custom_headers=headers)
        contact_id=get_contact_id_by_name(first_name=contact_first_name,last_name=contact_last_name,custom_headers=headers)
        print(deal_name)
        print(deal_id)
        print(contact_id)
        
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
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return JsonResponse({"message": "Deal and Contact are Associated"})
        else:
            return JsonResponse({"error": response.json()}, status=response.status_code)

    return JsonResponse({"error": "Invalid request method"}, status=400)



def list_contacts_associated_with_deals(request):
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
                
            return JsonResponse(contacts_with_deals, status=200,safe=False)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)




