from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    tn=input('Enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse ('The data succesfully entered')
  

def insert_WebPage(request):
    tn=input('Enter topic_name')
    n=input('Enter name')
    u=input('Enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('The data succesfully entered')

def insert_AccessRecords(request):
    tn=input('Enter topic_name')
    n=input('Enter name')
    u=input('Enter url')
    a=input('Enter author_name')
    d=input('Enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    AR=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('The data succesfully entered')










