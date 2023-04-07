from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from user.models import *
from superadmin.models import *
from django.db.models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from pathlib import Path,os
from django.http import HttpResponse
# Create your views here.
def super_admin_index(request):
     if 'username' not in request.session:
         return redirect("login")
     else:
         return render(request,"super_admin_index.html")
def manageCollage(request):
    Collage=collage.objects.all()
    return render(request,"collage.html",{'collage':Collage})
def manageDepartment(request):
    Department=department.objects.all()
    Collage=collage.objects.all()
    return render(request,"department.html",{'department':Department,'Collage':Collage})
def manageDesignation(request):
    Designation=designation.objects.all()
    Count=designation.objects.aggregate(Sum('power'))
    data=Count['power__sum']
    base=100/data
    return render(request,"designation.html",{'designation':Designation,'data':base})
def manageUsers(request):
    Users=user.objects.all()
    Designation=designation.objects.all()
    Department=department.objects.all()
    return render(request,"users.html",{"Users":Users,"Designation":Designation,"Department":Department})
def manageRegistration(request):
    Registration=registration.objects.all()
    return render(request,"registration.html",{'Registration':Registration})
def manageLogin(request):
    return render(request,"login.html")


def functionLogin(request):
    if request.method == 'POST':
        UserName=request.POST['userName']
        Password=request.POST['password']
        data=registration.objects.get(email=UserName,password=Password)
        if data.type==1:
            return render(request,"index.html")
        elif data.type==2:
            return render(request,"designation.html")
        elif data.type==3:
            return render(request,"about.html")
        else:
            return render(request,"login.html")
        
#manage collage
def addCollage(request):
    if request.method == 'POST':
        Name=request.POST['collageName']
        Description=request.POST['collageDescription']
        Image=request.FILES['collageImage']
        collage(collageName=Name,collageDescription=Description,collageImage=Image).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteCollage(request, id):
  Collage = collage.objects.get(id=id)
  data=Collage.collageImage.url
  string= Path(os.getcwd().replace("\\superadmin", ""))
  beta=Path(data)
  if os.path.exists(f'{string}{beta}'):
    os.remove(f'{string}{data}')
    Collage.delete()
  return redirect(request.META.get('HTTP_REFERER'))
    
def updateCollage(request, id):
    Name=request.POST['collageName']
    Description=request.POST['collageDescription']
    Collage = collage.objects.get(id=id)
    Collage.collageName=Name
    Collage.collageDescription=Description
    try:
        image=request.FILES['image']
        Collage.collageImage=image
    except MultiValueDictKeyError:
        pass
    finally:
        Collage.save()
    return redirect(request.META.get('HTTP_REFERER'))
#manage designation
def addDesignation(request):
    if request.method == 'POST':
        DesignationName=request.POST['DesignationName']
        Power=request.POST['Power']
        designation(designationName=DesignationName,power=Power).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteDesignation(request, id):
  Designation = designation.objects.get(id=id)
  Designation.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateDesignation(request, id):
    DesignationName=request.POST['DesignationName']
    Power=request.POST['Power']
    Designation = designation.objects.get(id=id)
    Designation.designationName=DesignationName
    Designation.power=Power
    Designation.save()
    return redirect(request.META.get('HTTP_REFERER'))
#manage department
def addDepartment(request):
    if request.method == 'POST':
        DepartmentName=request.POST['departmentName']
        Semester=request.POST['semester']
        CollageId=request.POST['collage']
        Id=collage.objects.get(collageName=CollageId)
        data=Id
        department(collageId=data,departmentname=DepartmentName,semester=Semester).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteDepartment(request, id):
  Department = department.objects.get(id=id)
  Department.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateDepartment(request, id):
    Dept=request.POST['Dept']
    Semester=request.POST['Semester']
    Collage=request.POST['Collage']
    Department = department.objects.get(id=id)
    Department.departmentname=Dept
    Department.semester=Semester
    Id=collage.objects.get(collageName=Collage)
    Department.collageId=Id
    Department.save()    
    return redirect(request.META.get('HTTP_REFERER'))
#Manage Users
def addUser(request):
    if request.method == 'POST':
        UserName=request.POST['userName']
        SurName=request.POST['surName']
        FatherName=request.POST['fatherName']
        Department=request.POST['department']
        Designation=request.POST['designation']
        Semester=request.POST['semester']
        PhoneNumber=request.POST['phoneNumber']
        Address=request.POST['address']
        Email=request.POST['email']
        DepartmentId=department.objects.get(departmentname=Department)
        DesignationId=designation.objects.get(designationName=Designation)
        DeptData=DepartmentId
        DesigData=DesignationId
        user(department=DeptData,designation=DesigData,userName=UserName,surName=SurName,fatherName=FatherName,semester=Semester,phoneNumber=PhoneNumber,address=Address,email=Email).save()
        registration(email=Email,username=UserName,password="password@123").save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteUser(request, id):
  Users = user.objects.get(id=id)
  Users.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateUser(request, id):
    UserName=request.POST['userName']
    SurName=request.POST['surName']
    FatherName=request.POST['fatherName']
    Department=request.POST['department']
    Designation=request.POST['designation']
    Semester=request.POST['semester']
    PhoneNumber=request.POST['phoneNumber']
    Address=request.POST['address']
    Email=request.POST['email']
    User = user.objects.get(id=id)
    DepartmentId=department.objects.get(departmentname=Department)
    DesignationId=designation.objects.get(designationName=Designation)
    DeptData=DepartmentId
    DesigData=DesignationId
    User.department=DeptData
    User.designation=DesigData
    User.userName=UserName
    User.surName=SurName
    User.fatherName=FatherName
    User.semester=Semester
    User.phoneNumber=PhoneNumber
    User.address=Address
    User.email=Email
    User.save()
    return redirect(request.META.get('HTTP_REFERER'))
#manage Registration
def addRegistration(request):
    if request.method == 'POST':
        Name=request.POST['collageName']
        Description=request.POST['collageDescription']
        Image=request.FILES['collageImage']
        collage(collageName=Name,collageDescription=Description,collageImage=Image).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteRegistration(request, id):
  User = user.objects.get(id=id)
  User.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateRegistration(request, id):
    Name=request.POST['collageName']
    Description=request.POST['collageDescription']
    Collage = collage.objects.get(id=id)
    Collage.collageName=Name
    Collage.collageDescription=Description
    return redirect(request.META.get('HTTP_REFERER'))
#login
def manageLogin(request):
    if request.method=="POST":
        ur=request.POST['userName']
        ps=request.POST['password']
        data=registration.objects.get(email=ur,password=ps)
        if data.email==ur and data.password==ps:
            request.session['username']=data.username
            request.session['email']=data.email
            request.session['type']=data.type
            if data.type==1:
                return redirect('super_admin_index')
            elif data.type==2:
                return redirect('service')
            else:
                return redirect('contact')
        else:
            return redirect("service") 
    else:
        return redirect("super_admin_index")
def manageLogout(request):
    del request.session['username']
    return redirect("login")
def generate():
    from random import randrange
    num = randrange(1000, 9999)
    return num
def changePassword(request):
    if request.method=="POST":
        Email=request.POST['Email']
        data=str(generate())
        topic='Mender Company'
        data='<p style="color:blue; font-style: oblique;font-size: 30px;">OTP:<b style="color:yellow;">' +data +'</b></p>'
        from_email='mender.company@gmail.com'
        to_email=Email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
        return redirect('check_OTP',data)

    else:
        return redirect('changePassword')
