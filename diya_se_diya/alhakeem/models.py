from django.db import models

# Create your models here.
class users(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    firstName = models.CharField(max_length=200, help_text='Enter your first name')
    lastName = models.CharField(max_length=200, help_text='Enter your last name')
    email= models.CharField(max_length=200, help_text='Enter your email')
    phone= models.CharField(max_length=200, help_text='Enter your phone')



class askforhelp(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    fullName = models.CharField(max_length=200, help_text='Enter your full name')
    uniName = models.CharField(max_length=200, help_text='Enter your university name')
    email= models.CharField(max_length=200, help_text='Enter your email')
    phone= models.CharField(max_length=200, help_text='Enter your phone')
    address= models.CharField(max_length=200, help_text='Enter your home address')
    city = models.CharField(max_length=200, help_text='Enter your city name')
    state= models.CharField(max_length=200, help_text='Enter your state name')
    requirement= models.CharField(max_length=200, help_text='Enter your requirement')
    detailsReq = models.TextField(max_length=200, help_text='Enter Details of your requirement')
    capability = models.TextField(max_length=200, help_text='Why do you think you are capable of donation?')
    anythingelse = models.TextField(max_length=200, help_text='Anything else you want donor know about you')


