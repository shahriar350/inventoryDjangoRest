from basic_module_app.models import Bank, Company, Category, Type, Color, Godown, Route, ProductInit
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Company
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Type
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Color
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bank
        fields = "__all__"


class GodownSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Godown
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Route
        fields = "__all__"


class ProductInitSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductInit
        fields = "__all__"

# class ProductSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#     company = CompanySerializer(read_only=True, allow_null=True)
#     category = CategorySerializer(read_only=True, allow_null=True)
#     type = TypeSerializer(read_only=True, allow_null=True)
#     color = ColorSerializer(read_only=True, allow_null=True)
#
#     class Meta:
#         model = Product
#         fields = "__all__"


# class RoleDesignationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RoleDesignation
#         fields = "__all__"


# class AdminDesignationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdminDesignation
#         fields = "__all__"
