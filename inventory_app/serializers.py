from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth_app.models import User
from basic_module_app.models import ProductInit
from basic_module_app.serializers import ProductInitSerializer
from inventory_app.models import CompanyReturn, SalesReturn, SalesOrder, ProductDetailsInit, PurchaseOrder

#
# class ProductDetailsInitSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = ProductDetailsInit
#         fields = (
#             'id',
#             'user',
#             'code',
#             'barcode',
#             'product',
#             'created_at',
#             'updated_at',
#         )
#
#
# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     # product_init_get = ProductDetailsInitSerializer(help_text="Product init data")
#     product_init = ProductDetailsInitSerializer(help_text="Product init data")
#
#     def validate_product_init(self, value):
#         if ProductDetailsInit.objects.filter(product=value['product']).exists():
#             raise ValidationError("This product has already a purchase.")
#         else:
#             return value
#
#     class Meta:
#         model = PurchaseOrder
#         fields = [
#             "id",
#             "company",
#             "category",
#             "pin_type",
#             "color",
#             "warranty_limit",
#             "rp",
#             "mrp",
#             "dp",
#             "quantity",
#             "discount_percent",
#             "discount_amount",
#             "total",
#             "product_init",
#         ]
#
#
# class SalesOrderSerializer(serializers.ModelSerializer):
#     product_init = serializers.PrimaryKeyRelatedField(queryset=ProductDetailsInit.objects.all())
#
#     class Meta:
#         model = SalesOrder
#         fields = "__all__"
#
#
# class SalesReturnSerializer(serializers.ModelSerializer):
#     product_init = serializers.ReadOnlyField()
#
#     class Meta:
#         model = SalesReturn
#         fields = "__all__"
#
#
# class CompanyReturnSerializer(serializers.ModelSerializer):
#     product_init = serializers.ReadOnlyField()
#
#     class Meta:
#         model = CompanyReturn
#         fields = "__all__"
from staff_app.models import Supplier


class ProductDetailsInitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetailsInit
        fields = (
            'id',
            "code",
            "barcode",
            "product",
        )


class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_group = serializers.HiddenField(default=None)
    product_init = ProductDetailsInitSerializer()

    class Meta:
        model = PurchaseOrder
        fields = (
            'id',
            "purchase_group",
            "company",
            "category",
            "pin_type",
            "color",
            "warranty_limit",
            "rp",
            "mrp",
            "dp",
            "quantity",
            "discount_percent",
            "discount_amount",
            "total",
            "product_init",
        )


class PurchaseOrderManySerializer(serializers.Serializer):
    purchases = PurchaseOrderSerializer(many=True)
    flat_discount_percent = serializers.IntegerField(allow_null=True)
    flat_discount_amount = serializers.IntegerField(allow_null=True)
    net_total = serializers.DecimalField(decimal_places=2, max_digits=10, allow_null=True)
    adjust_amount = serializers.DecimalField(decimal_places=2, max_digits=10, allow_null=True)
    pay_amount = serializers.DecimalField(decimal_places=2, max_digits=10, allow_null=True)
    Running_due = serializers.DecimalField(decimal_places=2, max_digits=10, allow_null=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())


class ProductDetailsInitSerializerM(serializers.ModelSerializer):
    get_product_purchase_order = PurchaseOrderSerializer()
    product = ProductInitSerializer()

    class Meta:
        model = ProductDetailsInit
        fields = (
            'admin',
            'code',
            'barcode',
            'product',
            'sr_visit_user',
            'sr_visit_return',
            'get_product_purchase_order',
        )


class SalesOrderSerializer(serializers.ModelSerializer):
    product_init = serializers.PrimaryKeyRelatedField(queryset=ProductDetailsInit.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(customer=True))

    class Meta:
        model = SalesOrder
        fields = "__all__"


class SalesReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReturn
        fields = "__all__"
