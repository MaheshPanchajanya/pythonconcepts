from typing import Sized
from django.core import mail
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Categories, Myorder,Potsmfg,Ads,About,Feed,Sliderabt, Special1,Special3,Pricelist
from django.contrib.auth.models import User, auth
from django.db.models import Sum
from django.contrib import messages
from django.core.mail import send_mail


def  index(request):
    if  request.GET.get("data"):
        slut = request.GET.get("data")
        sitwrap =  Potsmfg.objects.filter(category=slut)
        cato = Categories.objects.all()
        adsobj = Ads.objects.all()
        ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
        spc = Special3.objects.all()
        spc1 = Special1.objects.all()
        karto = Myorder.objects.filter(user=request.user,mailflag="false")
        totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
        finalprice =  totlkart['totalprice__sum']
        objs = {'cato':cato,'adsobj':adsobj,'sitwrap':sitwrap,'spc':spc,'spc1':spc1,'ordr':ordr,'karto':karto,'finalprice':finalprice}
        return render(request,"index_pottery.html",objs)
    
    else:

        cato = Categories.objects.all()
        adsobj = Ads.objects.all()
        sitwrap = Potsmfg.objects.all() 
        ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
        spc = Special3.objects.all()
        spc1 = Special1.objects.all()
        karto = Myorder.objects.filter(user=request.user,mailflag="false")
        totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
        finalprice =  totlkart['totalprice__sum']
        objs = {'cato':cato,'adsobj':adsobj,'sitwrap':sitwrap,'spc':spc,'spc1':spc1,'ordr':ordr,'karto':karto,'finalprice':finalprice}
        return render(request,"index_pottery.html",objs)
    
def view_category(request):
    #if request.user.is_authenticated:
    encounterpot = request.GET.get('data')
    cat1= Categories.objects.all()
    ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
    plist = Pricelist.objects.filter(pid=encounterpot)
    karto = Myorder.objects.filter(user=request.user,mailflag="false")
    totlkart = Myorder.objects.filter(user=request.user).aggregate(Sum('totalprice'))
    finalprice =  totlkart['totalprice__sum']
    
    

    if "sizo" in request.POST:

        lt = request.POST["sizo"]
         
        sitwrap = Potsmfg.objects.filter(id=encounterpot)
        slist = Pricelist.objects.filter(pid=encounterpot,size=lt) 
        
        
        
       

        return render(request,"viewcategory_potterycrafts.html",{'cato':cat1,'sitwrap':sitwrap,'plist':plist,'slist':slist,'ordr':ordr,'karto':karto,'finalprice':finalprice})

    elif "belly" in request.POST:
        if request.user.is_authenticated:

            ppl = request.user
            ptname = request.POST["potname"]
            catmgery = request.POST["category"]
            iq = request.POST["sap"]
            qos = request.POST["qty"]
            soz = request.POST.get("size")
            bse = request.POST.get("baseprice")
            
            #iq = request.FILES["sap"]
            sub = request.POST["totl"]
            if soz == None or qos == None:
                sitwrap = Potsmfg.objects.filter(id=encounterpot)
            #plist = Pricelist.objects.filter(pid=encounterpot)
                qco = "select quantity and size to add to Kart"
                return render(request,"viewcategory_potterycrafts.html",{'cato':cat1,'sitwrap':sitwrap,'plist':plist,'ordr':ordr,'karto':karto,'finalprice':finalprice,'qco':qco})
                #return render("index")
            else:    
                smr = Myorder.objects.create(user=ppl,name=ptname,category=catmgery,size=soz,quantity=qos,baseprice=bse,kartimg=iq,totalprice=sub)
                return redirect("index")    
        else:
            cato = Categories.objects.all()
            adsobj = Ads.objects.all()
            sitwrap = Potsmfg.objects.all()
            ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
            spc = Special3.objects.all()
            spc1 = Special1.objects.all()
            karto = Myorder.objects.filter(user=request.user,mailflag="false")
            totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
            finalprice =  totlkart['totalprice__sum']
            taco = "signin to add to kart and place order"
            objs = {'cato':cato,'adsobj':adsobj,'sitwrap':sitwrap,'spc':spc,'spc1':spc1,'ordr':ordr,'karto':karto,'finalprice':finalprice,'taco':taco}
            return render(request,"index_pottery.html",objs)
            #return redirect("index")
    else:    
        
        cat1= Categories.objects.all()
        encounterpot = request.GET.get('data')
        
   # adsobj = Ads.objects.all()
        if  Potsmfg.objects.filter(id=encounterpot).exists():
            sitwrap = Potsmfg.objects.filter(id=encounterpot)
            #plist = Pricelist.objects.filter(pid=encounterpot)
           
            return render(request,"viewcategory_potterycrafts.html",{'cato':cat1,'sitwrap':sitwrap,'plist':plist,'ordr':ordr,'karto':karto,'finalprice':finalprice})
        else:
            cat1= Categories.objects.all()
           # plist = Pricelist.objects.filter(pid=encounterpot)
            
            return render(request,"viewcategory_potterycrafts.html",{'cato':cat1,'plist':plist,'ordr':ordr,'karto':karto,'finalprice':finalprice})

