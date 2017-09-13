from django.contrib import admin

# Register your models here.
from .models import Python_Program
from .models import Java_Program
from .models import C_Program

admin.site.register(Python_Program)
admin.site.register(Java_Program)
admin.site.register(C_Program)