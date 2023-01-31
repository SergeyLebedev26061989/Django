from django.shortcuts import render, redirect
import csv
from .models import Phone

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_mode = request.GET.get('sort')
    p = Phone.objects.all()
    if sort_mode == 'name':
        p = p.order_by('name')
    elif sort_mode == 'max_price':
        p = p.order_by('-price')
    elif sort_mode == 'min_price':
        p = p.order_by('price')

    # ph = Phone.objects.order_by('price')
    context = {"phones": p}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p = Phone.objects.get(slug=request.get_full_path().split('/')[-2])
    context = {"phone": p}
    return render(request, template, context)

