from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from rest_framework.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number, password, **extra_fields):
        if User.objects.filter(phone_number=phone_number).count() > 0:
            raise ValidationError(_('Phone number is already taken'))
        if not phone_number:
            raise ValidationError(_('Phone number is required'))
        if len(phone_number) != 11:
            raise ValidationError(_('Phone number must be 11 number'))
        if phone_number[0] != '0' and phone_number[1] != '1':
            raise ValidationError(_('Phone number must be start with 01'))
        if not password:
            raise ValidationError(_('Password is required'))
        if not phone_number.isnumeric():
            raise ValidationError(_('Phone number must be numeric'))
        extra_fields.setdefault("active", True)
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.name = name.title()
        user.save(using=self._db)
        return user

    def create_sr(self, name, phone_number, password, **extra_fields):
        extra_fields.setdefault('sr', True)
        extra_fields.setdefault('active', True)
        return self.create_user(name, phone_number, password, **extra_fields)

    def create_counter(self, name, phone_number, password, **extra_fields):
        extra_fields.setdefault('counter', True)
        extra_fields.setdefault('active', True)
        return self.create_user(name, phone_number, password, **extra_fields)

    def create_customer(self, name, phone_number, password, **extra_fields):
        extra_fields.setdefault('customer', True)
        extra_fields.setdefault('active', True)
        return self.create_user(name, phone_number, password, **extra_fields)

    def create_supplier(self, name, phone_number, password, **extra_fields):
        extra_fields.setdefault('supplier', True)
        extra_fields.setdefault('active', True)
        return self.create_user(name, phone_number, password, **extra_fields)

    def create_superuser(self, name, phone_number, password, **extra_fields):
        extra_fields.setdefault("staff", True)
        extra_fields.setdefault("superuser", True)
        extra_fields.setdefault("admin", True)
        extra_fields.setdefault("active", True)
        user = self.create_user(name, phone_number, password, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    name = models.CharField(_('Your name'), max_length=100,
                            validators=[
                                RegexValidator(
                                    regex=r'^[a-zA-Z ]*$',
                                    message=_('name must be Alpha'),
                                ),
                            ]
                            )
    phone_number = models.CharField(unique=True, max_length=11, validators=[
        RegexValidator(
            regex=r'(^(01)[3-9]\d{8})$',
            message=_('Please provide a valid 11 digit phone number.'),
        ),
    ])
    superuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    sr = models.BooleanField(default=False)
    counter = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    supplier = models.BooleanField(default=False)
    showroom = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    permanent_address = models.TextField(null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    shop_name = models.CharField(max_length=255, null=True, blank=True)
    admin_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="get_admin_users")
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name="get_creator_user")
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_first_time(self):
        start = self.date_joined - timedelta(seconds=10)
        end = self.date_joined + timedelta(seconds=10)
        if start <= end:
            return start <= self.updated_at < end
        else:  # over midnight e.g., 23:30-04:15
            return start <= self.updated_at or self.updated_at < end


#
# class AdminChild(models.Model):
#     parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="get_admin_child")
#     child = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="get_child_admin")


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="get_user_details")
    code = models.CharField(max_length=255, null=True, blank=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_update = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    religion = models.CharField(max_length=255, null=True, blank=True)
    departmentID = models.CharField(max_length=255, null=True, blank=True)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    sr_due_limit = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(null=True, blank=True)
    driving_licence = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    mother_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=6, null=True, blank=True)
    reference_by = models.CharField(max_length=255, null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)

class UserBank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_user_banks_details")
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    check_number = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
