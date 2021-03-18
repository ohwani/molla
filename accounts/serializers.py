from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User
import re


class UserRegistrationSerializer(serializers.ModelSerializer):
    
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
        password = attrs['password']
        password2 = attrs['password2']

        if not re.match(check_password, attrs['password']):
            raise serializers.ValidationError({'password': 'Please check your password.'})

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        attr.set_password
        
        return attrs

    # def validate_email(self, attrs):
    #     email = User.objects.filter(email=attrs)
    #     if email.exists():
    #         raise serializers.ValidationError('This email already exists')
    #     return attrs
    
    


    # def validate(self, attrs):
    #     email = User.objects.filter(email=attrs['email'])
    #     if email.exists():
    #         raise serializers.ValidationError('This email already exists')
    #     return attrs


