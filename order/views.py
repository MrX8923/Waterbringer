from django.shortcuts import render
from .forms import *
from .json_writer import *


def index(request):
    return render(request, 'index.html', context={'title': 'Главная'})


def water_order(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'lastname': form.cleaned_data['lastname'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'address': form.cleaned_data['address'],
                'months': form.cleaned_data['months'],
                'amount': form.cleaned_data['amount']
            }

            make_json(data, 'order/json_files/clients.json')
            return render(request, 'final.html', context=data)
    else:
        form = OrderForm()
    data = {'title': 'ЗАКАЗ', 'form': form}
    return render(request, 'form.html', context=data)
