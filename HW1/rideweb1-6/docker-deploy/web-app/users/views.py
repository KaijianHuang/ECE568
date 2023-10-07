from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .forms import UserRegForm, DriverRegForm, UserEditForm, DriverEditForm
from django.contrib.auth.decorators import login_required
from .models import Driver,Rider

def intro(request):
    return render(request, 'users/intro.html')

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
        else:
            form = UserRegForm()
            return render(request, 'users/user_register.html',{'form':form})
    else:
        form = UserRegForm()
        return render(request, 'users/user_register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

@login_required
def RegisterAsDriver(request):
    if request.method == 'GET':
        if len(Driver.objects.filter(user_id=request.user.id))!=0:
            return redirect('driver')
        else:
            form = DriverRegForm()
            return render(request, 'users/RegisterAsDriver.html', {'form':form})   
    else:
        form = DriverRegForm(request.POST)
        if form.is_valid():
            birth = form.cleaned_data['Birth']
            vtype = form.cleaned_data['Vtype']
            plateNum = form.cleaned_data['PlateNum']
            brand = form.cleaned_data['Brand']
            model = form.cleaned_data['Model']
            color = form.cleaned_data['Color']
            MaxP = form.cleaned_data['maxP']
            licenseNum = form.cleaned_data['LicenseNum']
            special = form.cleaned_data['Special']
            new_driver = Driver(user = request.user, Brith=birth,LicenseNum=licenseNum,Vtype=vtype,
                    Brand=brand,Model=model,PlateNum=plateNum,maxP=MaxP,Special=special, Color = color)
            new_driver.save()
            messages.success(request, f'Successfully registered as a driver!')
            return redirect('driver')
      
@login_required
def driver(request):
    current_driver = Driver.objects.filter(user_id = request.user.id)
    if len(current_driver) != 0:
        return  render(request, 'users/driverInterface.html')
    else:
        return redirect('RegisterAsDriver')

@login_required
def EditAsUser(request):
    if request.method == 'GET':
        form = UserEditForm()
        return render(request, 'users/EditAsUser.html', {'form':form})
    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            request.user.rider.phone = form.cleaned_data['phone']
            request.user.save()
            request.user.rider.save()
            messages.success(request, f'Successfully updated!')
            return redirect('profile')
        else:
            form = UserEditForm()
            return render(request, 'users/EditAsUser.html',{'form':form})

@login_required
def EditAsDriver(request):
    if request.method == 'GET':
        form = DriverEditForm()
        return render(request, 'users/EditAsDriver.html', {'form':form})
    else:
        form = DriverEditForm(request.POST)
        if form.is_valid():
            request.user.driver.Vtype = form.cleaned_data['Vtype']
            request.user.driver.PlateNum = form.cleaned_data['PlateNum']
            request.user.driver.Brand = form.cleaned_data['Brand']
            request.user.driver.Model = form.cleaned_data['Model']
            request.user.driver.Color = form.cleaned_data['Color']
            request.user.driver.maxP = form.cleaned_data['maxP']
            request.user.driver.LicenseNum = form.cleaned_data['LicenseNum']
            request.user.driver.Special = form.cleaned_data['Special']
            request.user.save()
            request.user.driver.save()
            messages.success(request, f'Successfully updated!')
            return redirect('driver')
        else:
            form = DriverEditForm()
            return render(request, 'users/EditAsDriver.html',{'form':form})


