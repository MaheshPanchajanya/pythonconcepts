from datetime import date, time,datetime,timedelta
from novaadmin.models import Mysupport
from django.http.response import HttpResponse
from django.db.models.fields import TimeField
from novacustomermodule.models import Techsupport 
from users.models import Empuser
from django.contrib.auth.models import User
from dateutil import relativedelta
import xlwt

def automate():
    past = "06:30 PM"
    wah = "09:30 AM"
    leave = "sunday"
    weekday = datetime.today().strftime('%A')   
    rap = datetime.now().strftime("%I:%M %p")
    
    ######################### Task Automation ##############################################################
    
    if datetime.strptime(rap, "%I:%M %p") <= datetime.strptime(wah, "%I:%M %p") or datetime.strptime(rap, "%I:%M %p") >= datetime.strptime(past, "%I:%M %p") or weekday == leave:
        print("Task Paused working hours is over")
    else:    
        gali =  Empuser.objects.all()
    


        for uri in gali:
            copa = uri.client
            walid = str(uri.user)
            #zaid = uri.user
            za = Techsupport.objects.filter(allot__isnull=True).count()
        
            if za > 0:
                try:

                    sync = Techsupport.objects.filter(scmp=copa).update(allot=walid)
                    snic = Empuser.objects.filter(empnamecpy=walid)
                    peter = Empuser.objects.filter(empnamecpy=walid).count()
                    for pintu in snic:
                        latin = pintu.email
                        dear = pintu.empnamecpy
                    if peter == 1:

                        try:
                            from django.core.mail import EmailMultiAlternatives

                            subject = 'status report'
                            from_email = 'novatechnosys@gmail.com'
                            to = latin
    
                            text_content = 'Dear '+dear+','+'\n'+'\n'+'Check for support  in your dashboard.'

                            message = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        #message.attach_file('C:Users/Ibiza/Downloads/statusreport.xls')
                            message.send()
                

                        except:
                            print("not sent") 
                
            
                except:
                    print("error")
    

        try:

            urvi = Techsupport.objects.filter(status__isnull=True)
    
            for sang in urvi:
                ctime = sang.st
                cid = sang.id
                x = datetime.now().time()
            
            
                if x > ctime:
                    mfine = Techsupport.objects.filter(id=cid).update(status="Escalated")
                
                    
                else:
                    print("not escalated")    
        except:
            print("not found")
   
    
        try:

            saggy = Techsupport.objects.filter(status="Escalated")
            temp = ""
            for s in saggy:
                jobid = s.id
                var = Empuser.objects.filter(status="online")
                for p in var:
                    sap = Techsupport.objects.filter(allot=str(p.user)).count()
                    if sap >= 1:
                    #print(sap)
                        print("support is not free")
                    
                    else:
                    
                        xicor = Techsupport.objects.filter(id=s.id).update(allot=str(p.user),status="Pending")
                        print(xicor)#.update(allot=str(p.user),status="Processing")


            

                    
        except:
            print("not found")

  
        try:
            axr = Empuser.objects.filter(empnamecpy__isnull=True)

            for asm in axr:
                ici = asm.id
                usr = asm.user
                up = Empuser.objects.filter(id=ici).update(empnamecpy=str(usr))
        except:
            print("")

    
        asap = Techsupport.objects.filter(status="Resolved")

        for un in asap:
            c = un.id
            time1 = un.starttime
            time2 = un.endtime
            time3 = un.totaltime
            log = un.taskclear
            
            FMT = '%H:%M:%S'
            try:
                if log==False:

                    if time3==None:

                        tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
                        essr = str(tdelta)
                        plip = Techsupport.objects.filter(id=c).update(totaltime=essr,taskclear=True)
                    else:
                        tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
                        essr = str(tdelta)
                        xuv = datetime.strptime(time3, FMT)
                        pfr = datetime.strptime(essr, FMT)
                        xlm = datetime.strptime('00:00:00',FMT)
                        delta = (xuv - xlm + pfr).time()
                    
                        plip = Techsupport.objects.filter(id=c).update(totaltime=str(delta),taskclear=True)
                else:
                    print("Task already updated")

            
           
            except:
                print("error")
    
    
    ###########################################################################################################            

    #########  Time sheet  automation #########################################################################   
     
    wah = "04:38 PM"
    rap = datetime.now().strftime("%I:%M %p")
    leave = "sunday"
    weekday = datetime.today().strftime('%A')

    if datetime.strptime(rap, "%I:%M %p") == datetime.strptime(wah, "%I:%M %p") and weekday!=leave:

        
        boston = Techsupport.objects.all()
        FMT = '%H:%M:%S'
        
        for april in boston:
            tdate = april.sdate
            ttid = april.id
            tcmp = april.scmp
            tdetail = april.sdetail
            ttimetotal = april.totaltime
            tstatus = april.status
            tallot = april.allot
            intial = april.intial_starttime
            currentend = april.current_endtime
                
            avg = ttid[5:15] 
                
            abk = Mysupport.objects.filter(empsid=ttid).count()
                
            if abk == 1:
                nm = Mysupport.objects.filter(empsid=ttid)
                for vc in nm:
                    updtime = vc.emptotaltime
                    diadom = vc.empsid
                   
                lab1 = datetime.strptime(ttimetotal, FMT)
                lab2 = datetime.strptime(updtime, FMT)
                xlm = datetime.strptime('00:00:00',FMT)
                zenmaster = (lab1 - xlm + lab2).time()

        
                lim = Mysupport.objects.filter(empsid=diadom,timesheetflag="False").update(intialtime=intial,endtimecurrent=currentend,emptotaltime=str(zenmaster),sstatus=tstatus,timesheetflag="True")
                rmv = Techsupport.objects.filter(status="Resolved").delete()
                 
            else:
                rn = Mysupport.objects.create(empsdate=tdate,empsprfct=avg,empsid=ttid,empallot=tallot,empcmp=tcmp,stype="Support",empssdetail=tdetail,intialtime=intial,endtimecurrent=currentend,emptotaltime=ttimetotal,sstatus=tstatus)
                rmv = Techsupport.objects.filter(status="Resolved").delete()
    else:
        print("time sheet updated only at 09:30:00 PM of every week days only")    
        
       # saka = Mysupport.objects.all()

        #for mgr in saka:
        #    be = mgr.

    ##################### auto export mail automation ####################################################

    ######################################################################################

    wah = "06:11 PM"
    #gt =  "03:58:10 PM"
    rap = datetime.now().strftime("%I:%M %p")
    leave = "sunday"
    weekday = datetime.today().strftime('%A')
    
     
        
    if datetime.strptime(rap, "%I:%M %p") == datetime.strptime(wah, "%I:%M %p")   and weekday!=leave: 

        lyken = Mysupport.objects.all().update(timesheetflag="False")
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
    
        wb.save('C:/Users/Ibiza/Downloads/statusreport.xls')


        mme = Mysupport.objects.filter(mailflag="False").count()
        if mme != 0:
            try:
                from django.core.mail import EmailMultiAlternatives

                subject = 'status report'
                from_email = 'novatechnosys@gmail.com'
                to = 'ramamoorthym@gmail.com'
    
                text_content = 'Dear Sir,'+'\n'+'\n'+'Please find the attachment.'

                message = EmailMultiAlternatives(subject, text_content, from_email, [to])
                message.attach_file('C:Users/Ibiza/Downloads/statusreport.xls')
                message.send()
                rmd = Mysupport.objects.filter(mailflag="False").update(mailflag="True")

            except:
                print("not sent")
        else:
            print("mail already sent")
    else:
        print("mail is automated at 09:32 PM every week days only")   
    
    
    ######## Reset mail flag ####################################

    wah = "09:31 PM"
    #gt =  "03:58:10 PM"
    rap = datetime.now().strftime("%I:%M %p")
    leave = "sunday"
    weekday = datetime.today().strftime('%A')
    
    rmd = Mysupport.objects.filter(mailflag="True").count()
    
        
    if datetime.strptime(rap, "%I:%M %p") == datetime.strptime(wah, "%I:%M %p") and weekday!=leave:
        if rmd!=0:
            rmd = Mysupport.objects.filter(mailflag="True").update(mailflag="Flase")
        else:
            print("flag is reset")


        
    

   

