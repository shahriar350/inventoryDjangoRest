from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from auth_app.models import User
from auth_app.serializers import CustomerSearchSerializer
from inventory_app.models import PurchaseOrder, ProductDetailsInit, SalesOrder, PurchaseOrderGroup

#
# class PurchaseOrderView(ListCreateAPIView):
#     serializer_class = PurchaseOrderSerializer
#
#     def get_queryset(self):
#         return PurchaseOrder.objects.select_related("product_init").filter(product_init__user=self.request.user).all()
#
#     def perform_create(self, serializer):
#         prodValid =ProductDetailsInit.objects.create(
#             user=self.request.user, code=serializer.validated_data['product_init']['code'],
#             barcode=serializer.validated_data['product_init']['barcode'],
#             product=serializer.validated_data['product_init']['product']
#         )
#         serializer.save(product_init=prodValid)
#
#
from inventory_app.serializers import PurchaseOrderManySerializer
from staff_app.models import Supplier


class PurchaseOrderView(CreateAPIView):
    serializer_class = PurchaseOrderManySerializer

    def post(self, request, *args, **kwargs):
        serializer = PurchaseOrderManySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            group_product = PurchaseOrderGroup.objects.create(
                flat_discount_percent=serializer.validated_data['flat_discount_percent'],
                flat_discount_amount=serializer.validated_data['flat_discount_amount'],
                net_total=serializer.validated_data['net_total'],
                adjust_amount=serializer.validated_data['adjust_amount'],
                pay_amount=serializer.validated_data['pay_amount'],
                Running_due=serializer.validated_data['Running_due'],
                admin=request.user,
                supplier=serializer.validated_data['supplier'],
            )
            print("id is: ",serializer.validated_data['supplier'])
            supplier = Supplier.objects.get(id=serializer.validated_data['supplier'].id)
            supplier.due = serializer.validated_data['Running_due']
            supplier.save()
            for purchase in serializer.validated_data['purchases']:
                product_init = purchase['product_init']
                pro_init = ProductDetailsInit.objects.create(user=request.user, **product_init)
                PurchaseOrder.objects.create(purchase_group=group_product, product_init=pro_init,
                                             company=purchase['company'],
                                             category=purchase['category'],
                                             pin_type=purchase['pin_type'],
                                             color=purchase['color'],
                                             warranty_limit=purchase['warranty_limit'],
                                             rp=purchase['rp'],
                                             mrp=purchase['mrp'],
                                             dp=purchase['dp'],
                                             quantity=purchase['quantity'],
                                             discount_percent=purchase['discount_percent'],
                                             discount_amount=purchase['discount_amount'],
                                             total=purchase['total'],
                                             )

        return Response(data=serializer.data)

    # def get_queryset(self):
    #     return PurchaseOrder.objects.select_related("product_init").filter(product_init__user=self.request.user).all()
    #
    # def perform_create(self, serializer):
    #     prodValid =ProductDetailsInit.objects.create(
    #         user=self.request.user, code=serializer.validated_data['product_init']['code'],
    #         barcode=serializer.validated_data['product_init']['barcode'],
    #         product=serializer.validated_data['product_init']['product']
    #     )
    #     serializer.save(product_init=prodValid)

#
# class SalesOrderView(ListCreateAPIView):
#     serializer_class = SalesOrderSerializer
#
#     def get_queryset(self):
#         return SalesOrder.objects.all()
#
# class ProductDetailsInitSearch(ListAPIView):
#     serializer_class = CustomerSearchSerializer
#
#     def get_queryset(self):
#         user = User.objects.get(id=self.request.user.id)
#         return ProductDetailsInit.objects.filter(customer=True, admin_user=user.admin_created)
#
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['phone_number', 'present_address', 'shop_name']
