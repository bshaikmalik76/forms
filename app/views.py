from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']

        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('successfull')
    return render(request,'display_topic.html')



def display_webpage(request):
    if request.method=='POST':
        tn=request.POST['topic']
        W=request.POST['name']
        tu=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        N=Webpage.objects.get_or_create(topic_name=T,name=W,url=tu)[0]
        N.save()



        return HttpResponse('successfull')
    return render(request,'display_webpage.html')



def display_Access(request):
    if request.method=='POST':
        tn=request.POST['topic']
        tu=request.POST['url']
        W=request.POST['name']
        D=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()

        N=Webpage.objects.get_or_create(topic_name=T,name=W,url=tu)[0]
        N.save()

        A=Access.objects.get_or_create(name=N,date=D)[0]
        A.save()
       
        return HttpResponse('successfull')
    return render(request,'display_Access.html')





            



