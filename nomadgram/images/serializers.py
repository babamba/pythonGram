from rest_framework import serializers
from . import models
from nomadgram.users import models as user_model
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

# 시러얼라이즈는 Json to Python 또는 Python to Json 형태를 유지시켜주기 위해 사용
# rest_framework에 내장된 기능
# 클래스를 지정해주고 각각에 해당하는 시리얼라이즈에 request.data를 인수로 실행하여 가공처리 

class SmallImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
                    'id',
                    'message',
                    'creator'
                )
    

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class InputImagaeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )

class ImageSerializer(serializers.ModelSerializer, TaggitSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = models.Image
        fields = (
                    'id',
                    'file',
                    'location',
                    'caption',
                    'comments',
                    'like_count',
                    'creator',
                    'created_at',
                    'tags',
                )

class CountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'like_count',
            'comment_count'
        )