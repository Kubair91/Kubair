from django.db import models

# Create your models here.
class Add_Picture(models.Model):
    Pic_name = models.CharField(max_length=50, blank=False, default='Enter the name of the pic')
    image = models.ImageField(upload_to='Gallery_Pics')
    Added_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User')

    def save_name(self):
        self.save()

    def __str__(self):
        return self.Pic_name+" Added By "+self.author.username

