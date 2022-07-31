from contextlib import contextmanager
import MySQLdb
from django.apps import AppConfig, apps
from django.db import connection, models
from django.contrib import admin
from django.urls import reverse

from truckregister.apps import TruckregisterConfig
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
    brand                 = models.CharField(max_length=15)
    model                 = models.CharField(max_length=15)
    year                  = models.IntegerField()
    color                 = models.CharField(max_length=10)
    truck_license_number  = models.CharField(max_length=15)
    odometer              = models.IntegerField()
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

    
    def get_absolute_url(self):
        return reverse('truckregister:truck_detail', kwargs={'pk':self.pk})
    

    
class Driver(models.Model):
    name             = models.CharField(max_length=50)
    license_number   = models.IntegerField()
    truck            = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True, blank= True)

    def __str__(self) -> str:
        return self.name + " Drives a "+ self.truck.brand

        

# Get tables descriptions
def getTableFromModel(model):
    return str(__package__)+"_"+model.__name__

def tableDesc(table="testdynamic_driver"):

    @contextmanager
    def _db_cursor():
        cursor = connection.cursor()
        yield cursor
        cursor.close()

    with _db_cursor() as c:
      return  connection.introspection.get_table_description(c, table)

# Get database field types supported
def getFieldTypes():
    ft =  MySQLdb.constants.FIELD_TYPE
    return {getattr(ft,k):k for k in dir(ft) if not k.startswith('_')}

#Get a list of fieldtypes
def getFieldTypesList():
    typelist=[]
    fieldtypes = getFieldTypes()
    for _,type in fieldtypes.items() :
        typelist.append(type)
    return typelist



# Get tables fields
def getAllFieldsTable(model):
    conn = tableDesc(getTableFromModel(model))
    return {field for field in conn }

def unregister_model(app_label, model_name):
        try:
            del apps.all_models[app_label][model_name.lower()]
        except KeyError as err:
            raise LookupError("'{}' not found.".format(model_name)) from err


# Create the new field
def createFieldForNewColumn(fieldname,fieldtype,model):



        if fieldtype=="LONG":
            newfield=models.IntegerField(fieldname,blank=True, null=True)

        elif fieldtype=="VAR_STRING":
            newfield=models.CharField(fieldname,max_length=20,blank=True, null=True)

        elif fieldtype=="LONGLONG":
            newfield=models.BigIntegerField(fieldname,blank=True, null=True)

            
        elif fieldtype=="VARCHAR":
            newfield=models.CharField(verbose_name=fieldname, name=fieldname,max_length=20,blank=True, null=True,db_column=fieldname)

            
            
        # elif fieldtype=="VARCHAR":
        #     newfield=models.BooleanField(verbose_name=fieldname, name=fieldname,max_length=20,blank=True, null=True,db_column=fieldname)

        newfield.column=str(fieldname)
        newfield.attname=fieldname

        model.add_to_class(fieldname,newfield)
        
        # newfield.contribute_to_class(model,fieldname)

        return newfield



def addNewColumnInDB(model,field):
       with connection.schema_editor() as shem:
            
            shem.add_field(model,field)


# Get my models names
def getModelsNames():
    models=getModels()
    models_names=[]

    for model in models:
        models_names.append( model.__name__)

    return models_names

def getModelbyName(name):
    models=getModels()


    for model in models:
        if str(model.__name__).lower()==name:
            return model

    return None

# Get my models
def getModels():
    models =apps.get_models(include_auto_created=False,include_swapped=False)
    aux=[]
    for model in models:
        if str(model.__module__).startswith(__package__):
            aux.append(model)
    return aux

# Update model's fields
def updateModels(model=Driver,*args,**kargs):
    fieldtypes = getFieldTypes()
    
    for model in getModels():
        
        fields = getAllFieldsTable(model)

        modelfields= model._meta.get_fields()
        # print(modelfields)

        fieldSet = {fieldField.name for fieldField in modelfields}

        for field in fields:
            if field.name not in fieldSet and not str(field.name).endswith('_id') :

                createFieldForNewColumn(field.name,fieldtypes[field.type_code],model)
        

# model.add_to_class(fieldname,newfield)
        
# newfield.contribute_to_class(model,fieldname)
# setattr(Truck,"city",models.CharField(max_length=20,blank=True, null=True))
# Truck._meta.add_field(models.CharField("city","city",max_length=20,blank=True, null=True))

    