def special(request):
    cat1 = Categories.objects.all()
    episode =request.GET.get('data')
    ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
   
    karto = Myorder.objects.filter(user=request.user,mailflag="false")
    totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
    finalprice =  totlkart['totalprice__sum']
    if request.method=="POST":
        if request.user.is_authenticated:

            potname=request.POST["potname"]
            
            qos = request.POST["qty"]
            size = request.POST.get("size")
            baseprice = request.POST.get("baseprice")
            totalprice = request.POST["totalprice"]
            img = request.POST["imgshot"]
            print(size)
            print(qos)
            if qos == "" or qos == "Quantity":
                qco = "select quantity and size to add to Kart"
                sitwrap = Special1.objects.filter(id=episode)
                return render(request,"specialview.html",{'cato':cat1,'sitwrap':sitwrap,'ordr':ordr,'karto':karto,'finalprice':finalprice,'qco':qco})
            else:    
                crt = Myorder.objects.create(user=request.user,name=potname,size=size,quantity=qos,baseprice=baseprice,totalprice=totalprice,kartimg=img)    
                return redirect("index")
        else:
            cato = Categories.objects.all()
            adsobj = Ads.objects.all()
            sitwrap = Potsmfg.objects.all()
            ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
            spc = Special3.objects.all()
            spc1 = Special1.objects.all()
            karto = Myorder.objects.filter(user=request.user,mailflag="false")
            totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
            finalprice =  totlkart['totalprice__sum']
            taco = "signin to add to kart and place order"
            objs = {'cato':cato,'adsobj':adsobj,'sitwrap':sitwrap,'spc':spc,'spc1':spc1,'ordr':ordr,'karto':karto,'finalprice':finalprice,'taco':taco}
            return render(request,"index_pottery.html",objs)    
    else:
        
        if Special1.objects.filter(id=episode).exists():
        
            sitwrap = Special1.objects.filter(id=episode)
            return render(request,"specialview.html",{'cato':cat1,'sitwrap':sitwrap,'ordr':ordr,'karto':karto,'finalprice':finalprice})
        
        else:
            cat1= Categories.objects.all()
            return render(request,"specialview.html",{'cato':cat1,'ordr':ordr,'karto':karto,'finalprice':finalprice})

    
