from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.views import CommentViewSet, PostViewSet

app_name = 'posts'
router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = []
urlpatterns += path('', include(router.urls)),
