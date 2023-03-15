from django.contrib import admin
from home.models import Contact
#This is for new site
from home.models import Newapp
from home.models import Addexam
from home.models import *
# Register your models here.
admin.site.register(Contact)


#This is for new site
admin.site.register(Newapp)
admin.site.register(Addexam)
admin.site.register(Addroom)

admin.site.register(Addbuilding)
admin.site.register(Addexamcentre)
admin.site.register(Testing)

# This is for dbms
admin.site.register(Profile)
# Upto here