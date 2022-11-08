from django.shortcuts import render,HttpResponse,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from home.models import *

import os
import pandas as pd
from pathlib import Path
from django.core.files import File
from django.conf import settings
from django_pandas.io import read_frame
from django.contrib.auth.models import User
import random
# Create your views here.
def dbmshome(request):
    uploaded_file_url=''
    if request.method == "POST":
        
        uploaded_file=request.FILES['fileInvigilator']
        fs=FileSystemStorage()
        if fs.exists(uploaded_file.name):
            messages.info(request, 'File already exists in folder')
            fs.delete(uploaded_file.name)
        
        name = fs.save(uploaded_file.name,uploaded_file)
        uploaded_file_url = fs.url(name)
        messages.success(request, 'File is now uploaded not to database')
    context = {
        'uploaded_file_url': uploaded_file_url,
    }
    return render(request, "templatesdbms\dbmshome.html", context)


def dbmsuploadfiles(request):
    file_path=''
    if request.method == 'POST':
        profile=Profile.objects.get(user=request.user)
        if profile.file_user:
            file_path=profile.file_user.path
            if os.path.exists(file_path):
                os.remove(file_path)

        profile.file_user=request.FILES['fileInvigilator']
        profile.save()
        messages.success(request, 'File added to database')
        if profile.file_user:
            uploaded_file_url = profile.file_user.url
            excel_file = uploaded_file_url
            print(excel_file) 
            if os.path.exists(profile.file_user.path):
                excel_file = profile.file_user.path
                print(excel_file) 
            
        
            empexceldata = pd.read_excel(excel_file)
            
            dbframe = empexceldata
            
            for dbframe in dbframe.itertuples():
                if Newapp.objects.filter(newappphone=dbframe.Phone).exists()==False:
                    if len(dbframe.Name)>0:
                        newapp=Newapp.objects.create(profile=profile,newappname=dbframe.Name,newappemail=dbframe.Email, newappphone=dbframe.Phone,newappaddress=dbframe.Address,newappdepart=dbframe.Department,newappposition=dbframe.Position)
                        newapp.save()                
            

    profile=Profile.objects.get(user=request.user)
    newapp_data = Newapp.objects.filter(profile=profile).values_list("newappname","newappemail","newappphone","newappaddress","newappdepart","newappposition")
    
    
    
    
    
    data = pd.DataFrame(list(newapp_data),columns=["Name","Email","Phone","Address","Department","Position"])
    data.set_index('Name', inplace=True)
    
    
    
    
    newpath="media/"+'Invigilators List-'+profile.user.username+'.xlsx'
    data.to_excel(newpath)    
    path = Path(newpath)
    if profile.file_generated:
        if os.path.exists(profile.file_generated.path):
            os.remove(profile.file_generated.path)
    with path.open(mode='rb') as f:
        profile.file_generated = File(f, name=path.name)
        
        profile.save()

    file_path=path
    if os.path.exists(file_path):
        os.remove(file_path)


    file_user_basename=''
    file_generated_basename=''
    
    
    if profile.file_user:
        file_user_basename=os.path.basename(profile.file_user.path)
    if profile.file_generated:
        file_generated_basename=os.path.basename(profile.file_generated.path)

    context={
        
        "profile":profile,
        "file_user_basename":file_user_basename,
        "file_generated_basename":file_generated_basename,
    }
    return render(request, "templatesdbms\dbmsuploadfiles.html", context)
    
def dbmsfileslist(request):
    
    context={
    

    }
    return render(request, "templatesdbms\dbmsfileslist.html", context)

def dbmsnewapp(request):

    profile=Profile.objects.get(user=request.user)
    alltesting_data=Testing.objects.all()
    allnewapp_data=Newapp.objects.filter(profile=profile)
    numberofinvineachroom=2

    # allexam_data=Addexam.objects.filter(profile=profile)
    allexam_data=Addexam.objects.filter(examname="Bachelor 2079")
    listofinvallroom=[]
    listofroom=[]
    listofnewapp=list(allnewapp_data)
    for aed in allexam_data:
        allbuilding_data=aed.examaddbuilding.all()
        for abd in allbuilding_data:
            allroom_data = abd.rooms.all()
            listofroom=list(allroom_data)
            for ard in allroom_data:
                allnewaapproom=ard.invigilatorsinroom.all()
                for anar in allnewaapproom:
                    ard.invigilatorsinroom.remove(anar)
                  
    
                    
    
    
    
    
    for aed in allexam_data:
        allbuilding_data=aed.examaddbuilding.all()
        for abd in allbuilding_data:
            print(abd.buildingname)
            allroom_data = abd.rooms.all().order_by('?')
            numberofroom=len(list(allroom_data))

            if numberofroom*numberofinvineachroom<= len(allnewapp_data):
                for ard in allroom_data:
                    if len(ard.invigilatorsinroom.all())<numberofinvineachroom:                        
                        for alnewda in allnewapp_data: 
                            if alnewda not in listofinvallroom and len(ard.invigilatorsinroom.all())<numberofinvineachroom:
                                listofinvallroom.append(alnewda)
                                ard.invigilatorsinroom.add(alnewda)
            else:
                messages.error(request, "Not enough invigilator for all rooms")



    # print(allexam_data)

    # allroom_data = Addroom.objects.filter(profile=profile)
    # allinvigilator_data = Newapp.objects.filter(profile=profile)
    # for ard in allroom_data:
        
    #     print(ard.pk)
    #     print(ard.roomname)
    #     print (ard.invigilatorsinroom.all())
    # print(allroom_data)
    context={
    
        # "allroom_data":allroom_data,
        
    }
    return render(request, "templatesdbms\dbmsnewapp.html", context)



            