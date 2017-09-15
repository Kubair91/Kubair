

# Create your views here.
from django.shortcuts import render

from .models import Add_Picture


def gallery(request):
    contex={'pics':Add_Picture.objects.all()}
    return render(request,'gallery.html',contex)

def error_404(request):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)