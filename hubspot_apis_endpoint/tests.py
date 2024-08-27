import requests
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
# from .models import Contact

url = "http://localhost:8000/apis/contact/"


# from django.urls import reverse

class ContactAPITestCase(TestCase):
    def test_create_contact(self):
        # self.client = APIClient()
        data = {
            'email' : 'test12907@gmail.com',
            'firstname': 'Laro',
            'lastname': 'Mohammed',
        }
        
        # contact_serialized= 
        response = requests.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])