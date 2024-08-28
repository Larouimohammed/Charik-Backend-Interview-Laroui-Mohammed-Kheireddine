# Charik-Backend-Interview-Laroui-Mohammed-Kheireddine

   ### DRF integration with HubSpot APIS

# Introduction :

HubSpot is powerfull open-source crm platefrome and this package is DRF (django rest framework) 
integradtion with this third party crm soulution using django rest api calls that can help entreprise to easaly afect CRUD opration to exisiting APPS and offre more custimisation and facilitate ressource management . 

# Features
 - Create a contact in Hubspot PrivateApps .
 - Create a Deal in Hubspot PrivateApps .
 - Associate contact With Deal .
 - List all Contact With Assscoiated Deals.

# Setup: 
    
### after successfully creating Private App in hubspot copy your Token and export then as env var  follow this easy steps to get your djnago web server ready .
 
- export  YOUR_HUBSPOT_TOKEN='past_your_token_here'
- export  IMAGE_TAG='hubspot-apis-v1'
- git clone https://github.com/Larouimohammed/Charik-Backend-Interview-Laroui-Mohammed-Kheireddine.git
- cd Charik-Backend-Interview-Laroui-Mohammed-Kheireddine
- python3 manage.py test
- docker build  .  -t $IMAGE_TAG
- docker run -it -d --network host  -e HUBSPOT_TOKEN=$YOUR_HUBSPOT_TOKEN $IMAGE_TAG

# Test :
   
        sudo apt update -y && sudo apt upgrade -y && sudo apt install curl -y

### Create Contact 

        curl -X POST -H "Content-Type: application/json" -d '{"email": "m.laroui@esi-sba.dz", "firstname": "Laroui","lastname" :"Mohammed Kheireddine"}' http://localhost:8000/apis/contact/

### Create Deal 
        
        curl -X POST -H "Content-Type: application/json" -d '{"dealname":"Deal - Laroui Mohammed Kheireddine"}' http://localhost:8000/apis/deal/

### Associate Contact with deals

        curl -X POST -H "Content-Type: application/json" -d '{"dealname":"Deal - Laroui Mohammed Kheireddine","contact_first_name":"Laroui","contact_last_name":"Mohammed Kheireddine"}' http://localhost:8000/apis/associate/

### List all Contacts with Associated Deals

        curl -X GET http://localhost:8000/apis/list/        
