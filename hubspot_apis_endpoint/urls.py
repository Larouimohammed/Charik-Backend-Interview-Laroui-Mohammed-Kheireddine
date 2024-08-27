from hubspot_apis_endpoint import views
from django.urls import path



urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='create_contact'),
    path('deal/', views.DealView.as_view(), name='create_deal'),
    path('associate/', views.AssociationView.as_view(), name='associate'),
    path('list/', views.ContactView.as_view(), name='list'),

]




