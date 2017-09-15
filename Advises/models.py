from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Advise(models.Model):
    Advise=models.CharField(max_length=50,blank=False,default='Enter Your Advise Topic')
    Quote=models.CharField(max_length=50,blank=False,default='Enter Your Quote')
    Explanation=models.TextField(blank=False,default='Explain your advise')
    Created_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey('auth.User')
    likes=models.IntegerField(default=0)

    def save_name(self):
        self.save()

    def __str__(self):
        return self.Advise+" Added By "+self.author.username











