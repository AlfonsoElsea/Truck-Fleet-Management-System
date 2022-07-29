from .models import Truck, Driver, updateModels
from attr import attr, fields
from django import forms

updateModels()
class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields= '__all__'
        # labels={'brand':'',
        # 'model':'',
        # 'year':'',
        # 'color':'',
        # 'truck_license_number':'',
        # 'odometer':'',
        # 'miles_for_maintenance':'',
        # }

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

class DriverForm(forms.ModelForm):
    class Meta:
        model= Driver
        exclude=()
        labels= {
           'name':'',
           'last_name':'',
           'license_number':'',
           
        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'license_number':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'License'}),
            'truck':forms.Select(attrs={'class':'form-control','placeholder':'Truck'}),
        }

postinline=forms.inlineformset_factory(Truck, Driver, form=DriverForm, extra=1)


     
class recordTruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'

class recordDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

