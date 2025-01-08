from django.contrib import admin
from .models import data
from .models import Auditortaskdetails,Admintaskdetails
# Register your models here.
admin.site.register(data)
admin.site.register(Auditortaskdetails)
admin.site.register(Admintaskdetails)

