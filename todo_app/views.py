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
