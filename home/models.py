from datetime import datetime
from email.headerregistry import Address
from zipapp import ZipAppError
from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=122)
   email = models.CharField(max_length=122)
   phone = models.CharField(max_length=12)
   desc = models.TextField() 

   def __str__(self):
        
         now = datetime.now()
         return self.name 



class Register(models.Model):
   Name = models.CharField(max_length=122)
   Address = models.TextField(max_length=122)
   email = models.CharField(max_length=122, null=True)
   Package = models.CharField(max_length=30)

   def __str__(self):
        
         now = datetime.now()
         return self.Name 