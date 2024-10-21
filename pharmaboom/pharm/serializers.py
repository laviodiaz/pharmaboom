from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
import re


class DrugSerializer(serializers.Serializer):
    class Meta:
        model = models.Drug
        fields = ('pk', 'name', 'corp', 'brand', 'status', 'drug_form', 'drug_type', 'price', 'amount')

class ProductSerializer(serializers.Serializer):
    drug = DrugSerializer(many=False, read_only=True)

    class Meta:
        model = models.Product
        fields = ('pk', 'price', 'drug', 'amount')
