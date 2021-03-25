# from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
import re


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only': True}
        }

        validators = [
            UniqueTogetherValidator(
                queryset = User.objects.all(),
                fields = ['email'],
                message = 'This email already exists'
            )
        ]
    def validate(self, attrs):
        check_password = re.compile('^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
        email = attrs.get('email', None) 
        password = attrs.get('password', None)
        password2 = attrs.get('password2', None)

        if not re.match(check_password, attrs['password']):
            raise serializers.ValidationError({'password': 'Please check your password.'})

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        return attrs


# class LoginSerializer(serializers.Serializer):

#     class Meta:
#         model = User
#         fields = ['emali', 'passowrd']
    
#     def validate(self, attrs):
#         email = attrs.get('email', None) 
#         password = attrs.get('password', None)
#         user = authenticate(email=email, password=password)

#         if user is None:
#             raise serializers.ValidationError("Invalid login credentials")
#         try:
#             refresh = RefreshToken.for_user(user)
#             refresh_token = str(refresh)
#             access_token = str(refresh.access_token)

#             update_last_login(None, user)

#             validation = {
#                 'access': access_token,
#                 'refresh': refresh_token,
#                 'email': user.email,
#                 'role': user.role,
#             }

#             return validation
        
#         except AuthUser.DoesNotExist:
#             raise serializers.ValidationError("Invalid login credentials")

    
    # def validate_email(self, attrs):
    #     email = User.objects.filter(email=attrs)
    #     if email.exists():
    #         raise serializers.ValidationError('This email already exists')
    #     return attrs


