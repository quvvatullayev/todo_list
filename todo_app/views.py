from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Todo_list_model

# Create your views here.
class Create_todolist(View):
    def post(self, request):
        r = request.POST
        product = Todo_list_model.objects.create(
            task = r['task'],
            status = r['status'])
        product.save()
        return HttpResponse('OK')

class Delete_list(View):
    def get(self, request, id):
        product = Todo_list_model.objects.get(id = id)
        product.delete()
        return HttpResponse('OK delet')

class All_get_list(View):
    def get(self, request):
        product = Todo_list_model.objects.all()
        json_p = {'result':[]}
        for k in product:
            list_result = json_p['result']
            list_result.append(
                {'id':k.id,
                'task':k.task,
                'status':k.status})
        return JsonResponse(json_p)

class Get_list(View):
    def get(self, request, id):
        product = Todo_list_model.objects.get(id = id)
        json_p = {
            'id':product.id,
            'task':product.task,
            'status':product.status
        }
        return JsonResponse(json_p)

class Update_list(View):
    def post(self, request, id):
        product = Todo_list_model.objects.get(id = id)
        product.task = request.POST['task']
        product.status = request.POST['status']
        product.save()

        json_p = {
            'id':product.id,
            'task':product.task,
            'status':product.status
        }
        return JsonResponse(json_p)