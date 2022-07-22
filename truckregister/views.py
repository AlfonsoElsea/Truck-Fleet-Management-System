from ast import If
from msilib.schema import ListView
from multiprocessing import context
from re import sub
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from .models import Truck, Driver
from django.views import generic
from django.db.models import F
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView
from .forms import  TruckForm



class IndexView(generic.ListView):
    template_name = 'truckregister/home.html'
    context_object_name = 'list_of_trucks'
    
    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context['drivers_objects'] = Driver.objects.all()
        return context
    

    def get_queryset(self) :
        return Truck.objects.all()

class DetailView(generic.DetailView):
    model= Truck
    template_name = 'truckregister/truckdetails.html'

def TruckView(request, truck_id): 
  
    Truck.objects.filter(pk=truck_id)
    
    # truck.update(milesodometer=miles+int(odometer))
    return HttpResponseRedirect(reverse('truckregister:truck',args=(truck_id,)))

class TruckUpdateView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = "truckregister/truck_form.html"
    

def ProvidersView(request):
    return  render(request, "truckregister/providers.html")

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

def updateTruckView(request, pk):

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
                trucks = Truck.objects.all()
                context={'list_of_trucks':trucks}
                return redirect('truckregister:index')
            return redirect(request,'truckregister/home.html')

            # truck = Truck.objects.get(id=pk)
            # form = TruckForm(instance=truck)
            # if request.method=='POST':
            #     form= TruckForm(request.POST, instance=truck)
            #     if form.is_valid():
            #         form.save()
            #         return redirect('truckregister:index')
            # context={'form':form,'item':truck}
            # return render(request,'truckregister/home.html',context)    

def deleteTruckView(request, pk):
    truck = Truck.objects.get(id=pk)
   
    if request.method=='POST':
        truck.delete()
        return redirect('truckregister:index') 

    return redirect(request, 'truckregister/home.html')
     
def editOdometerView(request, pk):
    
    truck = Truck.objects.filter(id=pk)
    odometer= request.POST.get('odometer')    
    truck.update(odometer=odometer)
    return redirect('truckregister:index')
        




# def updateTruckView(request, pk):
#     truck = Truck.objects.get(id=pk)
#     form = TruckForm(instance=truck)
    
#     if request.method == 'POST':
#         form = TruckForm(request.POST,instance=truck)
#         if form.is_valid():
#             form.save()
#             return redirect('truckregister:index') 

#     context = {'form': form} 
#     return render (request, 'truckregister/update_truck.html',context)


# def deleteTruckView(request, pk):
#     truck = Truck.objects.get(id=pk)
#     context={'item':truck} 
#     if request.method=='POST':
#         truck.delete()
#         return redirect('truckregister:index') 

#     return render(request, 'truckregister/delete_truck.html', context)