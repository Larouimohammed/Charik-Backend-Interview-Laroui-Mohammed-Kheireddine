from django.http import JsonResponse
import requests

def get_deal_id_by_name(deal_name,custom_headers):
        url = "https://api.hubapi.com/crm/v3/objects/deals/search"
        search_payload = {
            "filterGroups": [
                {
                    "filters": [
                        {
                            "propertyName": "dealname",
                            "operator": "EQ",
                            "value": deal_name
                        }
                    ]
                }
            ],
            "properties": ["dealname"],
            "limit": 1
        }

        response = requests.post(url, json=search_payload, headers=custom_headers)
        
        if response.status_code == 200:
            results = response.json().get('results')
            if results:
                deal_id = results[0].get('id')
                return deal_id
            else:
                return None
        else:
            error_detail = response.json()
            raise Exception(f"Error fetching deal: {error_detail}")

def get_contact_id_by_name(first_name,last_name,custom_headers):
        url = "https://api.hubapi.com/crm/v3/objects/contacts/search"
        search_payload = {
            "filterGroups": [{
                "filters": [
                    {"propertyName": "firstname", "operator": "EQ", "value": first_name},
                    {"propertyName": "lastname", "operator": "EQ", "value": last_name}
                ]
            }],
            "properties": ["firstname", "lastname", "email"]
        }

        
        response = requests.post(url, json=search_payload, headers=custom_headers)
        
        if response.status_code == 200:
            results = response.json().get('results', [])
            if results:
                contact_id = results[0].get('id')
                return contact_id
            else:
                return JsonResponse({"error": "Contact not found"}, status=404)
        else:
            return JsonResponse({"error": "Failed to search for contact", "details": response.json()}, status=response.status_code)
        
        
def get_all_contacts(custom_headers):
        url = "https://api.hubapi.com/crm/v3/objects/contacts"
        contacts = []
        while url:
            response = requests.get(url,headers=custom_headers)
            if response.status_code == 200:
                data = response.json()
                contacts.extend(data.get('results', []))
                url = data.get('paging', {}).get('next', {}).get('link')
            else:
                raise Exception(f"Error fetching contacts: {response.json()}")
            
        return contacts

def get_deals_for_contact(contact_id,custom_headers):
        url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}/associations/deals'
        response = requests.get(url, headers=custom_headers)
        if response.status_code == 200:
            deals = response.json().get('results', [])
            return deals
        else:
            raise Exception(f"Error fetching deals for contact {contact_id}: {response.json()}")