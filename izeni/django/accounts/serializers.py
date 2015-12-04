from rest_framework import serializers
from .models import EmailUser


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = EmailUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = EmailUser
        read_only_fields = ('date_joined', 'last_login',
                            'is_developer', )
        exclude = ('is_superuser', 'groups', 'user_permissions',
                   'validation_key', 'validated_at', )
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    # TODO image url instead of file
    class Meta:
        model = EmailUser
        read_only_fields = ('email', 'date_joined', 'last_login',
                            'is_developer', )
        exclude = ('password', 'is_superuser', 'groups', 'user_permissions',
                   'validation_key', 'validated_at')
