from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.decorators import common_schema_decorator
from posts.constants import STATUS_ACTIVE, deep_param
from posts.models import Comment, Post
from posts.permissions import ContentMixin, IsAuthorOrReadOnly
from posts.serializers import (CommentListSerializer, CommentSerializer,
                               PostSerializer, serializable_object)


@common_schema_decorator(tags=['Публикации'])
class PostViewSet(ContentMixin, viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['name', 'content']
    filterset_fields = ['published_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return super().get_queryset().filter(status=STATUS_ACTIVE)
        if user.is_staff or user.is_superuser:
            return super().get_queryset()
        return super().get_queryset().exclude(~Q(author=user) & ~Q(status=STATUS_ACTIVE))


@common_schema_decorator(tags=['Комментарии'])
class CommentViewSet(ContentMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('author').prefetch_related('children').all()
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        return CommentSerializer

    def get_queryset(self):
        if self.kwargs.get('post_id'):
            post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
            return post.comments.filter(parent__isnull=True).all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post_id=post_id)

    @swagger_auto_schema(tags=['Комментарии'], operation_description='Дерево', manual_parameters=[deep_param])
    @action(
        detail=True,
        methods=['GET'],
        permission_classes=[IsAuthorOrReadOnly],
    )
    def comment_tree(self, request, post_id, pk):
        main_comment = get_object_or_404(Comment, post_id=post_id, id=pk)
        deep = int(request.query_params.get('deep'))
        deep = min(deep, 3)
        result = serializable_object(main_comment, deep)
        return Response(result)
