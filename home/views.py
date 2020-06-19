from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import random
from .models import Doctor, Patient
import datetime
import pytz
# Create your views here.
global naam
naam='shabana'

def home(request):
    docs=Doctor.objects.all().exclude(capacity='FULL')
    curtime=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
    return render(request,'home/home.html',{'docs':docs})

def clear(request):
    docs=Doctor.objects.all()
    for doc in docs:
        doc.pats=0
        doc.capacity=''
        doc.busyTill=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
        doc.save()
    return redirect('home')

    

def checknaam(request):
    return render(request,'home/naam.html',{'naam':naam})

def registration(request):
    if request.method=='POST':
        availableDoc = Doctor.objects.all().exclude(capacity='FULL').order_by('pats').first()
        if availableDoc!=None:
            fname = request.POST['fname']
            lname = request.POST['lname']
            naam = fname+' '+lname
            curtime=datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
            doctime=availableDoc.busyTill.astimezone(pytz.timezone('Asia/Kolkata'))
            if curtime < doctime:
                apptime=availableDoc.busyTill.astimezone(pytz.timezone('Asia/Kolkata'))
                availableDoc.busyTill+=datetime.timedelta(minutes=30)
            else:
                apptime=curtime
                availableDoc.busyTill=curtime+datetime.timedelta(minutes=30)
            pat = Patient(patname=naam,doctor=availableDoc,appointTime=apptime)
            pat.save()
            availableDoc.pats+=1
            availableDoc.save()
            if availableDoc.pats==4:
                availableDoc.capacity='FULL'
                availableDoc.save()
            details={'pat':pat}
            return render(request,'home/registration.html',details)           
        else:
            return redirect('home')
    else:
        return HttpResponse("Tu ja re, Ye scheme tere liye hai hi nahi")
            






