from django.contrib.auth import get_user_model
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1',
    ),
    patterns=[path('api/v1/', include('api.urls')), ],
    public=True,
    generator_class=OpenAPISchemaGenerator,
    authentication_classes=(SessionAuthentication,),
    permission_classes=(permissions.AllowAny,),
)
USER_MODEL = get_user_model()
urlpatterns = [
    path('swagger/', schema_view.with_ui(cache_timeout=0), name='swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('product/', include('product.urls')),
    path('token/login/', TokenObtainPairView.as_view(), name='api.token_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api.token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='api.token_verify'),
]
