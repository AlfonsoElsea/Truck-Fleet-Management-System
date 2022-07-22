from audioop import reverse
from django.db import models
from django.contrib import admin
# Camion

    # Marca 
    # Modelo
    # Año de fabricación
    # color
    # numero de licencia de opercion del camion
    # millas que tiene el odómetro
    # según las millas iniciales poner una aleta de mantenimiento según un dato de millas que se ponga sume con el dato inicial y mande alerta de mantenimiento 100 millas antes.

# Chofer
    # nombre del chofer
    # numero de licencia del chofer.

# Trabajador
    # id


class Truck(models.Model):
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    year = models.IntegerField()
    color = models.CharField(max_length=10)
    truck_license_number = models.CharField(max_length=15)
    odometer = models.IntegerField()
    miles_for_maintenance = models.IntegerField()
   
    @admin.display(boolean=True)
    def needs_maintenace(self):
        return self.miles_for_maintenance-self.odometer <=100
   
    @property
    def Needs_maintenace(self):
        if self.miles_for_maintenance-self.odometer <=100:
            return True
        else:
            return False

    @property
    def to_maintenance(self):
        return self.miles_for_maintenance-self.odometer
        
    @property
    def total_trucks(self):
        return Truck.objects.count()
        

    def __str__(self) -> str:
        return self.color+" " +self.brand +" "+self.model+ " "+ str(self.year) 

    # def needs_maintenance(self):
    #     return self.odometer>= self.miles_for_maintenance-100

    def get_absolute_url(self):
        return reverse('truck', kwargs={'pk':self.pk})
    

    
class Driver(models.Model):
    name = models.CharField(max_length=200)
    license_number = models.IntegerField(default=0)
    truck = models.ForeignKey(Truck, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name + " Drives a "+ self.truck.brand



    


