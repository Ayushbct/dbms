#This is all added later

import django_filters
from django_filters import CharFilter

from home.models import *

class ViewtableFilter(django_filters.FilterSet):
    newappname=CharFilter(field_name="newappname",lookup_expr='icontains',label='Name')
    newappemail=CharFilter(field_name="newappemail",lookup_expr='icontains',label='Email')
    newappphone=CharFilter(field_name="newappphone",lookup_expr='icontains',label='Number')
    class Meta:
        model=Newapp
        
        fields='__all__'
        exclude=['newappaddress',"newappdepart",'newappposition','profile']