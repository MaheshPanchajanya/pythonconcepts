
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db import models
from django.utils import timezone
import random
from datetime import datetime, timedelta
#from phonenumber_field.modelfields import PhoneNumberField
#from phonenumber_field.phonenumber import PhoneNumbers
# Create your models here.

def increment_booking_number():
    last_booking = Techsupport.objects.all().order_by('id').last()
    if not last_booking:
        return 'NOVA-{}-{}'.format(datetime.today().strftime('%d-%m-%Y'), 100)
    
    booking_id = last_booking.id
    booking_int2 = str(booking_id[5:15])
    chk = datetime.today().strftime('%d-%m-%Y')
    
    if chk > booking_int2:
        return 'NOVA-{}-{}'.format(datetime.today().strftime('%d-%m-%Y'), 100)   
    else:

        booking_int = int(booking_id[16:19])
    
        new_booking_int = booking_int + 1
        new_booking_id = 'NOVA-{}-{}'.format(datetime.today().strftime('%d-%m-%Y'), new_booking_int)
        return new_booking_id


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    tallynetid = models.CharField(max_length=100)
    password =   models.CharField(max_length=20)
    tallyserialno = models.CharField(max_length=25)
    phoneno = models.CharField(max_length=13)
    companyname = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2  = models.CharField(max_length=100)
    pan  = models.CharField(max_length=15)
    gsttin  = models.CharField(max_length=20)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip = models.CharField(max_length=25)

class Daybook(models.Model):
    
    date = models.CharField(max_length=10)
    vouchertype = models.CharField(max_length=100)
    vouchernumber = models.CharField(max_length=100)
    partyledger = models.CharField(max_length=100)
    amount = models.CharField(max_length=15)

class Techsupport(models.Model):
    id=models.CharField(default=increment_booking_number,auto_created=True, primary_key=True, serialize=False,unique=True,verbose_name='ID',max_length=200)
    sdate = models.CharField(max_length=50)
    prfctdate = models.CharField(max_length=20,null=True)
    scmp = models.CharField(max_length=100)
    suser = models.CharField(max_length=100)
    sphno = models.CharField(max_length=10,null=True)
    sprdt = models.CharField(max_length=100)
    sdetail = models.CharField(max_length=500)
    allot = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    screenshot = models.ImageField(upload_to="ss",null=True,blank=True)
    st = models.TimeField(default=datetime.now()+timedelta(minutes=2))
    intial_starttime=models.CharField(max_length=100,null=True)
    intialflg=models.CharField(max_length=100,default="False")
    current_endtime=models.CharField(max_length=100,null=True)
    currentendflg=models.CharField(max_length=100,default="False")
    starttime = models.CharField(max_length=100,null=True)
    endtime = models.CharField(max_length=100,null=True)
    totaltime = models.CharField(max_length=100,null=True)
    suprtdate = models.CharField(max_length=100,null=True)
    taskclear = models.BooleanField(default=False)
    

   