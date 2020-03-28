from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'email',
            'mobile_num',
            'DOB',
        ]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg = "User is not activated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to login given Username and password'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Must Provide username and password'
            raise exceptions.ValidationError(msg)
        return data