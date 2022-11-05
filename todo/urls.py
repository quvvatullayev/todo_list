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
from todo_app.views import Create_todolist, Delete_list, Get_list, All_get_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', All_get_list.as_view()),
    path('create_todo_list/', Create_todolist.as_view()),
    path('delet/<int:id>', Delete_list.as_view()),
    path('get_list/<int:id>', Get_list.as_view())
]
