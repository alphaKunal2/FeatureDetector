import re
from django.shortcuts import render,redirect
from filters import gabor,discrete_cosine,hough,lbp
from django.http import HttpResponse
from django.views import View
# Create your views here.

def home(request):
    if(request.method == 'GET'):
        return render(request,'index.html')

def filter_view(request,num=0):
    nums = [1,2,3,4,5,6]
    if(num in nums):
        if(request.method == 'GET'):
                return render(request,'filter.html')
        if(request.method == 'POST'):
            img = request.POST.get('img')
            if(num==1):
                print(img)
                new_img = discrete_cosine.discrete_cosine_transform(img)
                print(len(new_img))
                return render(request,'filter.html',{'img':new_img})
            elif(num==2):
                new_img = gabor.Gabor(img)
                return render(request,'filter.html',{'img':new_img})
            elif(num==3):
                new_img = hough.Hough_Transform(img)
                return render(request,'filter.html',{'img':new_img})
            elif(num==4):
                new_img = lbp.LBP_Kernel(img)
                return render(request,'filter.html',{'img':new_img})    
            # elif(num==5):
            # elif(num==6):
    else:
        return redirect(home)
    

