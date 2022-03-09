from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()
from django.db import models


# # Create your models here.
# class RoleDesignation(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class AdminDesignation(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_admin_designations")

    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    designation = models.ForeignKey(AdminDesignation, on_delete=models.CASCADE,
                                    related_name="get_designation_employees", null=True, blank=True)
    # role_designation = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True,
    #  related_name="get_group_employees")
    religion = models.CharField(max_length=255, null=True, blank=True)
    departmentID = models.CharField(max_length=255, null=True, blank=True)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=255, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    reference_by = models.CharField(max_length=255, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    advance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_admin_employees")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_all_suppliers")
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SupplierBank(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="get_supplier_banks")
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.bank_name
