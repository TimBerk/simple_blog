from django.urls import path

from users.views import RegistrationView, UserInfoView

app_name = 'users'

urlpatterns = [
    path('me/', UserInfoView.as_view(), name='users_info'),
    path('sign-up/', RegistrationView.as_view(), name='users_sign_up')
]
