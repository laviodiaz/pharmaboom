from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group
from django import template

from django.http import HttpResponse
from django.urls import reverse_lazy
import datetime

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models
from . import forms
from . import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, \
    DestroyAPIView

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class ProductListAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


def main(request):
    return render(request, 'main.html')


def add_prod_entry(request):
    if request.method == 'POST':
        form = forms.ProductEntryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product_from_db = get_object_or_404(models.Product, drug=product.drug)
            amount = product.amount + product_from_db.amount
            price = (product.price * product.amount + product_from_db.amount * product_from_db.price) / amount
            product_from_db.amount = amount
            product_from_db.price = price
            product_from_db.save()
            return redirect('products_list')
    else:
        form = forms.ProductEntryForm()
    return render(request, 'product_entry.html', {'form': form})


def manager_edit(request):
    return render(request, 'manager_edit.html')


class PharmListView(ListView):
    model = models.Pharmacy
    template_name = 'pharmacies.html'
    context_object_name = 'pharmacies'


class ProductListView(ListView):
    model = models.Product
    template_name = 'products.html'
    context_object_name = 'products'


class PharmDetailView(DetailView):
    model = models.Pharmacy
    template_name = 'pharm_detail.html'
    context_object_name = 'pharmacy'


class PharmCreateView(CreateView):
    model = models.Pharmacy
    form_class = forms.PharmacyForm
    template_name = 'pharmacy_create.html'
    success_url = reverse_lazy('ph_list')


class PharmUpdateView(UpdateView):
    model = models.Pharmacy
    form_class = forms.PharmacyForm
    template_name = 'pharm_update.html'
    success_url = reverse_lazy('ph_list')


def confirm_delete_pharm(request, pk):
    pharmacy = get_object_or_404(models.Pharmacy, pk=pk)
    return render(request, 'conf_delete_pharm.html', {'pharmacy': pharmacy})


def confirm_delete_order(request, pk):
    order = get_object_or_404(models.Order, pk=pk)
    if (order.date_delivery - datetime.date.today()).days >= 1:
        return render(request, 'confirm_delete_order.html', {'order': order})
    else:
        return render(request, 'fail_delete_order.html', {'order': order})


class PharmDeleteView(DeleteView):
    model = models.Pharmacy
    success_url = reverse_lazy('ph_list')
    template_name = 'conf_delete_pharm.html'


class DrugListView(ListView):
    model = models.Drug
    template_name = 'drugs.html'
    context_object_name = 'drugs'


class ProductListView(ListView):
    model = models.Product
    template_name = 'products.html'
    context_object_name = 'products'


class DrugDetailView(DetailView):
    model = models.Drug
    template_name = 'drug_detail.html'
    context_object_name = 'drug'


class DrugCreateView(CreateView):
    model = models.Drug
    form_class = forms.DrugForm
    template_name = 'drug_create.html'
    success_url = reverse_lazy('drugs_list')


def create_order(request):
    if request.method == 'POST':
        form = forms.CreatingOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product = get_object_or_404(models.Product, drug=order.drug)
            order.price = product.price
            order.amount = order.quantity * order.price
            order.customer = request.user
            if order.quantity <= product.amount:
                order.save()
                return redirect('orders_list')
            else:
                return redirect('orders_list')
    else:
        form = forms.CreatingOrderForm()
    return render(request, 'order_create.html', {'form': form})

# class OrderListView(ListView):
#     model = models.Order
#     template_name = 'orders.html'
#     context_object_name = 'orders'

def is_ready_or_no(x):
    return str(x) == "Выполнен"


def orders(request):
    user = request.user
    if user.groups.filter(name='client').exists():
        queryset = models.Order.objects.filter(customer = request.user)
        is_client = True
    else:
        queryset = models.Order.objects.all
        is_client = False
    return render(request, 'orders.html', {'orders': queryset, 'is_client':is_client, 'is_ready_or_no': is_ready_or_no})

class OrderDeleteView(DeleteView):
    model = models.Order
    success_url = reverse_lazy('orders_list')
    template_name = 'order_delete.html'

class OrderUpdateView(UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    template_name = 'order_update.html'
    success_url = reverse_lazy('orders_list')


def order_update(request, pk):
        order = get_object_or_404(models.Order, pk=pk)
        if request.method == 'POST':
            form = forms.OrderForm(request.POST, request.FILES, instance=order)
            if form.is_valid():
                order = form.save(commit=False)
                product_from_db = get_object_or_404(models.Product, drug=order.drug)
                order.save()
                if smb_to_str(order.order_status) == "Выполнен":
                    product_from_db.amount -= order.quantity
                    product_from_db.save()
                return redirect('orders_list')

        else:
            form = forms.OrderForm(instance=order)
        return render(request, 'order_update.html', {'form': form})


class DrugUpdateView(UpdateView):
    model = models.Drug
    form_class = forms.DrugForm
    template_name = 'drug_update.html'
    success_url = reverse_lazy('drugs_list')


def confirm_delete_drug(request, pk):
    drug = get_object_or_404(models.Drug, pk=pk)
    return render(request, 'conf_delete_drug.html', {'drug': drug})


class DrugDeleteView(DeleteView):
    model = models.Drug
    success_url = reverse_lazy('drugs_list')
    template_name = 'conf_delete_drug.html'


def sign_out(request):
    logout(request)
    return redirect('main')


def sign_up(request):
    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='client'))
            login(request, new_user)
            return redirect('main')
        else:
            return render(request, 'sign_up.html', {'form': form})
    else:
        form = forms.CreateUserForm()
        return render(request, 'sign_up.html', {'form': form})


def is_manager(user):
    return user.groups.filter(name='manager').exists()


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            if is_manager(user):
                return redirect('manager_edit')
            else:
                return redirect('products_list')
        else:
            return render(request, 'sign_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'sign_in.html', {'form': form})
