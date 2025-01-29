from rest_framework.viewsets import ModelViewSet
from django.db import models
from django.shortcuts import render
from rest_framework.decorators import action 
from .models import Product, Category
from rest_framework.response import Response
from django.views.generic.base import TemplateView
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_products = self.queryset.filter(stock__lt=models.F('min_stock_threshold'))
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        # Detectar si el cliente solicita explícitamente JSON
        if 'application/json' in request.headers.get('Accept', ''):
            return super().list(request, *args, **kwargs)

        # Por defecto, renderizar HTML
        return render(request, 'index.html', {'products': self.queryset.all()})

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

