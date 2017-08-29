from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from Advises.form import signupForm
from Advises.models import Advise

def index(request):
    context={'title':'Home'}
    return render (request,'index.html',context)

def base(request):
    context={'title':'base'}
    return render (request,'base.html',context)

def View_Advise(request):
    context = {'Advises': Advise.objects.all().order_by('Created_time').reverse()}
    return render (request,'View_Advise.html' ,context)

def home(request):
    contex={'title':'home'}
    return render(request,'home.html',contex)

def signup(request):
    contex={}
    signupform=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            messages.success(request,'Sign Up SuccessFull')
        else:
            messages.error(request,'SignUp Failed Please Try Again Later')
    contex={'signupform':signupform}
    return render(request,'signup.html',contex)

def login(request):
    contex={}
    login=login()