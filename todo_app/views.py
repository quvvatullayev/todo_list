from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import TodoItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class GetUser(View):
    def post(self, requser):
        username = requser.POST['username']
        password = requser.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            return JsonResponse({
                'id':user.id,
                'password':user.password,
                'username':user.username
            })
        return JsonResponse({'None User':False})

class Add_list(View):
    def post(self, request):
        todo = TodoItem(
            title = request.POST['title'],
            task = request.POST['task']
        )
        todo.save()
        return JsonResponse({'Add task':'OK status_code:200'})