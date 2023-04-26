from django.core import mail
from django.http import response
from xlwt.Column import Column
from novacustomermodule.views import customer
from django.http.response import HttpResponse
from novaadmin.models import Mysupport
from django.http import JsonResponse
from django.forms.widgets import ChoiceWidget, DateTimeBaseInput
from django.http import request
from users.models import Extendmyuser, Empuser
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from novacustomermodule.models import Company, Techsupport
from . forms import Updatefrom,Clients,Manage
from datetime import datetime, timedelta
#from django.core.mail import send_mail
from django.core.mail import EmailMessage, message, send_mail
import xlwt

import pandas as pd
#import schedule
import time
#from  .filters import Manageuser

# Create your views here.
def novaadmin(request):
    
   
    if request.method == "POST":
        uname= request.POST["uname"]
        pwsd = request.POST["pwsd"]
        
        user = auth.authenticate(username=uname,password=pwsd)
        try:
            darlene =user.id
            
        except:
            print("user / password invalid")
            return redirect("novaadmin")
        #print(darlene)
        
        if user is not None:
            if User.objects.filter(id=darlene,is_superuser=True).exists():
                auth.login(request, user)

                print("done")
                hilton = User.objects.count()
                whis = Company.objects.count()
                moro = Techsupport.objects.count()
                global liqiour 
                liqiour = hilton
                global merus
                merus = whis

                #get everyone 
                csr = Extendmyuser.objects.all() 
                aps = Empuser.objects.filter(status="Online")
                   
                return render(request,"nova_dashboard.html",{'liqiour':liqiour,'merus':merus,'csr':csr,'moro':moro,'aps':aps})
                    
                       
            else:
                print("it is not Admin credentials")
                return redirect("novaadmin")    
        else:
            print("username / password is invalid")
            return redirect("novaadmin")
    else:
        return render(request,"nova_adminlogin.html")


def dipierieo(request):

    auth.logout(request)
    return redirect("novaadmin")

#def allusrs(request):
#    if user.is_authenticated:
#        mk14 = User.objects.filter(is_superuser=False)
#        return render(request,"nova_allusrs.html",{'mk14':mk14})
#    else:
#        return redirect("novaadmin")    

