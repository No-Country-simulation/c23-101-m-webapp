from django.db import models
from django.utils.timezone import now
from apps.product.models import Product
from apps.users.models import CustomUser

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2, editable=False)
    date = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.sale_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sale of {self.product.name} ({self.quantity})"

class ProfitReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="profit_reports")
    total_sales = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    total_profit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def update_report(self):
        sales = Sale.objects.filter(product=self.product)
        self.total_sales = sales.aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        self.total_revenue = sales.aggregate(models.Sum('total'))['total__sum'] or 0.00
        self.total_profit = self.total_revenue - (self.product.purchase_price * self.total_sales)
        self.save()

    def __str__(self):
        return f"Profit Report for {self.product.name}"
