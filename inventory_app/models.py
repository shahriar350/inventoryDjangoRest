import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from basic_module_app.models import ProductInit, Company, Category, Type, Color
from staff_app.models import Employee, Supplier
import uuid

User = get_user_model()


class ProductDetailsInit(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_admin_purchase_orders")
    code = models.CharField(max_length=255, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True,unique=True)
    product = models.ForeignKey(ProductInit, on_delete=models.CASCADE, related_name="get_product_purchase_orders")
    sr_visit_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="get_sr_products",
                                      limit_choices_to={'sr': True})  # sr visit
    sr_visit_return = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.barcode + "-> " + self.product.name


class PurchaseOrderGroup(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    flat_discount_percent = models.IntegerField(null=True, blank=True)
    flat_discount_amount = models.IntegerField(null=True, blank=True)
    net_total = models.DecimalField(decimal_places=2, max_digits=10)
    adjust_amount = models.DecimalField(decimal_places=2, max_digits=10)
    pay_amount = models.DecimalField(decimal_places=2, max_digits=10)
    Running_due = models.DecimalField(decimal_places=2, max_digits=10)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_customer_purchase_order_finance")
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name="get_supplier_purchase_order_finance")


class PurchaseOrder(models.Model):
    purchase_group = models.ForeignKey(PurchaseOrderGroup, related_name="get_purchase_group_all",
                                       on_delete=models.SET_NULL, null=True)
    product_init = models.OneToOneField(ProductDetailsInit, on_delete=models.CASCADE,
                                        related_name="get_product_purchase_order")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="get_company_purchase_orders")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="get_category_purchase_orders")
    pin_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="get_type_purchase_orders")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="get_color_purchase_orders")
    warranty_limit = models.CharField(max_length=255, null=True, blank=True)
    rp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.PositiveIntegerField(null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_total_price(self):
        return self.dp * self.quantity - self.discount_amount

    def __str__(self):
        return self.company.name


class SalesOrder(models.Model):  # selling to customer and get some money from him.
    product_init = models.OneToOneField(ProductDetailsInit, on_delete=models.CASCADE,
                                        related_name="get_product_sales_order")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_customer_sales_orders",
                                 limit_choices_to={'customer': True})
    sales_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approve = models.BooleanField(default=False)  # customer or admin can approve that he received the product.

    def __str__(self):
        return self.customer.name


class SalesReturn(models.Model):
    product_init = models.OneToOneField(ProductDetailsInit, on_delete=models.CASCADE,
                                        related_name="get_product_sales_return")

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_customer_sales_returns",
                                 limit_choices_to={'customer': True})
    sr = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_sales_returns")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.name


class CompanyReturn(models.Model):
    product_init = models.OneToOneField(ProductDetailsInit, on_delete=models.CASCADE,
                                        related_name="get_product_company_return")
    dp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="get_supplier_sales_returns")

    def __str__(self):
        return str(self.dp)
