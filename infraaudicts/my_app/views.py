from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import data
from .models import Auditortaskdetails,Admintaskdetails,Item
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout




# Create your views here.
def home(request):
     
     return render(request,"mainpage.html")
def taskassign(request):
     techdetails = Auditortaskdetails.objects.all()
     return render(request,"mainpage.html", {'datas': techdetails})
def techcreate(request):
    if request.method == 'POST':
        # Retrieve form data
        techid = request.POST.get("technician-id")
        techname = request.POST.get("name")
        techarea = request.POST.get("area")
        techdead = request.POST.get("deadline")

        # Save data to the database
        techdata = Auditortaskdetails(
            Tech_ID=techid,
            name=techname,
            area=techarea,
            Deadline=techdead,
        )
        techdata.save()

        # Redirect to prevent form resubmission
        return redirect('task')

    # Fetch all technician details for display
    techdetails = Auditortaskdetails.objects.all()
    return render(request, "mainpage.html", {'datas': techdetails})

# def update(request,id):  
#     changed_data = Auditortaskdetails.objects.get(id=id) 
#     if request.method == 'POST':
#         # Retrieve form data
#         techid = request.POST.get("technician-id")
#         techname = request.POST.get("name")
#         techarea = request.POST.get("area")
#         techdead = request.POST.get("deadline")

#         # Save data to the database
#         techdata = Auditortaskdetails(
#             Tech_ID=techid,
#             name=techname,
#             area=techarea,
#             Deadline=techdead,
#         )
#         techdata.save()
#         return redirect('task')
    
#     return render(request, "mainpage.html", {'data': changed_data})


def update(request, id):  
    # Retrieve the existing object
    changed_data = Auditortaskdetails.objects.get(id=id) 

    if request.method == 'POST':
        # Update the fields of the existing object
        changed_data.Tech_ID = request.POST.get("technician-id")
        changed_data.name = request.POST.get("name")
        changed_data.area = request.POST.get("area")
        changed_data.Deadline = request.POST.get("deadline")
        
        # Save the updated object to the database
        changed_data.save()
        
        # Redirect to the task list or another page
        return redirect('task')
    
    # Render the form with the existing data for editing
    return render(request, "mainpage.html", {'data': changed_data})


def register(request):
     return render(request,"")


def delete(request,id):
    name = Auditortaskdetails.objects.get(id=id)
    name.delete()
    return redirect('task')

def auditaskassign(request):
    techdetails = Admintaskdetails.objects.all()
    return render(request,"mainpage.html", {'datas': techdetails})

# def audicreate(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         audiid = request.POST.get("auditor-id")
#         audiname = request.POST.get("name")
#         audiarea = request.POST.get("area")
#         audidead = request.POST.get("deadline")
#         audides = request.POST.get('description')
        
#         if len(request.FILES) != 0:
#             Admintaskdetails.image = request.FILES['image']
#         Admintaskdetails.save()

#         # Save data to the database
#         audidata = Admintaskdetails(
#             Audi_ID=audiid,
#             name=audiname,
#             area=audiarea,
#             Deadline=audidead,
#             description = audidead
          
#         )
#         audidata.save()

#         # Redirect to prevent form resubmission
#         return redirect('auditask')
#     audidetails = Admintaskdetails.objects.all()
#     return render(request, "mainpage.html", {'datas': audidetails})


def audicreate(request):
    if request.method == 'POST':
        # Retrieve form data
        audiid = request.POST.get("auditor-id")
        audiname = request.POST.get("name")
        audiarea = request.POST.get("area")
        audidead = request.POST.get("deadline")
        # audides = request.POST.get('description')

        # # Initialize image variable
        
        # if len(request.FILES) != 0:
        #     image = request.FILES['image']

        # Save data to the database
        audidata = Admintaskdetails(
            Audi_ID=audiid,
            name=audiname,
            area=audiarea,
            Deadline=audidead,
            # description=audides,
            # image=image  # Include the image if uploaded
        )
        audidata.save()

        # Redirect to prevent form resubmission
        return redirect('auditask')

    # Fetch all admin task details to display
    audidetails = Admintaskdetails.objects.all()
    return render(request, "mainpage.html", {'datas': audidetails})



def dashboard(request):
    audidetails = Admintaskdetails.objects.all()
    
    return render(request,'mainpage.html',{'datas': audidetails})

def audiquery(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']
        prod.save()
        messages.success(request,"uploaded successfully")
        return redirect('dash')
    return render(request,'mainpage.html')
# def update(request,id):
#     changed_data = Auditortaskdetails.objects.get(id=id) 
#     if request.method=='POST':
#         techid = request.POST['technician-id']
#         techname = request.POST['name']
#         techarea = request.POST['area']
#         techdead = request.POST['deadline']
#         changed_data.Tech_ID=techid
#         changed_data.name=techname
#         changed_data.area=techarea
#         changed_data.Deadline=techdead
#         changed_data.save()
#         return redirect('task')

#     return render(request,'mainpage.html',{'datas':[changed_data]})

# def update(request, id):
#     try:
#         changed_data = Auditortaskdetails.objects.get(id=id)  # Get the specific record
#     except Auditortaskdetails.DoesNotExist:
#         return HttpResponse("Technician not found.", status=404)

#     if request.method == 'POST':
#         # Update the data with the submitted form values
#         changed_data.Tech_ID = request.POST["technician-id"]
#         changed_data.name = request.POST["name"]
#         changed_data.area = request.POST["area"]
#         changed_data.Deadline = request.POST["deadline"]
#         changed_data.save()  # Save the updated record
#         return redirect('task')  # Redirect to the task assignment page

#     # Pass the object to the template for rendering
#     return render(request, 'mainpage.html', {'datas': [changed_data]})





# def logout_view(request):
#     logout(request)
#     return redirect('/loginpage')

# def login(request):
#     return render(request,"audictlogin.html")

