from django.urls import path

from . import views

urlpatterns = [
    path('api/user/', views.UserAPIView.as_view(), name='user'),
]