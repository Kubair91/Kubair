from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .form import signupForm
from .models import Advise


def index(request):
    context = {'title': 'Home'}
    return render(request, 'index.html', context)


def base(request):
    context = {'title': 'base'}
    return render(request, 'base.html', context)


def View_Advise(request):
    Advise_list = Advise.objects.all().order_by('Created_time')
    paginator = Paginator(Advise_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    contex = {'Advises': posts}
    return render(request, 'View_Advise.html', contex)


def home(request):
    contex = {'title': 'home'}
    return render(request, 'home.html', contex)


def signup(request):
    contex = {}
    signupform = signupForm()
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            messages.success(request, 'Sign Up SuccessFull')
        else:
            messages.error(request, 'SignUp Failed Please Try Again Later')
    contex = {'signupform': signupform}
    return render(request, 'signup.html', contex)


def upatelikes(request):
    Advise_id = request.GET.get('Advise_id', None)
    likes = 0
    if Advise_id:
        advise = Advise.objects.get(id=int(Advise_id))
        if advise is not None:
            advise.likes += 1
            likes = advise.likes
            advise.save()
    return HttpResponse(likes)


def ajax_serach(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            result = Advise.objects.filter(Q(Advise__contains=q)|
                                           Q(Quote__contains=q)|
                                           Q(Explanation__contains=q)).order_by('Created_time')
            data=serializers.serialize('json',result)
            return HttpResponse(data,'application/json')
        else:
            return HttpResponse("No Result found")
    else:
        print('not ajax')
    return redirect('/')
