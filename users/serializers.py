from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        help_text="Required. 4-30 characters. Letters, numbers, and @/./+/-/_ only.",
        error_messages={
            'min_length': "Username must be at least 4 characters.",
            'max_length': "Username cannot be longer than 30 characters."
        },
        style={
            'placeholder': 'e.g. john_doe123',
            'example': 'john_doe123'
        }
    )
    password = serializers.CharField(
        write_only=True,
        style={
            'input_type': 'password',
            'placeholder': 'Enter 8+ character password'
        }
    )
    email = serializers.EmailField(
        required=False,
        style={
            'placeholder': 'your.email@domain.com'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'username': {
                'style': {'placeholder': 'john_doe123'}
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        style={'placeholder': 'Your username'}
    )
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        return user