"""rideweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # users side view
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('intro/', users_views.intro, name = 'intro'),
    path('register/',users_views.register, name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('RegisterAsDriver/',users_views.RegisterAsDriver,name='RegisterAsDriver'),
    path('driverInterface/',users_views.driver, name = 'driver'),
    path('EditAsUser/', users_views.EditAsUser, name = 'EditAsUser'),
    path('EditAsDriver/', users_views.EditAsDriver, name = 'EditAsDriver'),
]
