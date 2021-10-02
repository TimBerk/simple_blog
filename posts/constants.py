from drf_yasg import openapi

STATUS_INACTIVE = 0
STATUS_ACTIVE = 1
STATUS_DRAFT = 2
STATUSES = (
    (STATUS_INACTIVE, 'Неактивный'),
    (STATUS_ACTIVE, 'Опубликованный'),
    (STATUS_DRAFT, 'Черновик'),
)

deep_param = openapi.Parameter(
    name='deep',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description='Deep',
    required=False,
    enum=[1, 2, 3]
)
