from django.db import models

# This is for dbms
from django.contrib.auth.models import User
# Up to here

#This is added later
from datetime import date
# Create your models here.
# This is for dbms
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    file_user = models.FileField( upload_to='profile/uploaded_files/',null=True,blank=True, max_length=100)
    file_generated = models.FileField( upload_to='profile/generated_files/',null=True,blank=True, max_length=100)

    def __str__(self):
        return self.user.username
# Upto here


class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name +" : "+ self.email


class Newapp(models.Model):
    # This is for dbms
    profile = models.ForeignKey(Profile,blank=True,null=True, on_delete=models.CASCADE)
    # Upto here
    newappname=models.CharField(max_length=122)
    newappemail=models.CharField(max_length=122,blank=True,default="-")
    newappphone=models.CharField(max_length=12)
    newappaddress=models.CharField(max_length=122)
    newappdepart=models.CharField(max_length=255,blank=True)
    newappposition=models.CharField(max_length=255)
    
    #newappdate=models.DateField()
    def __str__(self):
        return self.newappname +" : "+ self.newappdepart


class Addroom(models.Model):
    # This is for dbms
    profile = models.ForeignKey(Profile,blank=True,null=True, on_delete=models.CASCADE)
    # Upto here
    roomname=models.CharField(max_length=122)
    invigilatorsinroom=models.ManyToManyField(Newapp,blank=True)
    
    def __str__(self):
        return self.roomname

class Addbuilding(models.Model):
    # This is for dbms
    profile = models.ForeignKey(Profile,blank=True,null=True, on_delete=models.CASCADE)
    # Upto here
    buildingname=models.CharField(max_length=122)
    rooms=models.ManyToManyField(Addroom,blank=True)
    
    def __str__(self):
        return self.buildingname

class Addexamcentre(models.Model):
    # This is for dbms
    profile = models.ForeignKey(Profile,blank=True,null=True, on_delete=models.CASCADE)
    # Upto here
    examcentrename=models.CharField(max_length=122)
    buildings=models.ManyToManyField(Addbuilding,blank=True)
    
    def __str__(self):
        return self.examcentrename


class Addexam(models.Model):
    # This is for dbms
    profile = models.ForeignKey(Profile,blank=True,null=True, on_delete=models.CASCADE)
    # Upto here
    examname=models.CharField(max_length=122)
    examtype=models.CharField(max_length=122)
    examsemtype=models.CharField(max_length=122,blank=True,null=True)
    regularback=models.CharField(max_length=122,blank=True,null=True)
    # examcentre=models.CharField(max_length=122)
    examdate=models.CharField(max_length=122)
    newexamdate=models.DateField(max_length=122,blank=True, null=True)
    examtime=models.CharField(max_length=122)
    newexamtime=models.TimeField(max_length=122,blank=True, null=True)
    examtime_end=models.CharField(max_length=122,blank=True, null=True)
    newexamtime_end=models.TimeField(max_length=122,blank=True, null=True)
    examshift=models.CharField(max_length=122,blank=True, null=True)
    examdesc=models.TextField()
    #examnewapp=models.ForeignKey(Newapp,blank=True,null=True, on_delete=models.CASCADE)
    
    
    

    #This is for buildings in exam
    examaddbuilding=models.ManyToManyField(Addbuilding,blank=True)
    newaddexamcentre = models.ManyToManyField(Addexamcentre,blank=True)
    def __str__(self):
        return self.examname


class Testing(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    file_generated = models.FileField( upload_to='profile/generated_files/',null=True,blank=True, max_length=100)
    newappname=models.CharField(max_length=122,default="")
    newappphone=models.CharField(max_length=12,default="")
    def __str__(self):
        return self.newappname
        




