from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from InventoryRestApp.permissions import CustomDjangoModelPermission
from basic_module_app.models import Company, Category, Type, Color, Godown, ProductInit, Bank, Route
from basic_module_app.serializers import CompanySerializer, CategorySerializer, TypeSerializer, ColorSerializer, \
    GodownSerializer, ProductInitSerializer, BankSerializer, RouteSerializer


class CompanyCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    # permission_required = ('basic_module.view_company', 'basic_module.add_company','basic_module.change_company', 'basic_module.delete_company',)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ColorCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class GodownCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Godown.objects.all()
    serializer_class = GodownSerializer


class ProductInitCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = ProductInit.objects.all()
    serializer_class = ProductInitSerializer


class BankCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class RouteCRUD(ModelViewSet):
    permission_classes = [CustomDjangoModelPermission]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
