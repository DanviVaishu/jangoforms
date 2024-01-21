from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import*
def create_school(request):
    esfo=SchoolForm()
    d={'esfo':esfo}
    if request.method=='POST' :
        dsfo=SchoolForm(request.POST)
        if dsfo.is_valid():
            sn=dsfo.cleaned_data['Sname']
            sl=dsfo.cleaned_data['Slocation']
            sp=dsfo.cleaned_data['Sprincipal']
            e=dsfo.cleaned_data['Email']
            re=dsfo.cleaned_data['ReenterEmail']
            So=School.objects.get_or_create(Sname=sn,Slocation=sl,Sprincipal=sp,Email=e,ReenterEmail=re)[0]
            So.save() 
            return HttpResponse('submitted')
        else:
            return HttpResponse('data is invalid')
    
    return render(request,'create_school.html',d)



