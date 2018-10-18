from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from nomadgram.notifications import views as notification_views


# Create your views here.
# urls.py를 통해 요청 된 urlpatterns 에 할당 되어 있는 url이 요청되면 각 url에 할당된 view가 실행 
# 스프링에서는 Controller의 requestMapping 각각의 내부 실행 메서드라고 보면 쉬울 듯

class Feed(APIView):
    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image : image.created_at, reverse=True)
        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


def get_key(image):
    return image.created_at


class LikeImage(APIView):

    def post(self, request, image_id ,format=None):
        # 해당 views 호출한 요청자 아이디 변수 할당
        user = request.user

        # 요청에 같이 넘어온 request의 image_id값으로 이미지 모델의 해당 아이디에 해당하는 이미지있는지 try 있으면 try / catch 빠져나감
        try:
            found_image = models.Image.objects.get(id=image_id)

        # except처리되는 순간 밑에 있는 구문 실행 안함
        except models.Image.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        # 위에서 try가 실행되었을때 해당 object가 검색되었으면 delete 처리 
        try:
            preexisting_like = models.Like.objects.get(
                creator = user,
                image= found_image
            )
            print("exist_like & delete - name : " , user , " / image : " , found_image )

            # 이전에 좋아요한 오브젝트 발견하면 수정하지않음
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        # 위에서 try가 실행되고 try가 실패했을때 save 처리 
        except models.Like.DoesNotExist:
            print(found_image)

            new_like = models.Like.objects.create(
                creator = user,
                image = found_image
            )

            print("new_like & save - name : " , user , " / image : " , found_image )
            # 이전에 좋아요 하지않음 오브젝트 발견하면 수정
            new_like.save()

            notification_views.create_notification(user, found_image.creator, 'like', found_image)

        return Response(status=status.HTTP_201_CREATED)

class UnLikeImage(APIView):
     def delete(self, request, image_id, format=None):
         user = request.user
         try:
            preexisiting_like = models.Like.objects.get(
                creator=user,
                image__id=image_id
            )
            preexisiting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
         except models.Like.DoesNotExist:
             return Response(status=status.HTTP_304_NOT_MODIFIED)

class CommentOnImage(APIView):

    def post(self,request, image_id, format=None):
        # 해당 views 호출한 요청자 아이디 변수 할당
        user = request.user


        # 요청에 같이 넘어온 request의 image_id값으로 이미지 모델의 해당 아이디에 해당하는 이미지있는지 try 있으면 try / catch 빠져나감
        try :
            found_image = models.Image.objects.get(id=image_id)
        # try가 실패시 404 처리 
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # request data 를 json 형식에서  ~ python 형태로 시리얼라이즈 
        serializer = serializers.CommentSerializer(data=request.data)

        # 시리얼라이즈가 처리되었을때 db에 creator 컬럼에 요청 user아이디값 넣어주고 insert 처리
        if serializer.is_valid():
            serializer.save(creator=user, image=found_image)

            notification_views.create_notification(user, found_image.creator, 'comment', found_image, serializer.data['message'])

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        # 실패시 400 처리 
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Comment(APIView):
    def delete(self, request, comment_id, format=None):
        
        user = request.user

        # 유저가 쓴 댓글 만 삭제 
        try :
            comment = models.Comment.objects.get(id=comment_id, creator = user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search(APIView):
    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None :

            hashtags = hashtags.split(",")

            print(hashtags)

            # tags__name__in = deep relation ship 
            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()
            print(images)

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data , status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

        # 포함된 글자를 검색할때는 creator__username__contain= 
        # 정확하게 검색할때는 creator__username__exact
        # icontain / iexact 는 대소문자 구분없이 
        # models.Image.objects.filter(creator__username='jw')