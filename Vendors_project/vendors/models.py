from django.db import models
from django.core.validators import RegexValidator


class Vendors(models.Model):
    name = models.CharField(max_length = 200,null=True)    
    phone_number = models.CharField(max_length=17, blank=True)
    fax = models.CharField( max_length=17, blank=True)    
    website = models.CharField(max_length = 200,null=True)
    address1 = models.CharField(max_length = 200,null=True)
    address2 = models.CharField(max_length = 200,null=True)
    city = models.CharField(max_length = 200,null=True)
    state = models.CharField(max_length = 200,null=True)
    zipp = models.CharField(max_length = 200,null=True)
    country = models.CharField(max_length = 200,null=True,default="United States")
    ein = models.CharField(max_length = 200,null=True)    
    no_of_consultants = models.IntegerField(blank=True, null=True,editable = False)
    preferred_vendor = models.CharField(max_length=40,null=True)
    date = models.DateField(null=True)
    agreement_status = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField(max_length = 200,null=True) 
    first_name = models.CharField(max_length = 200,null=True)    
    last_name = models.CharField(max_length=200, blank=True)
    title = models.CharField( max_length=200, blank=True)    
    desk_phone = models.CharField(max_length = 200,null=True)
    mobile = models.CharField(max_length=17, blank=True)    
    email = models.CharField(max_length = 200,null=True)
    address1 = models.CharField(max_length = 200,null=True)
    address2 = models.CharField(max_length = 200,null=True)
    city = models.CharField(max_length = 200,null=True)
    state = models.CharField(max_length = 200,null=True)
    zipp = models.CharField(max_length = 200,null=True)
    country = models.CharField(max_length = 200,null=True,default="United States")
    speciality = models.CharField(max_length = 200,null=True)

    def __str__(self):
        return self.name