from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from posts.models import Comment, Post


@admin.register(Comment)
class CommentMPTTModelAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'post', 'parent')
    search_fields = ('content',)
    mptt_level_indent = 20


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    inlines = [CommentInline]
    list_display = ('id', 'name', 'published_at', 'status')
    list_search = ('name',)
