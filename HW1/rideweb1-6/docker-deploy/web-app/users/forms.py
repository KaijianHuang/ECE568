from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Driver,Rider
from django.forms.fields import DateInput, DateField, NumberInput

class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100,required=True)
    phone = forms.NumberInput()
    class Meta:
        model = Rider
        fields = ['username','email','password1','password2','first_name','last_name','phone']

class DateInput(forms.DateInput):
    input_type = 'date'

class DriverRegForm(forms.Form):
    Birth = forms.DateField(label='Date of Birth',help_text='month/day/year', 
                                required=True,
                                input_formats = ['%Y-%m-%d'],
                                widget=DateInput(format='%Y-%m-%d'))
    Vtype = forms.ChoiceField(label = 'Vehicle Type', choices = (("Sedan", "Sedan"), ("SUV", "SUV")))
    PlateNum = forms.CharField(label = "Vehicle Plate Number", required = True)
    Brand = forms.CharField(label = "Vehicle Brand", required = True)
    Model = forms.CharField(label = "Vehicle Model", required = True)
    Color = forms.CharField(label = "Vehicle Color", required = True)
    maxP = forms.IntegerField(label = "Max Number of Passenger", required = True) 
    LicenseNum = forms.CharField(label = "License Number", required = True)
    Special = forms.CharField(label = "Special Vehicle Information", required = False)
    class Meta:
        model = Driver
        fields = ['Birth', 'Vtype', 'PlateNum', 'Brand', 'Model', 'Color', 'maxP', 'LicenseNum', 'Special']

class UserEditForm(forms.Form):
    phone = forms.IntegerField()
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

class DriverEditForm(forms.Form):
    Vtype = forms.ChoiceField(label = 'Vehicle Type', choices = (("Sedan", "Sedan"), ("SUV", "SUV")))
    PlateNum = forms.CharField(label = "Vehicle Plate Number", required = True)
    Brand = forms.CharField(label = "Vehicle Brand", required = True)
    Model = forms.CharField(label = "Vehicle Model", required = True)
    Color = forms.CharField(label = "Vehicle Color", required = True)
    maxP = forms.IntegerField(label = "Max Number of Passenger", required = True) 
    LicenseNum = forms.CharField(label = "License Number", required = True)
    Special = forms.CharField(label = "Special Vehicle Information", required = False)
    class Meta:
        model = Driver
        fields = ['Vtype', 'PlateNum', 'Brand', 'Model', 'Color', 'maxP', 'LicenseNum', 'Special']
