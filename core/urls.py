from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginView, LogoutView
from tasks.views import TaskListCreateView, TaskDetailView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title='Task API',
        default_version='v1',
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", RegisterView.as_view(), name='register'),
    path("api/login/", LoginView.as_view(), name='login'),
    path("api/logout/", LogoutView.as_view(), name='logout'),
    path("api/tasks/", TaskListCreateView.as_view(), name='task-list'),
    path("api/tasks/<int:pk>/", TaskDetailView.as_view(), name='task-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),

]
