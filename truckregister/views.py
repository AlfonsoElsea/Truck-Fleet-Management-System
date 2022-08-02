
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from pymysql import NULL
from requests import request
from .models import Truck, Driver, addNewColumnInDB, createFieldForNewColumn, getFieldTypesList, getModelbyName, updateModels
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView
from .forms import  DriverForm, TruckForm, recordDriverForm, recordTruckForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url='login'
    template_name = 'truckregister/home.html'
    context_object_name = 'list_of_trucks'
    
    updateModels()
  
    
   

    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context['drivers_objects'] = Driver.objects.all()
        avail_trucks= Truck.get_available_trucks()
        avail_drivers= Driver.get_available_drivers()

        context['avail_drivers']=avail_drivers
    
        context['avail_trucks']=avail_trucks
        truckform=TruckForm()
        driverForm=DriverForm()
        context['truckform']=truckform
        context['driverForm']=driverForm

        return context
    

    def get_queryset(self) :
        return Truck.objects.all()

class TruckDetailView(LoginRequiredMixin,DetailView):
    login_url='login'

    model= Truck
    template_name = 'truckregister/truckdetails.html'


class DriverDetailView(LoginRequiredMixin,DetailView):
    login_url='login'

    model= Driver
    template_name = 'truckregister/driverdetails.html'

@login_required(login_url='login')
def TruckView(request, truck_id): 
    
    obj=Truck.objects.filter(pk=truck_id)
    
    
    # truck.update(milesodometer=miles+int(odometer))
    return HttpResponseRedirect(reverse('truckregister:truck',args=(truck_id,)))

class TruckUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    login_url='login'
    
    model = Truck
    form_class = TruckForm
    template_name = "truckregister/update.html"
    success_message= "Truck: %(brand)s succefully updated!"
    

    # def post(self, request, *args, **kwargs):
    #     prev=request.META.get('HTTP_REFERER','/')
    #     kwargs['prev']=prev
    #     self.success_url=prev
    #     print(prev)
    #     return super().get(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs) :
        
        
        
    #     return super().get(request, *args, **kwargs)


class DriverUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url='login'
    
    model = Driver
    form_class = DriverForm
    template_name = "truckregister/update.html"
    success_url = '/'
    success_message= "Driver: %(name)s succefully updated!"

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     prev=request.POST.get('next','/')
    #     return HttpResponseRedirect(prev) 

class DriverDeleteview(LoginRequiredMixin,DeleteView):
    login_url='login'
    model = Driver
    form_class = DriverForm
    template_name = "truckregister/delete_driver.html"
    success_url = '/'




@login_required(login_url='login')
def ProvidersView(request):
    return  render(request, "truckregister/providers.html")

@login_required(login_url='login')
def addTruckView(request):
    form=TruckForm()
    
    context = {}
    if request.method == 'POST':
            form= TruckForm(request.POST)
            if form.is_valid():
                form.save()
                submitted=True
                
                return redirect('truckregister:index')    
    
    context = {'form':form}
    
    return render (request, 'truckregister/add_truck.html',context)

@login_required(login_url='login')
def updateTruckView(request, pk):
            trucks = Truck.objects.all()
            truck =Truck.objects.filter(id=pk)
            form= TruckForm(instance= truck)
            print(truck)
            context={'list_of_trucks':trucks,'truckform':form}
            
            if request.method == 'POST':
                brand=request.POST.get('brand')
                model=request.POST.get('model')
                year=request.POST.get('year')
                color=request.POST.get('color')
                license=request.POST.get('license')
                odometer=request.POST.get('odometer')
                maintenance=request.POST.get('maintenance')
                truck= Truck(
                id=pk,
                brand=brand,
                model=model,
                year=year,
                color=color,
                truck_license_number=license,
                odometer=odometer,
                miles_for_maintenance= maintenance)
                truck.save()
               
                return redirect('truckregister:index')
            # return redirect(request,'truckregister/home.html', context)
            return redirect('truckregister:index')

   

@login_required(login_url='login')
def deleteTruckView(request, pk):
    truck = Truck.objects.get(id=pk)
   
    if request.method=='POST':
        truck.delete()
        return redirect('truckregister:index') 
    return redirect(request,'truckregister:index')  
    # return redirect(request, 'truckregister/home.html')
     
def editOdometerView(request, pk):
    
    truck = Truck.objects.filter(id=pk)
    if request.method=='POST':
        odometer= request.POST.get('odometer')    
        truck.update(odometer=odometer)
        return redirect('truckregister:index')
    return redirect('truckregister:index')
    # return redirect(request, 'truckregister/home.html')

@login_required(login_url='login')
def addDriverView(request):
    
    form=DriverForm
    print('Entered add Driver')
    # truck = Driver.objects.get
    if request.method == 'POST':
        print('Entered POST')
        form = DriverForm(request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            return redirect('truckregister:index')
    context = {'form':form}

    
    return render (request, 'truckregister/add_driver.html',context)
        


def addFieldView(request,name):
    
    fieldstypes= getFieldTypesList()
    context={'model':name,'types':fieldstypes}
    # fieldstypes = ['VARCHAR','LONGLONG','VAR_STRING']
    if request.method=='POST':
        url = str(request.path).split('/')
        modelname = url[len(url)-1]
        model = getModelbyName(modelname)
        newfield =createFieldForNewColumn(request.POST.get('field'),request.POST['datatype'],model)
     
        print(newfield)
        try:
            addNewColumnInDB(model,newfield)
            messages.success(request,"Field for "+ modelname+" created succefully")

        except:
            messages.warning(request, "Something went wrong, try again..")
            return render(request, 'truckregister/createField.html',context)

        return redirect('truckregister:index')
       
    updateModels()
    
    return render(request, 'truckregister/createField.html',context)

def createRecordView(request, name):
    
#     # print('before form')
    for item in request.GET.items():
        print(item)
    context={}
    
    
    model=getModelbyName(name)

    # form=form(request.POST)
    if name== "driver":        
        if request.method == 'POST':  
            form= recordDriverForm(request.POST)   
            if form.is_valid():
                form.save()                 
                return redirect('index')
            else:
                context={'form':form,'name':name}
                return render(request,'truckregister/addRecord.html',context)
        form= recordDriverForm() 
        context={'form':form,'name':name}

    else:
        if request.method == 'POST':  
            form= recordTruckForm(request.POST)   
            if form.is_valid():
                form.save()                 
                return redirect('index')
            else:
                context={'form':form,'name':name}
                return render(request,'truckregister/addRecord.html',context)
        form= recordTruckForm()
        context={'form':form,'name':name}


    return render(request,'truckregister/addRecord.html',context)


