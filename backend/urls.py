from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="CRUD API for managing employees",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("employees.urls")),
    path("api/login/", TokenObtainPairView.as_view()),
    path("api/refresh/", TokenRefreshView.as_view()),
    path("api/auth/", include("accounts.urls")),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
