from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Позволяет всем пользователям просматривать контент,
    но редактировать его могут администраторы и модераторы,
    авторизованные пользователи могут редактировать только свои записи
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        is_authenticated = request.user.is_authenticated
        is_admin = is_authenticated and request.user.is_superuser
        is_moderator = is_authenticated and request.user.is_staff
        if request.method in SAFE_METHODS or is_admin or is_moderator:
            return True
        return obj.author == request.user


class ContentMixin:
    permission_classes = [IsAuthorOrReadOnly]