def special2(request):
    cat1 = Categories.objects.all()
    episode =request.GET.get('vendata')
    ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
   
    karto = Myorder.objects.filter(user=request.user,mailflag="false")
    totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
    finalprice =  totlkart['totalprice__sum']
    if request.method=="POST":
        if request.user.is_authenticated:

            potname=request.POST["potname"]
            
            qos = request.POST["qty"]
            size = request.POST.get("size")
            baseprice = request.POST.get("baseprice")
            totalprice = request.POST["totalprice"]
            img = request.POST["imgshot"]
            if qos == "" or qos == "Quantity":
                qco = "select quantity and size to add to Kart"
                sitwrap = Special3.objects.filter(id=episode)
                return render(request,"specialviewtwo.html",{'cato':cat1,'sitwrap':sitwrap,'ordr':ordr,'karto':karto,'finalprice':finalprice,'qco':qco})
            else:
                crt = Myorder.objects.create(user=request.user,name=potname,size=size,quantity=qos,baseprice=baseprice,totalprice=totalprice,kartimg=img)    
                return redirect("index")
        else:
            cato = Categories.objects.all()
            adsobj = Ads.objects.all()
            sitwrap = Potsmfg.objects.all()
            ordr = Myorder.objects.filter(user=request.user,mailflag="false").count()
            spc = Special3.objects.all()
            spc1 = Special1.objects.all()
            karto = Myorder.objects.filter(user=request.user,mailflag="false")
            totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
            finalprice =  totlkart['totalprice__sum']
            taco = "signin to add to kart and place order"
            objs = {'cato':cato,'adsobj':adsobj,'sitwrap':sitwrap,'spc':spc,'spc1':spc1,'ordr':ordr,'karto':karto,'finalprice':finalprice,'taco':taco}
            return render(request,"index_pottery.html",objs)    
    else:
        
        if Special3.objects.filter(id=episode).exists():
        
            sitwrap = Special3.objects.filter(id=episode)
            return render(request,"specialviewtwo.html",{'cato':cat1,'sitwrap':sitwrap,'ordr':ordr,'karto':karto,'finalprice':finalprice})
        
        else:
            cat1= Categories.objects.all()
            return render(request,"specialviewtwo.html",{'cato':cat1,'ordr':ordr,'karto':karto,'finalprice':finalprice})  
            

               
   
def contact_dealer(request):
    return render(request,"sitemap.html")
    

        
    


def about_potterycrafts(request):
    abt = About.objects.all()
    ionhead = Sliderabt.objects.all()
    ibjfrab = {'abt':abt,'ionhead':ionhead}
    return render(request,"about_potterycrafts.html",ibjfrab)

def potteryfeeds(request):
    cato = Categories.objects.all()
    mfc = Feed.objects.all()
   
    cmb = {'cato':cato,'mfc':mfc}
    #return render(request,"pottery_blogs.html",cmb)
    if  request.method == "POST":
        fname = request.POST['fname']
        phone = request.POST['phone']
        email = request.POST['email']
        sandesh = request.POST['message']
            
            #send mail
        try:
            send_mail(
                "PotteryCrafts_Customer"+" "+" "+fname+" "+"phno:" +"  "+ phone,
                sandesh,
                email,
                ['potterycrafts33@gmail.com'],
                fail_silently=False,

            )
            mesiah = "Thanks for Sending us an enquiry ! we will revert back you soon"
            return render(request,"pottery_blogs.html",{'cato':cato,'mfc':mfc,'mesiah':mesiah})
        except:
            messages.info(request,"invalid email")
            return redirect('/')    

    else:
        return render(request,"pottery_blogs.html",cmb)

def removeordr(request):
    sp = request.GET.get("vendata")
    query = Myorder.objects.filter(user=request.user,id=sp).delete()
    return redirect("index")

def quotechk(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            phno = request.POST["phno"]
            email = request.POST["email"]
            address1 = request.POST["Address1"]
            address2 = request.POST["Address2"]
            city = request.POST["city"]
            pin = request.POST["pin"]
            state =  request.POST["state"]
            
            
            karto = Myorder.objects.filter(user=request.user).update(mailflag="true")
            #except:
            #    print("error")
            karto = Myorder.objects.filter(user=request.user).update(phno=phno,Email=email,address1=address1,address2=address2,city=city,pincode=pin,state=state)    
            

            
            msg = "Thank you for sending your order soon we will get back to you"
            return render(request,"quote.html",{'msg':msg})
            
        else:    
            karto = Myorder.objects.filter(user=request.user,mailflag="false")
            totlkart = Myorder.objects.filter(user=request.user,mailflag="false").aggregate(Sum('totalprice'))
            finalprice =  totlkart['totalprice__sum']
            return render(request,"quote.html",{'karto':karto,'finalprice':finalprice})
    else:
        return redirect("index")

   
