
import json
from django import http
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse, request
from . models import Company, Daybook, Techsupport
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from users.models import Empuser, Extendmyuser,Phoneofclnt
#from . models import Company
import mysql.connector
import pandas as pd
from xml.etree import ElementTree as Et
#from pandas import Index 
import requests
from datetime import datetime, timedelta
from django.core.mail import send_mail


#------------- index ------------#

def index(request):
    comp = Company.objects.all()
   # print(comp)
    return render(request,"index.html",{'comp':comp})

#----------------------------------#    

#---------- for nova support-----------#
def support(request):
    global  myid 
    myid = request.GET.get("data")
    global profile 
    s = request.user.is_active
    print(s)
    #phn =  Phoneofclnt.objects.filter(ussr=myid)
    profile = Extendmyuser.objects.filter(user_id=myid)
    mailman = User.objects.filter(id=myid)
    
    for m in mailman:
        submail = m.email
    global  saphire 
    saphire = ""                                                                                
    for x in profile:
           
        saphire =  x.companyname
      #  print(saphire)
    #/enfor 
        
    global cognizent
    cognizent = Company.objects.filter(companyname=saphire)
    phn =  Phoneofclnt.objects.filter(ussr=myid)
    sctr = datetime.now()
    ltr = datetime.today().strftime('%d-%m-%Y')
    
    
    if request.method == "POST":
        

        dexter = request.POST["cpname"]
        fenkin = request.POST["ussr"]
        doron = request.POST["mrscode"]
        boas = request.POST["slctprdt"]
        ayub = request.POST["issue"]
        steve = request.FILES["fino"]
        perid = request.POST["isdate"]
        currenttime = datetime.now()+timedelta(minutes=2)

        #smr = perid.replace("-","/")
        #avg = smr[5:15]
        mosul = Techsupport.objects.create(sdate=perid,scmp=dexter,suser=fenkin,sphno=doron,sprdt=boas,sdetail=ayub,screenshot=steve,st=currenttime)
       
        gaza = mosul.id
        
        past = "06:30 PM"
        wah = "09:30 AM"
        leave = "sunday"
        weekday = datetime.today().strftime('%A')
        rap = datetime.now().strftime("%I:%M %p")
        if datetime.strptime(rap, "%I:%M %p") <= datetime.strptime(wah, "%I:%M %p") or datetime.strptime(rap, "%I:%M %p") >= datetime.strptime(past, "%I:%M %p") and leave!=weekday:
            sms = "Issue has been submited  it will be processed next working day \n"+"your ticket number is :{}".format(gaza)
            return render(request,"support.html",{'cognizent':cognizent,'ltr':ltr,'sms':sms,'phn':phn})
        else:
            msg = "Issue has been submited sit tight while we process \n"+"your ticket number is :{}".format(gaza)
            return render(request,"support.html",{'cognizent':cognizent,'ltr':ltr,'msg':msg,'phn':phn})

        #return JsonResponse({'msg':msg},safe=False)
    else:
        if request.user.is_authenticated:
           
            return render(request,"support.html",{'cognizent':cognizent,'ltr':ltr,'phn':phn})
        else:
            return redirect("login")
#----------------------------------------#

#------ customermodule -----------------#

def customer(request):
    if request.user.is_authenticated:

        global  myid 
        myid = request.GET.get('data')
        global profile 
        s = request.user.is_active
        print(s)

        profile = Extendmyuser.objects.filter(user_id=myid)
        for x in profile:
            global  saphire 
            saphire =  x.companyname
      #  print(saphire)
    #/enfor 
        global cognizent
        cognizent = Company.objects.filter(companyname=saphire)
    #print(cognizent)
        return render(request,"nova_customer.html",{'cognizent':cognizent})
    else:
        return redirect("login")

