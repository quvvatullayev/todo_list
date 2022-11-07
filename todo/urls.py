"""todo URL Configuration

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
from todo_app.views import GetUser,Add_list, Updaet_list, Remov_list, Get_all
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getUser/', GetUser.as_view()),
    path('add_list/', Add_list.as_view()),
    path('update_list/<int:id>', Updaet_list.as_view()),
    path('remov_list/<int:id>', Remov_list.as_view()),
    path('get_all/', Get_all.as_view())
]
