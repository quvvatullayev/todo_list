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

class Updaet_list(View):
    def post(self, request, id):
        todo = TodoItem.objects.get(id = id)
        todo.task = request.POST.get('task')
        todo.title = request.POST.get('title')
        # todo.status = request.POST.get('status')
        todo.description = request.POST.get('description')
        todo.save()
        return JsonResponse(TodoItem.objects.get(id = id).todo_json())

class Remov_list(View):
    def get(self, request ,id):
        tood = TodoItem.objects.get(id = id)
        tood.delete()
        return JsonResponse({'Remov list':"OK status_code:200"})

class Get_all(View):
    def get(self, request):
        todo_all = TodoItem.objects.all()
        todo_all_json = {'results':[]}
        for i in todo_all:
            todo_all_json['results'].append(i.todo_json())
        return JsonResponse(todo_all_json)

class Get_id(View):
    def get(self, request, id):
        todo = TodoItem.objects.get(id = id)
        todo_json = todo.todo_json()
        return JsonResponse(todo_json)