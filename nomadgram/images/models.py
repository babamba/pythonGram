from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    # 생성 및 업데이트 시 공통적으로 사용되는 타임스탬프 정보 추상

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

    # 이미지 모델 ( 타임스탬프 클래스 상속 )

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def  __str__(self):
        return '{} - {}'.format(self.location, self.caption)


class Comment(TimeStampedModel):

    # 댓글 모델 ( 타임스탬프 클래스 상속 )

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True,)

    def  __str__(self):
        return self.message

class Like(TimeStampedModel):

    # 좋아요 ( relationship) 모델 ( 타임스탬프 클래스 상속 )

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def  __str__(self):
        return 'User : {} - Image Caption :{}'.format(self.creator.username, self.image.caption)