def dataall(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        groza = Company.objects.all()
        return render(request,"nova_data.html",{'groza':groza})
    else:
        return redirect("novaadmin")   

def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
       # hilton = User.objects.count()
       # whis = Company.objects.count()
        #moro = Techsupport.objects.count()
       # global liqiour 
       # liqiour = hilton
       # global merus
       # merus = whis

        #global csr        #get everyone 
        csr = Extendmyuser.objects.all()
        aps = Empuser.objects.filter(status="Online")
        #return JsonResponse({'liqiour':liqiour,'merus':merus,'csr':csr,'moro':moro})           
        return render(request,"nova_dashboard.html",{'csr':csr,'aps':aps})
    else:
        return redirect("novaadmin")

def manage(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        id =request.GET.get('data')
          
        csr = Extendmyuser.objects.get(user_id=id)
        form = Updatefrom(instance=csr) 
        
        if request.method == "POST":
            form = Updatefrom(request.POST, instance=csr)
            
            if form.is_valid():
                form.save()
                return redirect("dashboard")
            #save = "user is activated now"
            #return render(request,"dashboard",{'save':save})
        
            #print("unable to save")
       # fiesta = Manageuser(request.GET, queryset=csr)
       # csr = fiesta.qs
       # cemetary = {'csr':csr,'fiesta':fiesta}
    obj = {'form':form}
    return render(request,"nova_manageusr.html",obj)
    #else:
     #   return redirect("novaadmin")   
    
      #{% url '' %}?data={{scarl.id}}  
        
def manageclients(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        cid =request.GET.get('faraz')
        rid = Company.objects.get(id=cid)
        clientform = Clients(instance=rid)
        if request.method=="POST":
            clientform = Clients(request.POST, instance=rid)
            if clientform.is_valid():
                clientform.save()
                return redirect("dashboard")

    return render(request,"nova_editclients.html",{'clientform':clientform})

def  addclients(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        addform = Clients()
        if request.method=="POST":
             addform = Clients(request.POST)
             if addform.is_valid():
                 addform.save()
                 return redirect("dashboard")
        
    return render(request,"nova_addclients.html",{'addform':addform})

def supportlist(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        teago = Techsupport.objects.all()

        return render(request,"viewsupport.html",{'teago':teago})
    else:
        return render(request,"nova_adminlogin.html")

def empdashboard(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            asign=request.POST["sellist1"]
            ide = request.POST["ssid"]
            rap = Techsupport.objects.filter(id=ide).update(allot=asign,status="processing")
            prsntusr=request.user.username 
            sap = Techsupport.objects.filter(allot=prsntusr)
            lk = Empuser.objects.all()        
            current =  datetime.now()
            return render(request,"Novaempdashboard.html",{"current":current,"sap":sap,'lk':lk})
        else:

            prsntusr=request.user.username 
            sap = Techsupport.objects.filter(allot=prsntusr)
            lk = Empuser.objects.all()        
            current =  datetime.now()
            return render(request,"Novaempdashboard.html",{"current":current,"sap":sap,'lk':lk})
    else:
        
        return redirect("emplogin")

def emplogin(request):
    synom=""
    if request.method == "POST":
        ensname = request.POST["empname"]
        wrd = request.POST["pass"]
        user = auth.authenticate(username=ensname,password=wrd)
        try:
            lenin = Empuser.objects.filter(user_id=user.id)
        except:
            sept = "Invalid user"
            return render(request,"novaemplogin.html",{'invld':sept})

        for xr in lenin:
           synom=(xr.isemp)
        if synom == True:
            if user is not None:
                auth.login(request, user)
                
                rap = Empuser.objects.filter(user_id=request.user).update(status="Online")
                return redirect("empdashboard")
            else:
                errcode = "invalid username or password"
                return render(request,"Novaemplogin.html",{'errcode':errcode})
        else:
            invld = "Invalid Account"
            return render(request,"novaemplogin.html",{'invld':invld})
    else:
        return render(request,"Novaemplogin.html")

def guevara(request):
    qatar = Empuser.objects.filter(user_id=request.user).update(status="Offline")
    auth.logout(request)
    
    return redirect("emplogin")

def autofresh(request):
    hilton = Extendmyuser.objects.count()
    whis = Company.objects.count()
    moro = Techsupport.objects.count()
    caser = Empuser.objects.count()
    amd = Empuser.objects.filter(status="online")
    global liqiour 
    liqiour = hilton
    global merus
    merus = whis
    
    #global csr        #get everyone 
    #csr = Extendmyuser.objects.all() 
    #for alfa in amd:
        #print(alfa.empnamecpy)
  
        
    return JsonResponse({"liqiour":liqiour,"merus":merus,"moro":moro,"caser":caser,'amd':list(amd.values())})

def empmanage(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        addform2 =Manage()
        xmas = Company.objects.all()

        if request.method=="POST":
             addform2 = Manage(request.POST)
             if addform2.is_valid():
                addform2.save()
               
                return render(request,"novaadmin_manageemploye.html",{"addform2":addform2,"xmas":xmas})
       
    return render(request,"novaadmin_manageemploye.html",{"addform2":addform2,"xmas":xmas})

def cred(request):
    if  request.method == "POST":
        filename = request.FILES["filenameo"]
        emptype = request.POST["type"]
        data = pd.read_excel(filename)
        if emptype == "user":
            for index, row in data.iterrows():
                if User.objects.filter(username=row['uname']).exists() and  User.objects.filter(email=row['email']).exists():
                    print("username and email taken")
                    continue
                else:
                    crt = User.objects.create_user(first_name=row['fname'],last_name=row['lname'],username=row['uname'],email=row['email'],password=row['password'])
                    myextndusr =   Extendmyuser(companyname=row["company"],approval=row['approval'], user=crt) 
                    myextndusr.save()
                    print(myextndusr)
            return render(request,"novadmin_credentialtools.html",{'msg':"all credentials created"}) 
        else:  
            print("user is employe")         
    else:
        return render(request,"novadmin_credentialtools.html")


def suportmng(request):
    if request.user.is_authenticated:
        id =request.GET.get('data')
        gandalf = Techsupport.objects.filter(id=id)
        for pretoria in gandalf:
            tskstrt = pretoria.starttime
            tskend = pretoria.endtime
            taktotal = pretoria. totaltime
            tstatus = pretoria.status
        if request.method=="POST":
            wat = request.POST["slctprcs"]
            if wat == "Processing":
                if tstatus == wat:
                    mymsg = "you cannot update something as Processing which is already in Processing status"
                    return render(request,"managemysuport.html",{"gandalf":gandalf,"mymsg":mymsg})
                else:
                    m = str(datetime.now().time())
                    l = m[0:8]
                    souran = Techsupport.objects.filter(id=id).update(status=wat,starttime=l)
                    mouran = Techsupport.objects.filter(id=id,intialflg="False").update(intial_starttime=l,intialflg="True")
                    return redirect("empdashboard")

            elif wat=="Resolved":
                if tstatus == "Pending":
                    mymsg = "you cannot update something directly as Resolved with out processing"
                    return render(request,"managemysuport.html",{"gandalf":gandalf,"mymsg":mymsg})
                else:    
                    m = str(datetime.now().time())
                    l = m[0:8]
                    
                
                    souran = Techsupport.objects.filter(id=id).update(status=wat,endtime=l)
                    mouran = Techsupport.objects.filter(id=id,currentendflg="False").update(current_endtime=l,currentendflg="True")
                    return redirect("empdashboard")

            elif wat=="Pending":
                if  tstatus == "Pending":
                    mymsg = "you cannot update something which is already in Pending status"
                    return render(request,"managemysuport.html",{"gandalf":gandalf,"mymsg":mymsg})
                else:
                    m = str(datetime.now().time())
                    l = m[0:8]
                    FMT = '%H:%M:%S'
                    
                    if taktotal == None:
                        tdelta = datetime.strptime(l, FMT) - datetime.strptime(tskstrt, FMT)
                        essr = str(tdelta)   
                        souran = Techsupport.objects.filter(id=id).update(status=wat,endtime=l,totaltime=essr)
                        mouran = Techsupport.objects.filter(id=id,currentendflg="False").update(current_endtime=l,currentendflg="True")  
                        return redirect("empdashboard")     
                    else:  
                        tdelta = datetime.strptime(l, FMT) - datetime.strptime(tskstrt, FMT)
                        essr = str(tdelta)
                        dump = datetime.strptime('00:00:00', '%H:%M:%S')
                        alpha = datetime.strptime(taktotal, FMT)
                        beta = datetime.strptime(essr, FMT)
                        zeta = (alpha - dump + beta).time()
                        souran = Techsupport.objects.filter(id=id).update(status=wat,totaltime=str(zeta))
                        mouran = Techsupport.objects.filter(id=id,currentendflg="False").update(current_endtime=l,currentendflg="True")
                        return redirect("empdashboard")


            
        return render(request,"managemysuport.html",{"gandalf":gandalf})
    else:
        return redirect("emplogin")
        
def empchk(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        amd = Empuser.objects.all()
        
        return render(request,"novaemp.html",{"amd":amd})
    else:
        return redirect("novaadmin")

def timesheet(request):
    if request.user.is_authenticated:
        pse = Mysupport.objects.all()
        cmpfill = Company.objects.all()
        #empfill = Empuser.objects.all()
       

        if request.method=="POST":
            dtfltr = request.POST["fdate"]
            #dtfltr2 = request.POST["tdate"]
            
            slstat = request.POST["slctprcs"]
            slclnt = request.POST["slctclnt"]
            
            d = dtfltr[8:10]
            m = dtfltr[5:7]
            y = dtfltr[0:4]
            epson = "{}-{}-{}".format(d,m,y)
           
            
            
            if slclnt == "all":
              
                pse =  Mysupport.objects.filter(empsprfct=epson,sstatus=slstat)  or Mysupport.objects.filter(empsprfct=epson) or Mysupport.objects.filter(sstatus=slstat) or Mysupport.objects.filter(empcmp=slclnt)   or Mysupport.objects.all() 
                #pse = Mysupport.objects.filter(empsprfct=epson) or Mysupport.objects.filter(sstatus=slstat) or Mysupport.objects.filter(empcmp=slclnt) 
                return render(request,"nova_timesheet.html",{'pse':pse,'cmpfill':cmpfill})
            else:
                pse = Mysupport.objects.filter(empsprfct=epson,sstatus=slstat,empcmp=slclnt) or Mysupport.objects.filter(empsprfct=epson,sstatus=slstat) or Mysupport.objects.filter(empsprfct=epson,empcmp=slclnt) or Mysupport.objects.filter(sstatus=slstat,empcmp=slclnt) or Mysupport.objects.filter(empsprfct=epson) or Mysupport.objects.filter(sstatus=slstat) or Mysupport.objects.filter(empcmp=slclnt) 
                return render(request,"nova_timesheet.html",{'pse':pse,'cmpfill':cmpfill})
           

        else:
            

            return render(request,"nova_timesheet.html",{'pse':pse,'cmpfill':cmpfill})  

        
    else:

        return redirect("novaadmin")

def emptimesheet(request):
    if request.user.is_authenticated:
        cmpfill = Company.objects.all()
        pse = Mysupport.objects.filter(empallot=request.user)
        if request.method=="POST":
            dtfltr = request.POST["fdate"]
            dtfltr2 = request.POST["tdate"]
            slstat = request.POST["slctprcs"]
            slclnt = request.POST["slctclnt"]
            
            d = dtfltr[8:10]
            m = dtfltr[5:7]
            y = dtfltr[0:4]
            epson = "{}-{}-{}".format(d,m,y)
           
            
           

            if slclnt == "all":
                
                pse =  Mysupport.objects.filter(empsprfct=epson,empallot=request.user,sstatus=slstat)  or Mysupport.objects.filter(empallot=request.user,empsprfct=epson) or Mysupport.objects.filter(empallot=request.user,sstatus=slstat) or Mysupport.objects.filter(empallot=request.user,empcmp=slclnt) 
            #pse = Mysupport.objects.filter(empsprfct=epson) or Mysupport.objects.filter(sstatus=slstat) or Mysupport.objects.filter(empcmp=slclnt) 
                return render(request,"nova_timesheet.html",{'pse':pse,'cmpfill':cmpfill})
            else:
                pse = Mysupport.objects.filter(empsprfct=epson,empallot=request.user,sstatus=slstat,empcmp=slclnt) or Mysupport.objects.filter(empsprfct=epson,empallot=request.user,sstatus=slstat) or Mysupport.objects.filter(empsprfct=epson,empallot=request.user,empcmp=slclnt) or Mysupport.objects.filter(sstatus=slstat,empallot=request.user,empcmp=slclnt) or Mysupport.objects.filter(empallot=request.user,empsprfct=epson) or Mysupport.objects.filter(empallot=request.user,sstatus=slstat) or Mysupport.objects.filter(empallot=request.user,empcmp=slclnt) 
                return render(request,"nova_timesheet.html",{'pse':pse,'cmpfill':cmpfill})
            
           
        else:
            

            return render(request,"nova_emptimesheet.html",{'pse':pse,'cmpfill':cmpfill})                 

        
    else:

        return redirect("emplogin")


def exporttime(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachment; filename=statusreport.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    row_num = 0
    font_style= xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Date','Developer','Project','Type','Program','Start time','End time','Time Taken -(HH:MM:SS) ','Status']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Mysupport.objects.all().values_list('empsdate','empallot','empcmp','stype','empssdetail','intialtime','endtimecurrent','emptotaltime','sstatus')

    for row in rows:
        row_num += 1 

        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    
    wb.save(response)
    
    #C:\Users\Ibiza\Downloads
    return response



        
        
        

        




