from django.urls import path

from . import views

#/api/products
urlpatterns = [
    path('user/create', views.UserCreateAPIView.as_view()),
    path('user/<int:pk>/', views.UserDetailAPIView.as_view())
]