def dashboard(request):
    if request.method == "POST":
        frmdate = request.POST["frm"]
        todate = request.POST["ta"]
        print(frmdate)
        print(todate)
        xml = "<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>DATA</TYPE><ID>DayBook</ID>"
        xml += "</HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT><SVFROMDATE TYPE='DATE'>"
        xml += frmdate + "</SVFROMDATE><SVTODATE TYPE='DATE'>" + todate + "</SVTODATE></STATICVARIABLES></DESC></BODY></ENVELOPE>"
        daybook_res = get_data(xml)
        amount = 0
        for vch in daybook_res.findall("./BODY/DATA/TALLYMESSAGE/VOUCHER"):
            
            if len(vch.findall("ALLLEDGERENTRIES.LIST")) == 0:
                amount = vch.findall("LEDGERENTRIES.LIST").__getitem__(0).find("AMOUNT").text
            else:
                amount = vch.findall("ALLLEDGERENTRIES.LIST").__getitem__(0).find("AMOUNT").text
            
            dt = format_date(vch.find("DATE").text)
            #print(vch.find("DATE").text)
            print(dt)
            vctyp = vch.find("VOUCHERTYPENAME").text
            #print(vch.find("VOUCHERTYPENAME").text)
            print(vctyp)
            vcnum = vch.find("VOUCHERNUMBER").text
            #print(vch.find("VOUCHERNUMBER").text)
            print(vcnum)
            prty = vch.find("PARTYLEDGERNAME").text
            #print(vch.find("PARTYLEDGERNAME").text)
            print(prty)
            amt = format_amount(float(amount))
            print(amt)
            cont = Daybook.objects.create(date=dt,vouchertype=vctyp,vouchernumber=vcnum,partyledger=prty,amount=amt)
            
            #cont = {"dt":dt,"vctyp":vctyp,"vcnum":vcnum,"prty":prty,"amt":amt}
        fauda=Daybook.objects.all()
        laprus = []
        for x in fauda:
            silverfox = x.partyledger
            firefox =  float(x.amount)
            laprus.append([silverfox,firefox])

        return render(request,"test.html",{"fauda":fauda,"laprus":laprus})
        
    else:
        masod = Daybook.objects.all().delete()
        return render(request,"test.html")

def format_amount(amt):
    if amt < 0:
        return str(amt * (-1)) 

    return str(amt) 

def get_data(payload):
        req = requests.get(url="http://localhost:9000", data=payload)
        res = req.text.encode("UTF-8")
        return Et.fromstring(res)    

def format_date(date):
        return date[6:8] + "-" + date[4:6] + "-" + date[0:4]
#--------- nova uploads ---------------#

