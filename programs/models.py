from django.db import models

# Create your models here.
class Python_Program(models.Model):
    title=models.CharField(max_length=50,blank=False,default='Program Name')
    Program_code=models.TextField(blank=False,default='Programming Code')
    Created_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey('auth.User')
    likes=models.IntegerField(default=0)

    def save_name(self):
        self.save()

    def __str__(self):
        return self.title+" Added By "+self.author.username

class Java_Program(models.Model):
    title=models.CharField(max_length=50,blank=False,default='Program Name')
    Program_code=models.TextField(blank=False,default='Programming Code')
    Created_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey('auth.User')
    likes=models.IntegerField(default=0)

    def save_name(self):
        self.save()

    def __str__(self):
        return self.title+" Added By "+self.author.username

class C_Program(models.Model):
    title=models.CharField(max_length=50,blank=False,default='Program Name')
    Program_code=models.TextField(blank=False,default='Programming Code')
    Created_time=models.DateTimeField(auto_now=True)
    author=models.ForeignKey('auth.User')
    likes=models.IntegerField(default=0)

    def save_name(self):
        self.save()

    def __str__(self):
        return self.title+" Added By "+self.author.username