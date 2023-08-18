from django.db import models
from django.contrib.auth.models import User



class Services(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="loremipsum")
    image = models.ImageField(upload_to='products')

    def __str__(self):

        return self.name

class About(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="loremipsum")
    def __str__(self):

        return self.name

class Comments(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="loremipsum")
    image = models.ImageField(upload_to='products')
    date=models.DateField(auto_now_add=True)
    def __str__(self):

        return self.name

class BuildPackets(models.Model):
    name=models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="loremipsum")
    storage=models.CharField(max_length=10 , default="20")
    lifetimesupport=models.BooleanField(default=False)
    premiumaddons=models.BooleanField(default=False)
    fastestnetwork=models.BooleanField(default=False)
    moreoptions=models.BooleanField(default=False)
    image = models.ImageField(upload_to='build-packets' )
    price= models.IntegerField(default=1000)

    def get_lifetimesupport(self):
        if not self.lifetimesupport:
            return "non-function"
        else:
            pass
    def get_premiumaddons(self):
        if not self.premiumaddons:
            return "non-function"
        else:
            pass
    def get_fastestnetwork(self):
        if not self.fastestnetwork:
            return "non-function"
        else:
            pass    
    def get_moreoptions(self):
        if not self.moreoptions:
            return "non-function"
        else:
            pass

    def __str__(self):
        return self.name


class UserPackets(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    packet=models.ForeignKey(BuildPackets, on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.username
        