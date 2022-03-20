from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from auth_app.models import User


# User = get_user_model()

class Company(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_companies")

    def __str__(self):
        return self.name


class Category(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_categories")

    def __str__(self):
        return self.name


class Type(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_types")

    def __str__(self):
        return self.name


class Color(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_colors")

    def __str__(self):
        return self.name


class Bank(models.Model):
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_banks")

    def __str__(self):
        return self.bank_name + " " + self.account_number


class Route(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    opening_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="bank_routes")
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_routes")

    def __str__(self):
        return self.name


class Godown(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="route_godowns")
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_godowns")

    def __str__(self):
        return self.name


class ProductInit(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="get_category_product_init")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="get_company_product_init")
    opening_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_product_init")

    def get_user_admin(self):
        return User.objects.get(id=self.created_by.admin_user_id)

    def __str__(self):
        return self.name

class RouteUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="get_user_root")
    route = models.ForeignKey(Route,on_delete=models.CASCADE,related_name="get_route_user")
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="get_admin_in_route")