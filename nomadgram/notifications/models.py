from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models
from taggit.managers import TaggableManager

# Create your models here.
# 디비 컬럼이라고 생각하면 됨. 스프링에서는 VO
# 요청 시 다른 User : {} - Image Caption :{} 식으로 표시 값 바꿔줄수 있음
# 컬럼을 추가할때 makemigrations 및 migrate 실행 해줘야 추가된 컬럼이 활성

class Notification(image_models.TimeStampedModel):

    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow')
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='creator')
    to = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='to')
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, on_delete=models.PROTECT, null=True, blank=True)