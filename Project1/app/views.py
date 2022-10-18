from django.contrib import messages
from django.shortcuts import render,redirect
from filters import gabor,discrete_cosine,hough,lbp,fftLPF,fftHPF
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
        return render(request,'home.html')
    
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


def filter_view(request,num=0):
    nums = [1,2,3,4,5,6]
    if(num in nums):
        if(request.method == 'GET'):
                return render(request,'filter.html',{"inputImg":'null',"outputImg":'null'})
        if(request.method == 'POST'):
            img = request.POST.get('img')
            
            inputimg = 0
            new_img = 'null'

            if(img == ''):
                messages.error(request, 'Empty image provided')
                return render(request,'filter.html',{"inputImg":'null',"outputImg":'null'})
            else:
                img = stringToCv2(img)

                
                if(num==1):
                    new_img = discrete_cosine.discrete_cosine_transform(img)
                    
                elif(num==2):
                    new_img = gabor.Gabor(img)
                elif(num==3):
                    new_img = hough.Hough_Transform(img)
                elif(num==4):
                    new_img = lbp.LBP_Kernel(img)
                elif(num==5):
                    new_img = fftLPF.fft_low_pass_filter(img)
                elif(num==6):
                    new_img = fftHPF.fft_high_pass_filter(img)
            
            return render(request,'filter.html',{"inputImg":toString(img),"outputImg":toString(new_img)})
    else:
        return redirect(home)
    

