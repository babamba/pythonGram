from django.urls import path
from . import views

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

# like쪽에 int:image_id는 스프링 requestParam처럼 넘어오는 쿼리스트링 사용하도록 받는거 

urlpatterns = [
    path("feed/", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image")
]

# /images/3/like/

# 0. url 과 view를 생성
# 1. url 에서 id를 가져옴
# 2. 해당 id의 이미지를 찾는다.
# 3. 이미지에 좋아요를 생성한다.
