from cmath import e
import re
from django.shortcuts import render,redirect
from filters import gabor
from django.http import HttpResponse
from django.views import View
import base64
from PIL import Image
import cv2
import io
import numpy as np
# Create your views here.

def home(request):
    if(request.method == 'GET'):
        return render(request,'index.html')
def stringToCv2(base64_string):
    imgdata = base64.b64decode(base64_string)
    data =  Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(data), cv2.COLOR_BGR2RGB)

# convert PIL Image to an RGB image( technically a numpy array ) that's compatible with opencv

    

def toString(img):
    _, im_arr = cv2.imencode('.jpg', img)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    
    return im_b64

def filter_view(request,num):
    nums = [1,2,3,4,5,6]
    if(num in nums):
        if(request.method == 'GET'):
                return render(request,'filter.html',{"outputImg":'null'})
        if(request.method == 'POST'):
            if(True):
                img = request.POST.get('img')
                
                cv2img = stringToCv2(img)
                print(cv2img.shape)
                new_img = gabor.Gabor(cv2img)
                print(toString(new_img))
                return render(request,'filter.html',{"outputImg":toString(new_img)})
            # elif(num==2):
            # elif(num==3):
            # elif(num==4):
            # elif(num==5):
            # elif(num==6):
    else:
        return redirect(home)
    

