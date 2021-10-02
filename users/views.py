from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import RegisterSerializer, UserInfoSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(operation_summary='Общая информация',
                                                            tags=['Пользователь']))
class UserInfoView(IsAuthenticated, RetrieveAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user


@method_decorator(name='post', decorator=swagger_auto_schema(operation_summary='Регистрация', tags=['Пользователь']))
class RegistrationView(CreateAPIView):
    serializer_class = RegisterSerializer
