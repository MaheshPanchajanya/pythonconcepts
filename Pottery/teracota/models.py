from django.db import models

from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    imgfrcat = models.ImageField(upload_to='categorypics',null=True,blank=True)

class Potsmfg(models.Model):
    potname = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    materialtype = models.CharField(max_length=100)
    color = models.CharField(max_length=100,null=True)
    discription = models.CharField(max_length=200,null=True)
    img  = models.ImageField(upload_to='pics',null=True,blank=True)
    img1  = models.ImageField(upload_to='pics',null=True,blank=True)
    img2  = models.ImageField(upload_to='pics',null=True,blank=True)
    img3  = models.ImageField(upload_to='pics',null=True,blank=True)
    img4  = models.ImageField(upload_to='pics',null=True,blank=True)
    

class Ads(models.Model):
   adsimg  = models.ImageField(upload_to='adsimages',null=True,blank=True)
   Event = models.CharField(max_length=25,null=True)
   Eflg = models.CharField(max_length=6,default="False")
   discription =  models.CharField(max_length=25,null=True)
   title = models.CharField(max_length=25,null=True)

   
class About(models.Model):
    cnc = models.ImageField(upload_to='bof',null=True,blank=True)
    directorname = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100)
    properitorabt = models.CharField(max_length=200)
    phone = PhoneNumberField(null=True, blank=True, unique=True)

class Feed(models.Model):
    picforblg = models.ImageField(upload_to='blog',null=True,blank=True)
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Sliderabt(models.Model):
    ibtmg = models.ImageField(upload_to='cskabt',null=True,blank=True)

class Eyusr(models.Model):
    fullname = models.CharField(max_length=100)
    phno = PhoneNumberField(null=True, blank=True, unique=True)
    mail = models.EmailField(max_length=100)
    details = models.EmailField(max_length=500)

class Special1(models.Model):
    
    season = models.ImageField(upload_to='special',null=True,blank=True)
    season1 = models.ImageField(upload_to='special',null=True,blank=True)
    season2 = models.ImageField(upload_to='special',null=True,blank=True)
    season3 = models.ImageField(upload_to='special',null=True,blank=True)
    season4 = models.ImageField(upload_to='special',null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=10,null=True)
    price = models.CharField(max_length=20,null=True)
    discription = models.CharField(max_length=200,null=True)
    purpose = models.CharField(max_length=25,null=True)
    material = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=25,null=True)

class Special2(models.Model):
    season = models.ImageField(upload_to='special',null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=10,null=True)
    discription = models.CharField(max_length=200,null=True)
    purpose = models.CharField(max_length=25,null=True)
    material = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=25,null=True)

class Special3(models.Model):
    season = models.ImageField(upload_to='special',null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    size = models.CharField(max_length=10,null=True)
    price = models.CharField(max_length=10,null=True)
    discription = models.CharField(max_length=200,null=True)
    purpose = models.CharField(max_length=25,null=True)
    material = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=25,null=True)

class Pricelist(models.Model):
    size = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=10,null=True)
    pid = models.ForeignKey(Potsmfg,on_delete=models.CASCADE,null=True)

class Myorder(models.Model):
    user = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=50,null=True)
    size = models.CharField(max_length=100,null=True)
    quantity = models.CharField(max_length=100,null=True)
    baseprice = models.CharField(max_length=25,null=True)
    kartimg = models.CharField(max_length=100,null=True)
    totalprice = models.CharField(max_length=25,null=True)
    mailflag = models.CharField(max_length=10,default="false")
    phno = models.CharField(max_length=11,null=True)
    Email = models.CharField(max_length=100,null=True)
    address1 = models.CharField(max_length=100,null=True)
    address2 = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=10,null=True)
    state =  models.CharField(max_length=100,null=True)
    


    
    
