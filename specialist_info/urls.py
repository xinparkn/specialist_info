"""specialist_info URL Configuration

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
from . import user
from . import specialist as speci
from . import base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user.login),
    path('signin/', user.signin),
    path('logout/', user.logout),
    path('', base.home),
    path('user/', base.user),
    path('user/changeusername', user.change_username),
    path('user/changepassword', user.change_password),
    path('test/', base.test),
    path('specialist/add/', speci.add_specialist),
    path('specialist/category/', speci.category),
    path('specialist/list/', speci.list_specialist),
    path('specialist/view/', speci.view_specialist),
    path('specialist/del/', speci.del_specialist),
]
