from django.db import transaction
from rest_framework import serializers

from staff_app.models import AdminDesignation, Employee, Supplier, SupplierBank


class AdminDesignationSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AdminDesignation
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Employee
        fields = '__all__'


class SupplierBankSerializer(serializers.ModelSerializer):
    # admin = serializers.HiddenField(default=serializers.CurrentUserDefault())
    supplier = serializers.HiddenField(default=None)

    class Meta:
        model = SupplierBank
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    get_supplier_banks = SupplierBankSerializer(many=True)
    admin = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Supplier
        fields = (
            'id',
            'code',
            'name',
            'owner_name',
            'nid',
            'phone_number',
            'email',
            'image',
            'address',
            'due',
            'admin',
            'get_supplier_banks',
        )

    def create(self, validated_data):
        with transaction.atomic():
            banks = validated_data.pop('get_supplier_banks')
            supplier = Supplier.objects.create(**validated_data)
            for i in banks:
                i['supplier'] = supplier
                print("data is: ",i)
                SupplierBank.objects.create(**i)
            return Supplier.objects.prefetch_related("get_supplier_banks").get(id=supplier.id)
