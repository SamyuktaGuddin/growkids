from django.shortcuts import render

from .models import userprofile
from .models import UserLogin
from .models import trainer_reg
from .models import training_details
from .models import enroll
from .models import payment_details

import datetime

# Create your views here.

from django.core.files.storage import FileSystemStorage
import os
from proj_growkids.settings import BASE_DIR


def showhome(request):
    return render(request,"rehome.html")

def makepay(request):
    return render(request,"makepayment.html")

def showabout(request):
    return render(request,"about.html")

def showcontact(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3', '')

        contact.objects.create(name=s1, email=s2,message=s3)

    return render(request,"contact.html")

def explfrm(request):
    return render(request,"expl.html")

def showstudent(request):
    userdict = userprofile.objects.all()
    return render(request,'viewstudents.html', {'userdict': userdict})

def showenroll(request):
    userdict = enroll.objects.all()
    return render(request,'viewenroll.html', {'userdict': userdict})

def showtrainingdetails(request):
    userdict = training_details.objects.all()
    return render(request,'viewtraining_details.html', {'userdict': userdict})

def showtrainerdetails(request):
    userdict = trainer_reg.objects.all()
    return render(request,'viewtrainerdetails.html', {'userdict': userdict})


def showstdenttrainer(request):
    userdict =userprofile.objects.all()
    return render(request,'viewstudentstrainer.html', {'userdict': userdict})

def showtrainerdetailsstud(request):
    userdict = trainer_reg.objects.all()
    return render(request,'viewtrainerstud.html', {'userdict': userdict})


def showpayment(request):
    userdict =payment_details.objects.all()
    return render(request,'viewpayment.html', {'userdict': userdict})

def profilefrm(request):
    if request.method=="POST":
        s1=request.POST.get('t1')
        s2=request.POST.get('t2')
        s3= request.POST.get('t3', '')
        s4= request.POST.get('t4', '')
        s5= request.POST.get('t5', '')
        s6= request.POST.get('t6', '')
        s7 = request.POST.get('t7', '')
        s8 = request.POST.get('t8', '')
        s9 = request.POST.get('t9', '')
        userprofile.objects.create(firstname=s1,lastnaem=s2,dob=s3,age=s4,
                                  parentname=s5, parentnumber=s6,address=s7,email=s8,category=s9)
        UserLogin.objects.create(username=s8, password=s6, utype='student')
        now = datetime.datetime.now()
        idate = now.strftime("%Y-%m-%d")
        enroll.objects.create(category=s9, trainer_name=s2, studentname=s1, studentemail=s8, enrolldate=idate)
        payment_details.objects.create(emailid=s8, paidby=s1, amount='1000', paydate=idate)
        return render(request, "makepayment.html")
    return render(request,"profile.html")


def inserttrainingdetails(request):
    if request.method=="POST" and request.FILES['myfile']:
        s1=request.POST.get('t1')
        s2=request.POST.get('t2')
        s3= request.POST.get('t3', '')
        s4= request.POST.get('t4', '')
        myfile= request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)

        training_details.objects.create(category=s1,trainer_name=s2,email_id=s3,details=s4,
                                  video=myfile)
    return render(request,"trainingdetails.html")

def bspfrm(request):
    return render(request,"bsp.html")

def regfrm(request):
    if request.method == "POST":
        s1 = request.POST.get('t1')
        s2 = request.POST.get('t2')
        s3 = request.POST.get('t3', '')
        s4 = request.POST.get('t4', '')
        s5 = request.POST.get('t5', '')
        s6 = request.POST.get('t6', '')
        s7 = request.POST.get('gender', '')

        trainer_reg.objects.create(firstname=s1, qualification=s2, email=s3, phoneno=s4,yearofexp=s5,category=s6, gender=s7)
        UserLogin.objects.create(username=s3, password=s4, utype='trainer')
        now = datetime.datetime.now()
        idate = now.strftime("%Y-%m-%d")
        payment_details.objects.create(emailid=s3, paidby=s1, amount='1000', paydate=idate)
        return render(request, "bsp.html")
    return render(request,"reg.html")


def forgot(request):
    if request.method == "POST":
        uname = request.POST.get('t1', '')
        user = UserLogin.objects.filter(username=uname).count()
        if user >= 1:
            userlog = UserLogin.objects.filter(username=uname).values()
            for u in userlog:
                upass = u['password']
                content = upass
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('rockpython839@gmail.com', 'pzbrfwlyorbnnigr')
                mail.sendmail('rockpython839@gmail.com', uname, content)
                mail.close()
                return render(request, 'login.html', {'msg': 'Your password has been sent to your E-mail'})
        else:
            return render(request, 'forgot.html', {'msg': 'Enter a valid username'})
    return render(request, 'forgot.html')



def logcheck(request):
    if request.method == "POST":
        username = request.POST.get('t1', '')
        password = request.POST.get('t2', '')
        request.session['username']=username
        #if username=="admin" and password=="admin":
        checklogin = UserLogin.objects.filter( username=username).values()
        for a in checklogin:
            utype = a['utype']
            upass= a['password']
            if(upass == password):
                if (utype == "admin"):
                    return render(request, 'admin_home.html', context={'msg': 'welcome to storehead'})

                if(utype == "trainer"):
                    return render(request, 'trainer_home.html', context={'msg': 'welcome to customer'})

                if (utype == "student"):
                    return render(request, 'student_home.html', context={'msg': 'welcome to account dept'})

            else:
                return render(request,'log.html',{'msg':'Check user name or passwrod'})

    return render(request,'log.html')

def changepass(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')
        ucheck = UserLogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    UserLogin.objects.filter(username=uname).update(password=newpass)
                   # base_url=reverse('login')
                    msg='password has been changed successfully'
                    #return redirect(base_url,msg=msg)
                    return render(request, 'login.html')
                else:
                    return render(request, 'changepassword.html',{'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'changepassword.html',{'msg': 'invalid username'})
    return render(request, 'changepassword.html')

