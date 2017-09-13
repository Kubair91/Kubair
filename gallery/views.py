from django.shortcuts import render

# Create your views here.
from .models import Add_Picture


def gallery(request):
    contex={'pics':Add_Picture.objects.all()}
    return render(request,'gallery.html',contex)