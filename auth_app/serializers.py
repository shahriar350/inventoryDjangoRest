from django.contrib.auth.models import Permission
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth_app.models import User, UserDetails


class UserDetailsSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=None)

    class Meta:
        model = UserDetails
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    get_user_details = UserDetailsSerializer()
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True)
    admin_user = serializers.HiddenField(default=None)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    extra_kwargs = {
        'password': {'write_only': True}
    }

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'phone_number',
            'password',
            'image',
            'admin',
            'sr',
            'counter',
            'customer',
            'supplier',
            'showroom',
            "user_permissions",
            "permanent_address",
            "present_address",
            "shop_name",
            "admin_user",
            "created_by",
            "get_user_details",
        )

    def create(self, validated_data):
        with transaction.atomic():
            all_details = validated_data.pop('get_user_details')
            permissions = validated_data.pop('user_permissions')
            self_user = User.objects.get(id=validated_data['created_by'].id)
            print("current user is: ", self_user)
            check_admin = True
            temp_user = self_user
            while check_admin:
                curr_user = temp_user
                if curr_user.admin:
                    validated_data['admin_user'] = curr_user
                    check_admin = False
                else:
                    if curr_user.admin_user_id is None:
                        raise ValidationError("Admin cannot find. Please contact to super admin or admin.")
                    temp_user = User.objects.get(id=curr_user.admin_user_id)
                    print("got user: -> ", temp_user)

            user = User.objects.create_user(**validated_data)
            # AdminChild.objects.create()
            user.user_permissions.set(permissions)
            UserDetails.objects.create(user=user, **all_details)
            return User.objects.prefetch_related("get_user_details", "user_permissions").get(id=user.id)


#
# class UserRegistrationSerializer(serializers.Serializer):
#     user = UserSerializer()
#     details = UserDetailsSerializer()

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class SingleUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(min_length=11, max_length=11)
    password = serializers.CharField()


class CustomerSearchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"


class CustomerSearchSerializer(serializers.ModelSerializer):
    get_user_details = CustomerSearchDetailsSerializer()

    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "phone_number",
            "customer",
            "created_by",
            "permanent_address",
            "present_address",
            "shop_name",
            "get_user_details",
        )
