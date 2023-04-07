from django.shortcuts import render,redirect
from django.shortcuts import redirect
from user.models import *
from superadmin.models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def forgot_password(request):
    return render(request,"forgot_password.html")
def forgot_username(request):
    return render(request,"forgot_username.html")

def functionLogin(request):
    if request.method == 'POST':
        UserName=request.POST['userName']
        Password=request.POST['password']
        data=registration.objects.get(username=UserName,password=Password)
        if data.type==1:
            return render(request,"index.html")
        elif data.type==2:
            return render(request,"service.html")
        elif data.type==3:
            return render(request,"about.html")
        else:
            return render(request,"login.html")
def contactValidate(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact(name=name,email=email,subject=subject,message=message).save()
        topic='Mender Company'
        data='<p style="color:blue; font-style: oblique;font-size: 30px;">Thank you <b style="color:yellow;">' +name +'</b> for join us with your valuable message.</p>'
        from_email='mender.company@gmail.com'
        to_email=email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
        return redirect(request.META.get('HTTP_REFERER'))