from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

User = get_user_model()


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_staff')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Пароль', required=True, write_only=True)
    password_repeat = serializers.CharField(label='Пароль', required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_repeat', 'first_name', 'last_name']

    def validate_password_repeat(self, value):
        password = self.initial_data.get('password')
        if password != value:
            raise serializers.ValidationError('Пароли не совпадают')

        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data.pop('new_password_repeat', None)

        try:
            with transaction.atomic():
                user_object: User = User()
                for k, v in validated_data.items():
                    if hasattr(user_object, k):
                        setattr(user_object, k, v)
                user_object.set_password(password)
                user_object.save()
        except Exception as e:
            raise serializers.ValidationError({'detail': str(e)})

        return user_object
