from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
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
    
    images = images_serializers.CountImageSerializer(many=True, read_only=True)
    # ReadOnlyField 는 ㅎ당 필드들을 수정하지않는다.
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = models.User
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

class SignUpSerializer(RegisterSerializer):

    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user