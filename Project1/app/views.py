from cmath import e
import re
from django.shortcuts import render,redirect
import filters
from django.http import HttpResponse
from django.views import View
# Create your views here.

def home(request):
    if(request.method == 'GET'):
        return render(request,'index.html')

def filter_view(request,num):
    nums = [1,2,3,4,5,6]
    if(num in nums):
        if(request.method == 'GET'):
                return render(request,'filter.html')
        if(request.method == 'POST'):
            if(num==1):
                img = request.POST.get('img')
                new_img = filters.gabor.Gabor(img)
                return render(request,'filter.html',{'img':new_img})
            # elif(num==2):
            # elif(num==3):
            # elif(num==4):
            # elif(num==5):
            # elif(num==6):
    else:
        return redirect(home)
    

