# Charik-Backend-Interview-Laroui-Mohammed-Kheireddine
DRF integration with HubSpot

# Introduction :

HubSpot is powerfull open-source crm platefrome and this package is DRF (django rest framework) 
integradtion with this third party crm soulution using django rest api calls that can help entreprise to easaly afect CRUD opration to exisiting APPS and offre more custimisation and facilitate ressource management . 

# Setup: 
    
    #after successfully creating Private App in hubspot copy your Token and export then as env var .
    
    export  YOUR_HUBSPOT_TOKEN='past_your_token_here'
    
    export  IMAGE_TAG='image_tag_name'

    git clone https://github.com/Larouimohammed/Charik-Backend-Interview-Laroui-Mohammed-Kheireddine.git

    cd Charik-Backend-Interview-Laroui-Mohammed-Kheireddine
    
    docker build  .  -t hubspot-apis-v1

    docker run -it -d -p 8000:8000 -e HUBSPOT_TOKEN=$YOUR_HUBSPOT_TOKEN  $IMAGE_TAG


# Test :
   
        sudo apt update -y && sudo apt upgrade -y && sudo apt install curl -y

## create Contact 

        curl -X POST -H "Content-Type: application/json" -d '{"email": "m.laroui@esi-sba.dz", "firstname": "Laroui","lastname" :"Mohammed Kheireddine"}' http://localhost:8000/apis/contact/

##  create deal 
        curl -X POST -H "Content-Type: application/json" -d '{"dealname":"Deal - Laroui Mohammed Kheireddine"}' http://localhost:8000/apis/deal/

## associate contact with deal

        curl -X POST -H "Content-Type: application/json" -d '{"dealname":"Deal - Laroui Mohammed Kheireddine","contact_first_name":"Laroui","contact_last_name":"Mohammed Kheireddine"}' http://localhost:8000/apis/associate/

##  list all contact with associated deals

        curl -X GET http://localhost:8000/apis/list/        
