from django.db import models

# Create your models here.
class collage(models.Model):
    collageId=models.AutoField
    collageName=models.TextField(max_length=100)
    collageDescription=models.TextField(max_length=550)
    collageImage=models.ImageField(upload_to="collage/")
class designation(models.Model):
    designationId=models.AutoField
    designationName=models.TextField(max_length=30,unique=True)
    power=models.IntegerField(unique=True)
class department(models.Model):
    departmentId=models.AutoField
    collageId=models.ForeignKey(collage,on_delete=models.CASCADE)
    departmentname=models.CharField(max_length=200)
    semester=models.IntegerField()
class user(models.Model):
    userId=models.AutoField
    userName=models.TextField(max_length=20)
    surName=models.TextField(max_length=20)
    fatherName=models.TextField(max_length=20)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    designation=models.ForeignKey(designation,on_delete=models.CASCADE)
    semester=models.IntegerField()
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.CharField(max_length=100)
class registration(models.Model):
    id=models.AutoField
    email=models.EmailField()
    username=models.TextField(max_length=50)
    password=models.TextField(max_length=50)
    type=models.IntegerField(default=1)
