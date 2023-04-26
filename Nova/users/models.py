from novacustomermodule.models import Techsupport
from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Extendmyuser(models.Model):
    companyname = models.CharField(max_length=200,null=False)
    approval = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

   
class Empuser(models.Model):
    isemp = models.BooleanField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #techsup = models.OneToOneField(Techsupport,on_delete=models.CASCADE,null=True)
    empnamecpy = models.CharField(max_length=200,null=True)
    client = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    status =  models.CharField(max_length=100,default="Offline")

class Phoneofclnt(models.Model):

    ussr = models.OneToOneField(User,on_delete=models.CASCADE)
    pno = models.CharField(max_length=10,null=True)
