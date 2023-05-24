"""agriproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from precisionagri import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name= 'home'),
    path('form/',views.crop,name= 'form'),
    path('loginpage/',views.adminlogin,name = 'loginpage'),
    path('result/<crop>/<n>/<p>/<k>/<t>/<h>/<phv>/<r>/',views.result,name='prediction'),
    path('pdf/<crop>/<n>/<p>/<k>/<t>/<h>/<phv>/<r>/',views.pdf,name='pdf'),
    path('search/',views.search,name='search'),
]
