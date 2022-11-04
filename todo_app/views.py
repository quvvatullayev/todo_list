from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import Todo_list_model

# Create your views here.
class Create_todolist(View):
    def post(self, request):
        r = request.POST
        product = Todo_list_model()
        product.task = r.get('task')
        product.status = r.get('status')
        product.save()
        return JsonResponse(product)