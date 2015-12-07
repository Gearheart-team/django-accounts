from django import forms
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (ReadOnlyPasswordHashField,
                                       AdminPasswordChangeForm,
                                       UserCreationForm)
from social.apps.django_app.default import models
from .models import EmailUser


def admin_cleanup(admin_site=None):
    """
    Unregister dependency app models to unclutter the admin, and return
    a cleaned up admin site instance.
    """
    admin_site = admin_site or admin.site
    try:
        admin_site.unregister(models.Association)
    except NotRegistered:
        pass
    try:
        admin_site.unregister(models.Nonce)
    except NotRegistered:
        pass
    try:
        admin_site.unregister(models.UserSocialAuth)
    except NotRegistered:
        pass
    return admin_site


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=("Raw passwords are not stored, so there is no way to see "
                   "this user's password, but you can change the password "
                   "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = EmailUser
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = EmailUser
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            EmailUser.objects.get(email=email)
        except EmailUser.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])


class EmailUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = MyUserCreationForm
    change_password_form = AdminPasswordChangeForm
    actions_on_bottom = True
    ordering = ('email',)
    list_filter = ()
    readonly_fields = ('image_tag',)
    list_display = ('email', 'first_name', 'last_name', 'preferred_name',
                    'phone', 'gender', 'age', 'birthdate', 'is_superuser',
                    'is_developer')
    search_fields = ('email', 'last_name', 'preferred_name', 'first_name')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        ('User Info', {
            'fields': (
                'email', 'password',
                ('first_name', 'last_name', 'preferred_name'),
                ('image', 'image_tag'),
                'gender',
                'phone',
                'birthdate',
                ('validation_key', 'validated_at',),
            ),
        }),
        ('Roles', {
            'fields': (
                'is_developer',
                'is_superuser',
            ),
        }),
    )
admin.site.register(EmailUser, EmailUserAdmin)
