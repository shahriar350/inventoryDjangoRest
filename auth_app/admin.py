from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from auth_app.forms import UserAdminChangeForm, UserAdminCreationForm, User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone_number', 'admin', 'staff',
                                    'sr',
                                    'counter',
                                    'showroom',
                                    'customer',
                                    'supplier',]
    list_filter = ['phone_number']
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('name',
                                      'image',)}),
        ('Permissions', {'fields': ('active','superuser',
                                    'admin',
                                    'staff',
                                    'sr',
                                    'counter',
                                    'showroom',
                                    'customer',
                                    'supplier',
                                    'groups', 'user_permissions',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password')}
         ),
    )
    search_fields = ['phone_number']
    ordering = ['phone_number']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
