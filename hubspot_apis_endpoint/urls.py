from django.urls import path
from hubspot_apis_endpoint import views

urlpatterns = [
    path('contact/', views.create_contact, name='create_contact'),
    path('deal/', views.create_deal, name='create_deal'),
    path('associate/', views.contact_deal_associate, name='associate'),
    path('list/', views.list_contacts_associated_with_deals, name='list'),
    
]

