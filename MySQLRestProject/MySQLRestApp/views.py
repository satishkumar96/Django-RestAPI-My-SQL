from django.shortcuts import render
from .models import Customer
from rest_framework import generics
from rest_framework import filters
from .serializers import CustomerSerializer

# Create your views here.

class CustomerCreate(generics.CreateAPIView):
    """API endpoint that allows of a new customer"""
    queryset = Customer.objects.all,
    serializer_class = CustomerSerializer

class CustomerList(generics.ListAPIView):
    """API endpoint that allows customer to be viewed"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'city']

class CustomerDetail(generics.RetrieveAPIView):
    """API endpoint that returns a single customer by pk"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.RetrieveUpdateAPIView):
    """API endpoint that allows a customer record to be updated"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows a customer record to be deleted"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer