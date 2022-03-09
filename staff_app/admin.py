from django.contrib import admin

# Register your models here.
from staff_app.models import Supplier, SupplierBank


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ('id','name',)

@admin.register(SupplierBank)
class SupplierBankAdmin(admin.ModelAdmin):
    model = SupplierBank
    list_display = ('supplier','bank_name',)

