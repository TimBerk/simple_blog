from rest_framework import serializers

from posts.models import Comment, Post


def serializable_object(node, level=1):
    root_obj = {'id': node.pk, 'name': node.author.username, 'text': node.text, 'children': []}
    obj_cache = {node.pk: root_obj}
    for descendant in node.get_descendants().filter(level__lte=level).select_related('author'):
        parent_obj = obj_cache[descendant.parent.pk]
        descendant_obj = {
            'id': descendant.pk,
            'name': descendant.author.username,
            'text': descendant.text,
            'children': []}
        parent_obj['children'].append(descendant_obj)
        obj_cache[descendant.pk] = descendant_obj
    return root_obj


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'parent', 'children')
        read_only_fields = ('author',)

    def get_children(self, obj):
        return serializable_object(obj)


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'parent')
        read_only_fields = ('author',)


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author', read_only=True)
    status_name = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
