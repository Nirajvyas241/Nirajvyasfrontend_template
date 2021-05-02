from django.shortcuts import render,HttpResponse
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
    'variable': "this is sent"
    }
    return render(request,'index.html',context)
#return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
#return HttpResponse("this is about page")

def services(request):
    return render(request,'languagesknown.html')
#return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        contact = Contact(name=name,desc=desc)
        contact.save()
        messages.success(request,'Your form has been Submitted Succesfully.We will get back to you soon Through E-mail!')
    return render(request, 'contact.html')
#return HttpResponse("this is contact page")