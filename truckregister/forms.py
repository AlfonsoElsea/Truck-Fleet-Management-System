from .models import Truck, Driver
from attr import fields
from django import forms


from truckregister.models import Truck

# class TruckForm(forms.ModelForm):    
#     # odometer= forms.IntegerField()
    
#     class Meta:
#         model = Truck
#         fields = ('odometer',)
#         labels={
#             'odometer':'',
#         }
            
        

#         widgets={
#             'odometer':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Odometer'}),
#         }

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields= '__all__'
        labels={'brand':'',
        'model':'',
        'year':'',
        'color':'',
        'truck_license_number':'',
        'odometer':'',
        'miles_for_maintenance':'',
        }

# {brand, model, year,color, truck_license_number,odometer,miles_for_maintenance}
        widgets={
            'brand':forms.TextInput(attrs={'class':'form-control','placeholder': 'Brand'}),
            'model':forms.TextInput(attrs={'class':'form-control','placeholder': 'Model'}),
            'year':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Year'}),
            'color':forms.TextInput(attrs={'class':'form-control','placeholder': 'Color'}),
            'truck_license_number':forms.NumberInput(attrs={'class':'form-control','placeholder':'License Number'}),
            'odometer':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Odometer'}),
            'miles_for_maintenance':forms.NumberInput(attrs={'class':'form-control','placeholder':'Miles for Maintenance'}),
            
            }

