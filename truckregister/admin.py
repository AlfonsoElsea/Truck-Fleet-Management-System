from attr import fields
from django.contrib import admin
from .models import Truck, Driver


class TruckAdmin(admin.ModelAdmin):
    list_display = ('truck_license_number','brand','model','color','odometer','needs_maintenace')
    
    



class DriverAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','license_number', 'truck')

admin.site.register(Truck, TruckAdmin)
admin.site.register(Driver,DriverAdmin)

# Register your models here.
