from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from superadmin.models import *
from django.db.models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from pathlib import Path,os
from django.http import *
# Create your views here.
def index(request):
    if "Founder and Managing Trustee" in request.session:
        sessionData=request.session['Founder and Managing Trustee']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif  "Vice-Chancellor" in request.session:
        sessionData=request.session['Vice-Chancellor']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "Vice-President" in request.session:
        sessionData=request.session['Vice-President']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "Director" in request.session:
        sessionData=request.session['Director']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "Head Of Department" in request.session:
        sessionData=request.session['Head Of Department']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "Teacher" in request.session:
        sessionData=request.session['Teacher']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "student" in request.session:
        sessionData=request.session['student']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    elif "admin" in request.session:
        sessionData=request.session['admin']
        sessionData=registration.objects.get(email=sessionData)
        return render(request,"index.html",{"session":sessionData})
    else:
        return redirect("manageLogin")
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


def manageLogin(request):
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
        registration(email=Email,username=UserName,password="password@123",type=DesigData).save()
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
def functionLogin(request):
    if request.method=="POST":
        ur=request.POST['userName']
        ps=request.POST['password']
        data=registration.objects.get(email=ur,password=ps)
        if data.email==ur and data.password==ps:
            if data.type.designationName=="Founder and Managing Trustee":
                request.session["Founder and Managing Trustee"]=data.email
                return redirect('index')
            elif data.type.designationName=="Vice-Chancellor":
                request.session["Vice-Chancellor"]=data.email
                return redirect('index')
            elif data.type.designationName=="Vice-President":
                request.session["Vice-President"]=data.email
                return redirect('index')
            elif data.type.designationName=="Director":
                request.session["Director"]=data.email
                return redirect('index')
            elif data.type.designationName=="Head Of Department":
                request.session["Head Of Department"]=data.email
                return redirect('index')
            elif data.type.designationName=="Teacher":
                request.session["Teacher"]=data.email
                return redirect('index')
            elif data.type.designationName=="student":
                request.session["student"]=data.email
                return redirect('index')
            else:
                request.session["admin"]=data.email
                return redirect('index')
        else:
            return redirect("manageDesignation") 
    else:
        return redirect("manageCollage")
def manageLogout(request):
    if "Founder and Managing Trustee"  in request.session:
        del request.session['Founder and Managing Trustee']
    elif "Vice-Chancellor" in request.session:
        del request.session['Vice-Chancellor']
    elif "Vice-President" in request.session:
        del request.session['Vice-President']
    elif "Director" in request.session:
        del request.session['Director']
    elif "Head Of Department" in request.session:
        del request.session['Head Of Department']
    elif "Teacher" in request.session:
        del request.session['Teacher']
    elif "student" in request.session:
        del request.session['student']
    elif "admin" in request.session:
        del request.session['admin']
    return redirect("manageLogin")
