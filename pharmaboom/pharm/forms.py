from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = models.ProductEntry
        fields = ['drug', 'amount', 'price']
        widgets = {
            'drug': forms.Select(),
            'amount': forms.TextInput,
            'price': forms.TextInput,

        }

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = models.Pharmacy
        fields = ['name', 'pharm_chain', 'status', 'city', 'address']
        widgets = {
            'name': forms.TextInput(),
            'pharm_chain': forms.Select(),
            'status': forms.Select(),
            'city': forms.Select(),
            'address': forms.TextInput(),
        }


class DrugForm(forms.ModelForm):
    class Meta:
        model = models.Drug
        fields = ['name', 'corp', 'brand', 'status', 'drug_form', 'drug_type', 'photo', 'price', 'amount']
        widgets = {
            'name': forms.TextInput(),
            'corp': forms.Select(),
            'brand': forms.Select(),
            'status': forms.Select(),
            'drug_form': forms.Select(),
            'drug_type': forms.Select(),
            'photo': forms.FileInput(),
            'price': forms.NumberInput(),
            'amount': forms.NumberInput(),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['drug',  'pharmacy', 'quantity', 'order_status', 'date_delivery']
        widgets = {
            'drug': forms.Select(),
            'pharmacy': forms.Select(),
            'quantity': forms.NumberInput(),
            'order_status': forms.Select(),
            'date_delivery':forms.DateInput()
        }


class CreateUserForm(UserCreationForm):
    email = forms.CharField(
        label="E-mail",
        widget=forms.EmailInput(),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user
