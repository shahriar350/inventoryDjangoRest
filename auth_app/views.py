from django.contrib.auth import login, authenticate
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, authentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import User
from auth_app.serializers import UserSerializer, PermissionSerializer, SingleUserSerializer, CustomerSearchSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated


class UserRegistration(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.prefetch_related("user_permissions", 'get_user_details').all()


#     serializer_class =

class AdminPermissions(ListAPIView):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        return self.request.user.user_permissions.all()


class UserLogin(CreateAPIView):
    serializer_class = SingleUserSerializer
    queryset = User.objects.first()

    def post(self, request, *args, **kwargs):
        # serializer = SingleUserSerializer(data=request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            groups = user.user_permissions.all().values_list('codename', flat=True)
            last_login = user.last_login
            user.last_login = timezone.now()
            user.save()
            if last_login is None:
                return Response({
                    'group': groups,
                    'token': token.key,
                    'first_time': True
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'group': groups,
                    'token': token.key
                }, status=status.HTTP_200_OK)
            # groups = user.user_permissions.all()
            # groups = user.get_all_permissions()
        else:
            raise ValidationError('Please provide correct credential')


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        Token.objects.get(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)


class CustomerGetSearch(ListAPIView):
    serializer_class = CustomerSearchSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        return User.objects.prefetch_related("get_user_details").filter(customer=True, created_by=user.created_by)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone_number', 'present_address', 'shop_name']
