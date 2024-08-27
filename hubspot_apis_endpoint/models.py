from django.db import models


class Contact(models.Model):
    email= models.EmailField(unique=True,max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class Deal(models.Model):
    dealname = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='deals')

    def __str__(self):
        return f"{self.name}"



class Association(models.Model):
    dealname=models.CharField(max_length=100)
    contact_first_name=models.CharField(max_length=100)
    contact_last_name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.dealname} {self.contact_first_name}"
    
    