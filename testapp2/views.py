from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginfn(request):
    return render(request, 'login.html')

def index(request):
    return HttpResponse('Hello my friends')

def submitfn(request):
    return render(request,'submit.html')