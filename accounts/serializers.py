from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def validate_email(self, attrs):
    #     email = User.objects.filter(email=attrs)
    #     if email.exists():
    #         raise serializers.ValidationError('This email already exists')
    #     return attrs

    def validate(self, attrs):
        email = User.objects.filter(email=attrs['email'])
        if email.exists():
            raise serializers.ValidationError('This email already exists')
        return attrs
