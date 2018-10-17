from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# class 기반 뷰 - http request 를 위한 모든 method 를 class 안에 넣음
class UserProfile(APIView):
    def get(self, request, username, format=None):
        try:
            found_user = models.User.objects.get(username=username)
            serializer = serializers.UserProfileSerializer(found_user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

            print(found_user)
        except models.User.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)

class ExploreUsers(APIView):
    def get(self, request, format=None):


        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ListUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
class UnFollowUser(APIView):
    def delete(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_unfollow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # ManyToMany(다대다) 관계에서 객체를 제거
        user.following.remove(user_to_unfollow)

        user.save()

        return Response(status=status.HTTP_200_OK)

class FollowUser(APIView):
    def post(self, request,  user_id, format=None):
        
        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # ManyToMany(다대다) 관계에서 객체를 추가 
        user.following.add(user_to_follow)

        # 대상의 follower에 해당 유저 추가 
        user_to_follow.followers.add(user)

        return Response(status=status.HTTP_200_OK)

# 팔로워 리스트 
class UserFollowers(APIView):
    def get(self, request, username, format=None):
        try :
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK )

# 팔로잉 리스트 
class UserFollowing(APIView):
    def get(self, request, username, format=None):
        try :
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_following = found_user.following.all()
        serializer = serializers.ListUserSerializer(user_following, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK )



class Search(APIView):
    def get(self, request, format=None):

        username = request.query_params.get('username', None)

        if username is not None :

            users = models.User.objects.filter(username__istartswith=username)

            serializer = serializers.ListUserSerializer(users, many=True)

            return Response(data=serializer.data , status=status.HTTP_200_OK)
        
        else : 
            return Response(status=status.HTTP_400_BAD_REQUEST)


        # --------------------------------------------------------------------------------

        # QuerySet
        # Post.objects.all() : “SELECT * FROM post…” 와 같은 SQL문 생성
        # Post.objects.create() : “INSERT INTO post VALUES(…)” 와 같은 SQL문 생성

        # --------------------------------------------------------------------------------

        # --------------------------------------------------------------------------------

        # 제외조건 (exclude)
        # 제목에 '테스트'를 포함한 record를 제외한 전체
        # Post.objects.all().exclude(title__icontains='test')
        # 제목에 1을 포함하지만 3으로 끝나지 않는 record
        # Post.objects.filter(title__icontains='1').exclude(title__endswith='3')

        # OR 조건 (filter)

        # from django.db.models import Q (or 조건을 위해 Q객체 임포트 )
        # 모델클래스명.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건
        # 모델클래스명.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건

        # AND 조건 (filter) 혹은 SQL WHERE절
        # queryset = 모델클래스명.objects.all()
        # queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2)
        # queryset = queryset.filter(조건필드3=조건값3)

        # 필터링 (qs1 = qs2)
        # qs1 = Post.objects.filter(title__icontains='1', title__endswith='3') # i = ignore_case (대소문자 구별 X)
        # qs2 = Post.objects.filter(title__icontains='1').filter(title__endswith='3') # 체이닝

        # --------------------------------------------------------------------------------

        # 특정필드 기준 정렬조건 (Meta.ordering)
        
        # class Post(models.Model):
            #....
            # class Meta:
            #    ordering = ['-id'] # id 필드 기준 내림차순 정렬, 미지정시 임의 정렬

        # --------------------------------------------------------------------------------

        # 범위 조건 (슬라이싱)
        # queryset = queryset[:10] # 현재 queryset에서 처음10개만 가져오는 조건을 추가한 queryset

        # 리스트 슬라이싱과 거의 유사하나, 역순 슬라이싱은 지원하지 않음
        # queryset = queryset[-10:] # AssertionError 예외 발생

        # 이때는 먼저 특정 필드 기준으로 내림차순 정렬을 먼저 수행한 뒤, 슬라이싱
        # queryset = queryset.order_by('-id')[:10]
        # 예를 들어 처음 5 개의 객체 ( )를 반환합니다 .LIMIT 5
        # Entry.objects.all()[:5]
        # 6 번째에서 10 번째까지의 객체 ( ) 를 반환합니다 .OFFSET 5 LIMIT 5
        # Entry.objects.all()[5:10]

        # --------------------------------------------------------------------------------

        #.save(), .create() 실행시 DB에 INSERT SQL이 전달된다.
        # queryset.update(title='test title') # 일괄 update 요청
        # queryset = Post.objects.all()
        # queryset.delete() # 일괄 delete 요청

        # --------------------------------------------------------------------------------

