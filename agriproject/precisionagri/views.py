from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import agriculture,NPK
from .form import agriform,queryform
from django.contrib import messages
from .prediction import cropprediction
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from precisionagri.form import loginform
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from agriproject.pdf import pdffile
from django.core.exceptions import ObjectDoesNotExist
def home(request):
    if request.method == 'POST':
        form = queryform(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['phone']
            mess = request.POST['message']
            message = "Hi this is "+name+" .My query is "+mess+" .Please solve this query and share the solution via "+email+" or "+mobile+" ."
            send_mail('Query Message',message,'brsapp33@gmail.com',['sasiguruvignesh@gmail.com',],fail_silently=False)
            return redirect(reverse('home',messages.success(request,'Message sent successfully.')))
        else:
            return redirect(reverse('home',messages.error(request,'Oops an error occured! Please try again.')))
    querycontext = {'query':queryform}
    return render(request,'registration/mainhome.html',querycontext)
def crop(request):
    context = {'agriform':agriform}
    if request.method == "POST":
        form = agriform(request.POST)
        if form.is_valid():
            state = request.POST['State_Name']
            district = request.POST['district']
            nit = request.POST['nitrogen']
            pho = request.POST['phosphorus']
            pot = request.POST['potassium']
            temp = request.POST['temperature']
            humidity = request.POST['humidity']
            ph = request.POST['ph']
            rain = request.POST['rainfall']
            n = float(nit)
            p = float(pho)
            k = float(pot)
            t = float(temp)
            h = float(humidity)
            phv = float(ph)
            r = float(rain)
            dist = "".join(district.split())
            if not dist.isalpha():
                return redirect(reverse('form',messages.error(request,"District Name not be in numeric.")))
            if (n < 0 or p < 0 or k < 0 or t < 0 or h < 0 or phv < 0 or r < 0):
                return redirect(reverse('form',messages.error(request,'Input values must be a positive number.')))
            store = agriculture.objects.filter(State_Name = state, District = district, Nitrogen = n, Phosphorous = p, Potassium = k, Temperature = t, Humidity = h, PH = phv, Rainfall = r)
            if store:
                res = store.first()
                rest = res.Crop_Label
                return redirect('prediction',rest,n,p,k,t,h,phv,r)
            else:
                results = cropprediction([n,p,k,temp,humidity,ph,rain])
                a = agriculture.objects.create(State_Name = state, District = district, Nitrogen = nit, Phosphorous = pho, Potassium = pot, Temperature = temp, Humidity = humidity, PH = ph, Rainfall = rain, Crop_Label = results)
                a.save()
                return redirect('prediction',results,n,p,k,t,h,phv,r)
    return render(request,'registration/crop.html',context)

def result(request,crop,n,p,k,t,h,phv,r):
    crop_dict = {'crop':crop,'n':n,'p':p,'k':k,'t':t,'h':h,'ph':phv,'r':r}
    return render(request,'registration/result.html',crop_dict) 

def adminlogin(request):
    template = loginform()
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/',messages.success(request,"This account already signed in."))
    if request.method == 'POST':
        requestform = loginform(request.POST)
        if requestform.is_valid():
            uname = request.POST['username']
            pwd = request.POST['password']
            try:
                user = User.objects.get(username = uname)
                if user.is_superuser:
                    person = authenticate(request,username = uname,password = pwd)
                    if person is not None:
                        login(request,person)
                        return redirect('/admin/')
                    else:
                        return redirect(reverse('loginpage',messages.error(request,"Enter Valid Credentials.")))
                else:
                    return redirect(reverse('loginpage',messages.error(request,'Sorry! Only admins has the rights to access.')))
            except:
                messages.error(request,"No such user object")
            
        else:
            return redirect(reverse('loginpage',messages.error(request,'Captcha must be required')))
    return render(request,'registration/login.html',{'forms' : template })

def pdf(request,crop,n,p,k,t,h,phv,r):
    crop_dict1 = {'crop':crop,'n':n,'p':p,'k':k,'t':t,'h':h,'ph':phv,'r':r}
    pdf = pdffile('registration/pdf.html',crop_dict1)
    return HttpResponse(pdf, content_type='application/pdf')

def search(request):
    if request.method == 'POST':
        query = request.POST['cropip']
        querylower = query.lower()
        try:
            cropname = NPK.objects.get(Crop_Name = query)
            n = cropname.Std_nitrogen
            p = cropname.Std_phosphorous
            k = cropname.Std_potassium
            return render(request,'registration/searchtl.html',{'nitrogen' : n,'phosphorous':p,'potassium':k, 'crop': querylower})
        except ObjectDoesNotExist:
            return redirect(reverse('home',messages.error(request,'Enter Valid Crop Name')))


