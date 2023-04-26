from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from novacustomermodule.models import Company

from . models import Extendmyuser

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['mail']
        pswd  = request.POST['pswd']
        cnfrm = request.POST['cnfrm']
        if pswd == cnfrm:
            if User.objects.filter(username=uname).exists():
                print("username taken")
                return render(request,"nova_registration.html",{'err1':"username is already registered "}) 
            
            elif User.objects.filter(email=email).exists():
                return render(request,"nova_registration.html",{'err2':"email already registered "})
                print("email registered")
               
            else:
                crt = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pswd)
                myextndusr =   Extendmyuser(companyname=request.POST["cmp"],approval="approved", user=crt) 
                myextndusr.save()
                print( myextndusr)
                return redirect("/",{'msg':"Registered sucessfully"})
                print("Registered sucessfully")

           #err1="confirm password do not match"
        else:
            return render(request,"nova_registration.html",{'err3':"password not matching"})
            print("password not matching")
    else:
        comp = Company.objects.all()
        return render(request,"nova_registration.html",{'comp':comp})
   
def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        try:
            user = auth.authenticate(username=username,password=password)
            extnprofile = Extendmyuser.objects.filter(user_id=user.id)
            
        except:
            
            strmsg = "invalid user or password"
            return render(request,"nova_login.html",{'strmsg':strmsg})

        
        try:

            for pro in extnprofile:
                jinja = pro.approval
        
            if jinja=="Enable":
                if user is not None:
                    auth.login(request, user)
                
            #id =user.id
            #print(id)
            #cmpx = Extendmyuser.objects.get(user_id=id)
            #print([cmpx.companyname])

                    return redirect("/")
               


            
                else:
                    strmsg = "username or password is invalid"
                    return render(request,"nova_login.html",{'strmsg':strmsg})
            else:
                strmsg = "user is not Activated yet please contact system admin"
                return render(request,"nova_login.html",{'strmsg':strmsg})
        except:
            
            strmsg = "sorry you are not client user to login"
            return render(request,"nova_login.html",{'strmsg':strmsg})        
    else:
        return render(request,"nova_login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
               
            
       
        

