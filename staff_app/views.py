from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from InventoryRestApp.permissions import CustomDjangoModelPermission
from staff_app.models import AdminDesignation, Employee, SupplierBank, Supplier
from staff_app.serializers import AdminDesignationSerializer, EmployeeSerializer, SupplierBankSerializer, \
    SupplierSerializer
from rest_framework.permissions import DjangoModelPermissions


class AdminDesignationCRUD(ModelViewSet):
    serializer_class = AdminDesignationSerializer
    permission_classes = [CustomDjangoModelPermission]

    def get_queryset(self):
        user = self.request.user
        return AdminDesignation.objects.filter(admin=user)


class EmployeeCRUD(ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [CustomDjangoModelPermission]

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(admin=user)


class BankCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    serializer_class = SupplierBankSerializer
    queryset = SupplierBank.objects.all()


class SupplierCRUD(ListCreateAPIView):
    permission_classes = [CustomDjangoModelPermission]
    serializer_class = SupplierSerializer
    # parser_classes = [FormParser, MultiPartParser]

    def get_queryset(self):
        return Supplier.objects.prefetch_related("get_supplier_banks").all()

    # def get_serializer_context(self):
    #     return {'request': self.request}
