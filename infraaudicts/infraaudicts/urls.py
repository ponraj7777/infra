"""
URL configuration for Sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from my_app import views
# from adminpanel import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
     path('admin/',admin.site.urls),
     path('',views.home),
     path('taskassign',views.taskassign,name='task'),
     path('techcreate',views.techcreate),
     path('update<int:id>',views.update), 
     path('delete<int:id>',views.delete),
     path('auditaskassign',views.auditaskassign,name='auditask'),
     path('audicreate',views.audicreate),
     path('dashboard',views.dashboard,name = 'dash'),
     path('audiquery',views.audiquery)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)