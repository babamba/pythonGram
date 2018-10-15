from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializers):

    class Meta:
        model = models.Image
        fields = '__all__'


class CommentSerializer(serializers.Serializers):
    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializers):
    class Meta:
        model = models.Like
        fields = '__all__'

