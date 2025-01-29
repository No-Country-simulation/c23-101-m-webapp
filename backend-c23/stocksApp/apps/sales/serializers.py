from rest_framework import serializers
from .models import Sale, ProfitReport

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'product', 'user', 'quantity', 'sale_price', 'total', 'date']

class ProfitReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitReport
        fields = ['id', 'product', 'total_sales', 'total_revenue', 'total_profit']