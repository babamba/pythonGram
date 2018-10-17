from rest_framework import serializers
from . import models
from nomadgram.users import models as user_model
from nomadgram.images import serializers as images_serializers

# 시러얼라이즈는 Json to Python 또는 Python to Json 형태를 유지시켜주기 위해 사용
# rest_framework에 내장된 기능
# 클래스를 지정해주고 각각에 해당하는 시리얼라이즈에 request.data를 인수로 실행하여 가공처리 

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )

class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImageSerializer(many=True)

    class Meta:
        model = user_model.User
        fields = (
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images'
        )
