from django import forms
from django.contrib.auth import get_user_model, authenticate

from django.contrib.auth.forms import ReadOnlyPasswordHashField

# User = get_user_model()
from auth_app.models import User


class RegisterForm(forms.ModelForm):
    """
    The default

    """

    password = forms.CharField(widget=forms.PasswordInput)

    # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number']

    def clean_phone_number(self):
        '''
        Verify email is available.
        '''
        phone_number = self.cleaned_data.get('phone_number')
        qs = User.objects.filter(phone_number=phone_number)
        if qs.exists():
            raise forms.ValidationError("phone_number is taken")
        return phone_number

    # def clean(self):
    #     '''
    #     Verify both passwords match.
    #     '''
    #     # cleaned_data = super().clean()
    #     # password = cleaned_data.get("password")
    #     # password_2 = cleaned_data.get("password_2")
    #     # if password is not None and password != password_2:
    #     #     self.add_error("password_2", "Your passwords must match")
    #     return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active = True
        if commit:
            user.save()

        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'active', 'admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
