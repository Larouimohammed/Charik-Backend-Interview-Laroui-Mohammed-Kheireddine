from django.db import models


class Contact(models.Model):
    email= models.EmailField(unique=True,max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age =  models.IntegerField()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"