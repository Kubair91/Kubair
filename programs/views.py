from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Python_Program, Java_Program, C_Program


def Selection(request):
    context = {'title': 'Select'}
    return render(request, 'Programs_Selections.html', context)

def Python_Code(request):
    program =Python_Program.objects.all().order_by('Created_time')
    paginator = Paginator(program, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    contex = {'pythonp': posts}
    return render(request, 'Python_programs.html', contex)

def Java_Code(request):
    program = Java_Program.objects.all().order_by('Created_time')
    paginator = Paginator(program, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    contex = {'javap': posts}
    return render(request, 'Java_Programs.html', contex)

def C_Code(request):
    program = C_Program.objects.all().order_by('Created_time')
    paginator = Paginator(program, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    contex = {'cp': posts}
    return render(request, 'C_Programs.html', contex)