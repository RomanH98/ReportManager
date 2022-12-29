from django.shortcuts import render, redirect
from .models import SalesPlan


def get_plan_start(request):
    return render(request, 'get_plan/get_plan.html')

def set_plan(request):
    if (request.method == "POST"):
        obj, created = SalesPlan.objects.get_or_create(store_name= request.POST.get('store_name'))
        obj.product1 = request.POST.get('product1')
        obj.product2 = request.POST.get('product2')
        obj.save()
        return render(request, 'get_plan/save.html')

def all_stores(request):
    stores = SalesPlan.objects.all()
    return render(request, 'get_plan/all_stores.html', {'data': stores})
