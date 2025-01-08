from django.db import models
import os 
import datetime
# Create your models here.
class data(models.Model):
    Name = models.CharField(max_length=20,default="")
    Age = models.IntegerField(default="")
    Address = models.CharField(max_length=20,default="")
    Contact = models.IntegerField(default="")
    Email = models.CharField(max_length=20,default="")
class Auditortaskdetails(models.Model):
    Tech_ID = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=100, default="")  # Change to CharField for string input
    area = models.CharField(max_length=20, default="")
    Deadline = models.DateField()  # Change to DateField for proper date handling


def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('static/uploads/',filename)


class Admintaskdetails(models.Model):
    Audi_ID = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=100, default="")  # Change to CharField for string input
    area = models.CharField(max_length=20, default="")
    Deadline = models.DateField()  # Change to DateField for proper date handling
    

class Item(models.Model):
    description = models.TextField(max_length=500,null = True)
    image = models.ImageField(upload_to=filepath,null=True,blank=True)


    def __str__(self):
        return f"{self.Tech_ID} - {self.name}"