def uploads(request):
    if  request.method == "POST":
        filename= request.FILES["filename"]
        hname = request.POST["hname"]
        port =  request.POST["port"] 
        print(filename)
        link='http://{}:{}'.format(hname,port)
        print(link)
        data = pd.read_excel(filename)
         
        #perc=100/len(data)
        url = link
        typeof = request.POST["typein"]
        
        if typeof == "Sales":
           
            try:
            
                for index, row in data.iterrows():
                    data = '<ENVELOPE>'
                    data += '<HEADER>'
                    data += '<TALLYREQUEST>Import Data</TALLYREQUEST>'
                    data += '</HEADER>'
                    data += '<BODY>'
                    data += '<IMPORTDATA>'
                    data += '<REQUESTDESC>'
                    data += '<REPORTNAME>Vouchers</REPORTNAME>'
                    data += '</REQUESTDESC>'
                    data += '<REQUESTDATA>'
                    data += '<TALLYMESSAGE xmlns:UDF="TallyUDF">'
                    data += '<VOUCHER ACTION="Create">'
                    data += '<DATE>'+str(row['VCHDate'])+'</DATE>'
                    data += '<PARTYNAME>'+row['PARTYLEDERNAME']+'</PARTYNAME>'
                    data += '<PARTYLEDGERNAME>'+row['PARTYLEDERNAME']+'</PARTYLEDGERNAME>'
                    data += '<VOUCHERTYPENAME>'+row['VOUCHERTYPE']+'</VOUCHERTYPENAME>'
                    data += '<VOUCHERNUMBER>'+str(row['VCHNO'])+'</VOUCHERNUMBER>'
                    data += '<PERSISTEDVIEW>Invoice Voucher View</PERSISTEDVIEW>'
                    data += '<VCHENTRYMODE>Item Invoice</VCHENTRYMODE>'
                    data += '<ISINVOICE>Yes</ISINVOICE>'
                    data += '<ALLINVENTORYENTRIES.LIST>'
                    data += '<STOCKITEMNAME>'+row['ITEMNAME']+'</STOCKITEMNAME>'
                    data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                    data += '<RATE>'+str(row['RATE'])+'/nos</RATE>'
                    data += '<AMOUNT>'+str(row['Amount'])+'</AMOUNT>'
                    data += '<ACTUALQTY>'+str(row['QTY'])+'nos</ACTUALQTY>'
                    data += '<BILLEDQTY>'+str(row['QTY'])+'nos</BILLEDQTY>'
                    data += '<BATCHALLOCATIONS.LIST>'
                    data += '<GODOWNNAME>'+row['Godown']+'</GODOWNNAME>'
                    data += '<AMOUNT>'+str(row['Amount'])+'</AMOUNT>'
                    data += '<ACTUALQTY>'+str(row['QTY'])+'nos</ACTUALQTY>'
                    data += '<BILLEDQTY>'+str(row['QTY'])+'nos</BILLEDQTY>'
                    data += '</BATCHALLOCATIONS.LIST>'
                    data += '<ACCOUNTINGALLOCATIONS.LIST>'
                    data += '<LEDGERNAME>'+row['LEDGERNAME']+'</LEDGERNAME>'
                    data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                    data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                    data += '<AMOUNT>'+str(row['Amount'])+'</AMOUNT>'
                    data += '</ACCOUNTINGALLOCATIONS.LIST>'
                    data += '</ALLINVENTORYENTRIES.LIST>'
                    data += '<LEDGERENTRIES.LIST>'
                    data += '<LEDGERNAME>'+row['PARTYLEDERNAME']+'</LEDGERNAME>'
                    data += '<ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>'
                    data += '<ISPARTYLEDGER>Yes</ISPARTYLEDGER>'
                    data += '<ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE>'
                    data += '<AMOUNT>'+'-'+str(row['TotalAmount'])+'</AMOUNT>'
                    data += '</LEDGERENTRIES.LIST>'
                    data += '<LEDGERENTRIES.LIST>'
                    data += '<BASICRATEOFINVOICETAX.LIST TYPE="Number">'
                    data += '<BASICRATEOFINVOICETAX>'+str(row['SGSTrate'])+'</BASICRATEOFINVOICETAX>'
                    data += '</BASICRATEOFINVOICETAX.LIST>'
                    data += '<LEDGERNAME>'+row['SGST']+'</LEDGERNAME>'
                    data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                    data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                    data += '<AMOUNT>'+str(row['SGSTamount'])+'</AMOUNT>'
                    data += '</LEDGERENTRIES.LIST>'
                    data += '<LEDGERENTRIES.LIST>'
                    data += '<BASICRATEOFINVOICETAX.LIST TYPE="Number">'
                    data += '<BASICRATEOFINVOICETAX>'+str(row['CGSTrate'])+'</BASICRATEOFINVOICETAX>'
                    data += '</BASICRATEOFINVOICETAX.LIST>'
                    data += '<LEDGERNAME>'+str(row['CGST'])+'</LEDGERNAME>'
                    data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                    data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                    data += '<AMOUNT>'+str(row['CGSTamount'])+'</AMOUNT>'
                    data += '</LEDGERENTRIES.LIST>'
                    data += '</VOUCHER>'
                    data += '</TALLYMESSAGE>'
                    data += '</REQUESTDATA>'
                    data += '</IMPORTDATA>'
                    data += '</BODY>'
                    data += '</ENVELOPE>'
                    req = requests.post(url=url, data=data)
                   
                    
               

                success="Sales Records imported sucessfully"
                #return HttpResponse("Uploaded")
                return render(request,"nova_uploads.html",{'success':success,'cognizent':cognizent})

            except:
                conn = "make sure Tally Prime/ERP is opened"
                return render(request,"nova_uploads.html",{'conn':conn})

        elif request.POST["typein"]=="Ledger":
            try:
                for index, row in data.iterrows():
                    data =  '<ENVELOPE><HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER><BODY>'
                    data += '<IMPORTDATA><REQUESTDESC><REPORTNAME>All Masters</REPORTNAME></REQUESTDESC><REQUESTDATA>'
                    data += '<TALLYMESSAGE xmlns:UDF="TallyUDF"><LEDGER Action="Create"><NAME>'+row['name']+'</NAME><PARENT>'+row['group']
                    data += '</PARENT><ADDRESS>'+row['address']+'</ADDRESS><COUNTRYOFRESIDENCE>'+row['country']+'</COUNTRYOFRESIDENCE>'
                    data += '<LEDSTATENAME>'+row['province']+'</LEDSTATENAME><LEDGERMOBILE>'+str(row['mobile number'])+'</LEDGERMOBILE><PARTYGSTIN>'
                    data += str(row['gst'])+'</PARTYGSTIN></LEDGER></TALLYMESSAGE></REQUESTDATA></IMPORTDATA></BODY></ENVELOPE>'
                    req = requests.post(url=url, data=data)
                
                
                   
                success="Ledgers imported successfully"
                return render(request,"nova_uploads.html",{'success':success,'cognizent':cognizent})

            except:
                conn = "make sure Tally Prime/ERP is opened"
                return render(request,"nova_uploads.html",{'conn':conn})
                
        elif request.POST["typein"]=="Stock item":
            try:
                for index, row in data.iterrows():
                    data = '<ENVELOPE><HEADER><TALLYREQUEST>Import Data</TALLYREQUEST></HEADER><BODY><IMPORTDATA><REQUESTDESC><REPORTNAME>All Masters</REPORTNAME></REQUESTDESC><REQUESTDATA>';
                    data += '<TALLYMESSAGE xmlns:UDF="TallyUDF"><STOCKITEM Action="Create"><NAME>' + row['ITEMNAME'] + '</NAME><BASEUNITS>' + row['UNITS'] + '</BASEUNITS><OPENINGBALANCE>' + str(row['opening balance']) + '</OPENINGBALANCE>'
                    data += '<GSTAPPLICABLE>&#4;Applicable</GSTAPPLICABLE><GSTDETAILS.LIST><APPLICABLEFROM>20170701</APPLICABLEFROM><CALCULATIONTYPE>On Value</CALCULATIONTYPE><HSNCODE>' + str(row['HSN']) + '</HSNCODE>'
                    data += '<TAXABILITY>Taxable</TAXABILITY><STATEWISEDETAILS.LIST><STATENAME>&#4; Any</STATENAME><RATEDETAILS.LIST><GSTRATEDUTYHEAD>Central Tax</GSTRATEDUTYHEAD>'
                    data += '<GSTRATEVALUATIONTYPE>Based on Value</GSTRATEVALUATIONTYPE><GSTRATE>' + str(row['GST'] / 2) + '</GSTRATE></RATEDETAILS.LIST><RATEDETAILS.LIST><GSTRATEDUTYHEAD>State Tax</GSTRATEDUTYHEAD>'
                    data += '<GSTRATEVALUATIONTYPE>Based on Value</GSTRATEVALUATIONTYPE><GSTRATE>' + str(row['GST'] / 2) + '</GSTRATE></RATEDETAILS.LIST><RATEDETAILS.LIST><GSTRATEDUTYHEAD>Integrated Tax</GSTRATEDUTYHEAD>'
                    data += '<GSTRATEVALUATIONTYPE>Based on Value</GSTRATEVALUATIONTYPE><GSTRATE>' + str(row['GST']) + '</GSTRATE></RATEDETAILS.LIST><RATEDETAILS.LIST><GSTRATEDUTYHEAD>Cess</GSTRATEDUTYHEAD>'
                    data += '<GSTRATEVALUATIONTYPE>Based on Value</GSTRATEVALUATIONTYPE></RATEDETAILS.LIST></STATEWISEDETAILS.LIST></GSTDETAILS.LIST></STOCKITEM></TALLYMESSAGE></REQUESTDATA>'
                    data += '</IMPORTDATA></BODY></ENVELOPE>'
                    req = requests.post(url=url, data=data)
                
               
                success="Stock item imported successfully"
                return render(request,"nova_uploads.html",{'success':success,'cognizent':cognizent})
            except:
                conn = "make sure Tally Prime/ERP is opened"
                return render(request,"nova_uploads.html",{'conn':conn})      
    else:
        if request.user.is_authenticated:
            
            return render(request,"nova_uploads.html",{'cognizent':cognizent})
        else:
            return redirect("login")#global  myid 
        
            
