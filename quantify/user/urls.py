from django.urls import path
from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view(), name="user-list"),
    path("<int:pk>/update/", views.UserUpdateAPIView.as_view(), name="user-update"),
    path("<int:pk>/delete/", views.UserDeleteAPIView.as_view(), name="user-delete"),
    path("<int:pk>/", views.UserDetailAPIView.as_view(), name="user-detail"),
    path("<int:pk>/change-password/", views.UserChangePasswordAPIView.as_view(), name="user-change-password"),
]

