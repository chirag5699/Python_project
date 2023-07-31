from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Employee
from myapp.serializers import Employeeserial 
import datetime
import time
from django.shortcuts import render
from .models import *

# Create your views here.


@api_view(['GET'])
def getemployees(request,name,mail):
    # emplist=Employee.objects.get(id=name)
    Employee.objects.create(
        fname=name,
        email=mail
    )
    # serial = Employeeserial(emplist,many=True)
    return Response({"msg":"Successfully inserted"})
   
@api_view(['GET'])
   
def face_api(request):
    emplist=Employee.objects.all()
    serial = Employeeserial(emplist,many=True)
    return Response(serial.data)

@api_view(['GET'])
def update(request,ck,nm,em):
    emplist=Employee.objects.get(id=ck)
    emplist.fname=nm
    emplist.email=em
    emplist.save()
    serial = Employeeserial(emplist)
    return Response(serial.data)
  
@api_view(['GET']) 
def delete(request,ck):  
    emplist=Employee.objects.get(id=ck)
    emplist.delete()
    serial = Employeeserial(emplist)
    return Response(serial.data)