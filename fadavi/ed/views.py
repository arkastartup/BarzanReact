from django.shortcuts import render
import json
from django.http import StreamingHttpResponse
from .models import users
from django.forms.models import model_to_dict
from django.core.files.storage import FileSystemStorage
import hashlib


check={'status':'fail','name':'0'}
active_users=[]
def index(data):
    if (data.method == "POST"):

        dataa=json.loads(data.body)
        if (dataa['state']== "signup"):
            signup(dataa)
        elif (dataa['state']== "signin"):
            signin(dataa)
        elif (dataa['state']== "changepass"):
            changepass(dataa)
        elif (dataa['state']== "login"):
            signupp(data)
        return StreamingHttpResponse(json.dumps(check),content_type="application/json")
   # elif (dat)
    else:


       #exist=users.objects.filter(username="reza").values()

       #s=exist['password']
        #return StreamingHttpResponse(data.body)

         return render(data, 'Home.htm')
def signup (data):

        p=data['username']
        if users.objects.filter(username=p):


            check['status']='این نام کاربری قبلا ثبت شده است'


        else:
            database=users()
            database.username=data['username']
            passwordd=data['password']
            hexe = hashlib.sha256(passwordd.encode()) 
            hexe=hexe.hexdigest()
            database.password= hexe
            database.save()
            check['status']='success'


def signin(data):

        p=data['username']
        passwordd=data['password']
        t= hashlib.sha256(passwordd.encode()) 
        t= t.hexdigest()
        if users.objects.filter(username=p):
            if users.objects.filter(username=p,password=t):
                check['status']='success'
                check['name']=data['username']
                id=p+t
                activate(id)
            else:
                check['status']='رمز عبور صحیح نمیباشد'

        else:

            check['status']='این نام کاربری وجود ندارد'
def changepass(data):

    d=data['username']
    p=data['password']
    t= hashlib.sha256(p.encode()) 
    p= t.hexdigest()
    newp=data['newpassword']
    exist=users.objects.filter(username=d).values()
    dat = json.dumps(list(exist))
    if(dat['password']==p):

        exist.update(password=newp)
        check['status']='success'

    else:
        check['status']=' رمز قثثقثقث عبور قبلی صحیح نمیباشد'

def activate(id):
    if id not in active_users:
        active_users.append(id)
    else:
        check['status'] = 'این کاربر از قبل وارد سیستم شده است'
def signupp(data):
    return render(data,'signup.htm')       
