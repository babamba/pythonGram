from django.urls import path
from . import views

# 스프링에서 requestMapping 어노테이션과 비슷
# app_name 은 큰 카테고리 역할
# 그이후 urlPatterns 안의 path들을 통해 요청url에 맞는 걸 찾아 url에 할당 된 view를 실행한다.
# requestParam 처럼 요청에 담긴 인수들을 통해 처리도 가능

# from nomadgram.users.views import (
#     user_list_view,
#     user_redirect_view,
#     user_update_view,
#     user_detail_view,
# )

# app_name = "users"
# urlpatterns = [
#     path("", view=user_list_view, name="list"),
#     path("~redirect/", view=user_redirect_view, name="redirect"),
#     path("~update/", view=user_update_view, name="update"),
#     path("<str:username>/", view=user_detail_view, name="detail"),
# ]

#app_name = "images"

#urlpatterns = [
#    path("all/", view=views.ListAllImages.as_view(), name="all_images"),
#    path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
#   path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
#]

app_name = "images"

# like쪽에 int:image_id는 스프링 requestParam처럼 넘어오는 쿼리스트링 사용하도록 받는거 대신 views.py에서 파라미터로 지정안하면 에러 발생

# 2.0 이하 url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
# 2.0 부터 path('articles/<int:year>', views.year_archive),

urlpatterns = [
    path("feed/", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comment/", view=views.CommentOnImage.as_view(), name="comment_image")
]

# 장고 업데이트로 인한 url path의 정규식사용
# converter의 종류는

# str: /를 제외한 모든 문자열
# int
# slug: hypen, undersocre로 연결된 slug 형태의 str
# uuid
# path

# 출처: http://seulcode.tistory.com/210 [seulcoding]

# class FourDigitYearConverter: 
#     regex = '[0-9]{4}' 
#     def to_python(self, value): 
#         return int(value) 
        
#     def to_url(self, value): 
#         return '%04d' % value

# 위에 import 처리 from django.urls import register_converter, path
#from . import converters, views # 이런식으로 등록한다. 
# 록한 converter를 호출해서 사용하면 됨 
# register_converter(converters.FourDigitYearConverter, 'yyyy') 
# 
# urlpatterns = [ 
#   path('articles/2003/', views.special_case_2003), 
#   path('articles/<yyyy:year>/', views.year_archive), ... 
# ]

# 그외 전 버전으로 쓰려면 re_path로 처리

# /images/3/like/

# 0. url 과 view를 생성
# 1. url 에서 id를 가져옴
# 2. 해당 id의 이미지를 찾는다.
# 3. 이미지에 좋아요를 생성한다.
