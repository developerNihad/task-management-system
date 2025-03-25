from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginView, LogoutView
from tasks.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", RegisterView.as_view(), name='register'),
    path("api/login/", LoginView.as_view(), name='login'),
    path("api/logout/", LogoutView.as_view(), name='logout'),
    path("api/tasks/", TaskListCreateView.as_view(), name='task-list'),
    path("api/tasks/<int:pk>/", TaskDetailView.as_view(), name='task-detail'),
]
