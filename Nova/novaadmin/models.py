from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.lookups import IsNull

# Create your models here.
class Mysupport(models.Model):
    empsdate = models.CharField(max_length=50,null=True)
    empsprfct = models.CharField(max_length=50,null=True)
    empsid = models.CharField(max_length=50,null=True)
    empallot = models.CharField(max_length=50,null=True)
    empcmp = models.CharField(max_length=100,null=True)
    stype = models.CharField(max_length=50,null=True)
    empssdetail = models.CharField(max_length=500,null=True)
    intialtime = models.CharField(max_length=20,null=True)
    endtimecurrent = models.CharField(max_length=20,null=True)
    emptotaltime = models.CharField(max_length=20,null=True) 
    sstatus = models.CharField(max_length=25,null=True)
    mailflag = models.CharField(max_length=10,default="False")
    timesheetflag = models.CharField(max_length=10,default="False")
    
    #empreslvd = models.CharField(max_length=50,null=True)



