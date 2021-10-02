from django.contrib.auth import get_user_model
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from posts.constants import STATUS_DRAFT, STATUSES

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    name = models.CharField('Наименование', max_length=255)
    content = models.TextField('Контент')
    published_at = models.DateTimeField('Дата публикации', db_index=True)
    status = models.SmallIntegerField('Статус', default=STATUS_DRAFT, choices=STATUSES)

    class Meta:
        ordering = ['id']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.name


class Comment(MPTTModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    text = models.TextField('Контент')
    parent = TreeForeignKey(
        'self', verbose_name='Родитель',
        on_delete=models.DO_NOTHING, blank=True, null=True, related_name='children'
    )
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:20]
