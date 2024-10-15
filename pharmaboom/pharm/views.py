from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group

from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . import models
from . import forms


def main(request):
    return render(request, 'main.html')


def add_prod_entry(request):
    if request.method == 'POST':
        form = forms.ProductEntryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product_from_db = get_object_or_404(models.Product, pk=product.id)
            adding_price = product.price
            adding_amount = product.amount
            amount = adding_amount + product_from_db.amount
            price = (adding_price * adding_amount + product_from_db.amount * product_from_db.price) / amount
            product.amount = amount
            product.price = price
            product.save()
            return redirect('drugs_list')
    else:
        form = forms.ProductEntryForm
    return render(request, 'product_entry.html', {'form': form})


def manager_edit(request):
    return render(request, 'manager_edit.html')


class PharmListView(ListView):
    model = models.Pharmacy
    template_name = 'pharmacies.html'
    context_object_name = 'pharmacies'


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
    template_name = 'main.html'
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


def is_member(user):
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
            if is_member(user):
                return redirect('manager_edit')
            else:
                return redirect('main')
        else:
            return render(request, 'sign_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'sign_in.html', {'form': form})
