import requests
from django.test import TestCase
from rest_framework import status


class ContactAPITestCase(TestCase):
    def test_create_contact(self):
        
        url = "http://localhost:8000/apis/contact/"
        
        data= {"email": "finaltest5@gmail.com","firstname":"test", "lastname":"test"}
        
        session = requests.Session()
        
        response = session.post(url=url, json=data) 
   
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        if response.status_code == status.HTTP_400_BAD_REQUEST:
        
            print("Error details:", response.data)
    

      