def any(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            typeof = request.POST["typein"]
            
            if typeof == "Mysql Server":
                try:
                    global mydb 
                    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="tallyprime",auth_plugin='mysql_native_password')
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM sales")
                    myresult = mycursor.fetchall()
                    
                    url = 'http://localhost:9000'

                    for x in myresult:
                        data = '<ENVELOPE>'
                        data += '<HEADER>'
                        data += '<TALLYREQUEST>Import Data</TALLYREQUEST>'
                        data += '</HEADER>'
                        data += '<BODY>'
                        data += '<IMPORTDATA>'
                        data += '<REQUESTDESC>'
                        data += '<REPORTNAME>Vouchers</REPORTNAME>'
                        data += '</REQUESTDESC>'
                        data += '<REQUESTDATA>'
                        data += '<TALLYMESSAGE xmlns:UDF="TallyUDF">'
                        data += '<VOUCHER ACTION="Create">'
                        data += '<DATE>'+str(x[0])+'</DATE>'
                        data += '<PARTYNAME>'+x[2]+'</PARTYNAME>'
                        data += '<PARTYLEDGERNAME>'+x[2]+'</PARTYLEDGERNAME>'
                        data += '<VOUCHERTYPENAME>'+x[4]+'</VOUCHERTYPENAME>'
                        data += '<VOUCHERNUMBER>'+str(x[1])+'</VOUCHERNUMBER>'
                        data += '<PERSISTEDVIEW>Invoice Voucher View</PERSISTEDVIEW>'
                        data += '<VCHENTRYMODE>Item Invoice</VCHENTRYMODE>'
                        data += '<ISINVOICE>Yes</ISINVOICE>'
                        data += '<ALLINVENTORYENTRIES.LIST>'
                        data += '<STOCKITEMNAME>'+x[5]+'</STOCKITEMNAME>'
                        data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                        data += '<RATE>'+str(x[7])+'/nos</RATE>'
                        data += '<AMOUNT>'+str(x[8])+'</AMOUNT>'
                        data += '<ACTUALQTY>'+str(x[6])+'nos</ACTUALQTY>'
                        data += '<BILLEDQTY>'+str(x[6])+'nos</BILLEDQTY>'
                        data += '<BATCHALLOCATIONS.LIST>'
                        data += '<GODOWNNAME>'+x[9]+'</GODOWNNAME>'
                        data += '<AMOUNT>'+str(x[8])+'</AMOUNT>'
                        data += '<ACTUALQTY>'+str(x[6])+'nos</ACTUALQTY>'
                        data += '<BILLEDQTY>'+str(x[6])+'nos</BILLEDQTY>'
                        data += '</BATCHALLOCATIONS.LIST>'
                        data += '<ACCOUNTINGALLOCATIONS.LIST>'
                        data += '<LEDGERNAME>'+x[3]+'</LEDGERNAME>'
                        data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                        data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                        data += '<AMOUNT>'+str(x[8])+'</AMOUNT>'
                        data += '</ACCOUNTINGALLOCATIONS.LIST>'
                        data += '</ALLINVENTORYENTRIES.LIST>'
                        data += '<LEDGERENTRIES.LIST>'
                        data += '<LEDGERNAME>'+x[2]+'</LEDGERNAME>'
                        data += '<ISDEEMEDPOSITIVE>Yes</ISDEEMEDPOSITIVE>'
                        data += '<ISPARTYLEDGER>Yes</ISPARTYLEDGER>'
                        data += '<ISLASTDEEMEDPOSITIVE>Yes</ISLASTDEEMEDPOSITIVE>'
                        data += '<AMOUNT>'+'-'+str(x[19])+'</AMOUNT>'
                        data += '</LEDGERENTRIES.LIST>'
                        data += '<LEDGERENTRIES.LIST>'
                        data += '<BASICRATEOFINVOICETAX.LIST TYPE="Number">'
                        data += '<BASICRATEOFINVOICETAX>'+str(x[13])+'</BASICRATEOFINVOICETAX>'
                        data += '</BASICRATEOFINVOICETAX.LIST>'
                        data += '<LEDGERNAME>'+x[10]+'</LEDGERNAME>'
                        data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                        data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                        data += '<AMOUNT>'+str(x[16])+'</AMOUNT>'
                        data += '</LEDGERENTRIES.LIST>'
                        data += '<LEDGERENTRIES.LIST>'
                        data += '<BASICRATEOFINVOICETAX.LIST TYPE="Number">'
                        data += '<BASICRATEOFINVOICETAX>'+str(x[14])+'</BASICRATEOFINVOICETAX>'
                        data += '</BASICRATEOFINVOICETAX.LIST>'
                        data += '<LEDGERNAME>'+str(x[11])+'</LEDGERNAME>'
                        data += '<ISDEEMEDPOSITIVE>No</ISDEEMEDPOSITIVE>'
                        data += '<ISPARTYLEDGER>No</ISPARTYLEDGER>'
                        data += '<AMOUNT>'+str(x[17])+'</AMOUNT>'
                        data += '</LEDGERENTRIES.LIST>'
                        data += '</VOUCHER>'
                        data += '</TALLYMESSAGE>'
                        data += '</REQUESTDATA>'
                        data += '</IMPORTDATA>'
                        data += '</BODY>'
                        data += '</ENVELOPE>'
                        req = requests.post(url=url, data=data)

                    success="Transaction imported successfully"
                    return render(request,"nova-allupload.html",{'success':success,'cognizent':cognizent})
                except:
                    conn = "make sure Tally Prime/ERP is opened"
                    return render(request,"nova-allupload.html",{'conn':conn})  
        else:
            return render(request,"nova-allupload.html",{'cognizent':cognizent})
    
def sprtupdate(request):
    secario = Techsupport.objects.filter(suser=request.user)
    return JsonResponse({'secario':list(secario.values())})