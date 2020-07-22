from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to project3</marquee>")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html", context={"data":"data of me","name":"Jyothi"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html", {'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html", {'a':10 ,'b':25})

def url_data(request,name):
    return HttpResponse("{}".format(name))

def ab(request,a,b):
     if a > b :
        return HttpResponse("{}".format(a))
     else :
        return HttpResponse("{}".format(b))
    
def st(request,input):
    vcount=0
    ccount=0
    
    for i in input:
        if i in ("a","e","i","o","u"):
            vcount += 1
            return HttpResponse( "vowel - {}".format(vcount))
        else:
            ccount += 1
            return HttpResponse("consonant - {}".format(ccount))
   
def vowel(request, input): 
    ocount = 0
    ccount = 0
    for i in input:
        if i in 'aeiou':
            ocount += 1
        else:
            ccount += 1
    return render(request, 'directory/vowel.html', {'input':input, 'ocount':ocount, 'ccount':ccount})
    
