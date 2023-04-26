from teracota.models import Myorder
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.db.models import Sum

# Create your views here.
def dboardlogin(request):
    if request.method == "POST":
        name = request.POST["email"]
        password = request.POST["pswd"]

        user = auth.authenticate(username=name,password=password)

        if User.objects.filter(username=name).exists(): 
            try:
                darlene =user.id
            
            except:
                print("user / password invalid")
                return redirect("dboardlogin")
            if user is not None:
                if User.objects.filter(id=darlene,is_superuser=True).exists():
                    auth.login(request, user)
                    return redirect("dasboard")
                else:
                    print("it is not Admin credentials")
                    return redirect("dboardlogin")
            else:
                print("username / password is invalid")
                return redirect("dboardlogin")
    else:

        return render(request,"Dashboard_login.html")

def dlogout(request):

    auth.logout(request)
    return redirect("dboardlogin")

def dasboard(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        if request.method=="POST":
            slct = request.POST["slct"]
            simen = Myorder.objects.filter(mailflag="true").values("user").distinct()
            blah = Myorder.objects.filter(user=slct,mailflag="true").values("user","phno","Email","address1","address2","city","pincode","state").distinct()
            sifa = Myorder.objects.filter(mailflag="true")
            totlkart = Myorder.objects.filter(user=slct,mailflag="true").aggregate(Sum('totalprice'))
            finalprice =  totlkart['totalprice__sum']
            return render(request,"Dashboard.html",{'blah':blah,'sifa':sifa,'simen':simen,'finalprice':finalprice})
        else:
            simen = Myorder.objects.filter(mailflag="true").values("user").distinct()
            blah = Myorder.objects.filter(mailflag="true").values("user","phno","Email","address1","address2","city","pincode","state").distinct()
            sifa = Myorder.objects.filter(mailflag="true")
            return render(request,"Dashboard.html",{'blah':blah,'sifa':sifa,'simen':simen})

def removeorder(request):
    if request.user.is_authenticated and request.user.is_superuser==True:
        amy = request.GET.get('rmv')
       
        eli = Myorder.objects.filter(user=amy).delete()
        simen = Myorder.objects.filter(mailflag="true").values("user").distinct()
        blah = Myorder.objects.filter(mailflag="true").values("user","phno","Email","address1","address2","city","pincode","state").distinct()
        sifa = Myorder.objects.filter(mailflag="true")
        return render(request,"Dashboard.html",{'blah':blah,'sifa':sifa,'simen':simen})
        
