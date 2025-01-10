from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    description = models.TextField(blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    stock = models.PositiveIntegerField()
    min_stock_threshold = models.PositiveIntegerField(default=10)

    @property
    def selling_price(self):
        return self.purchase_price * (1 + self.margin / 100)

    def is_low_stock(self):
        return self.stock < self.min_stock_threshold

    def __str__(self):
        return self.name
