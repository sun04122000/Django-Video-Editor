"""videoeditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from coralcut import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',views.edit_video),
    path('black/',views.black),
    path('paint/',views.paint),
    path('fadein/',views.fade_in),
    path('fadeout/',views.fade_out),
    path('Mirror_x/',views.mirrorx),
    path('Mirror_y/',views.mirrory),
    path('timesymmetry/',views.timesymmetry),
    path('invertcolors/',views.invertcolors),
    path('lumcontrast/',views.lumcontrast),
    path('evensize/',views.evensize),
    path('timemirror/',views.timemirror),
    path('speed/',views.speed),
    path('volume/',views.volume),
    path('rotate/',views.rotate),
    path('gammac/',views.gammac),
]
