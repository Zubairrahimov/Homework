from django.urls import path
from .views import (
    UserGetView, 
    UserDeleteUpdateGetView,
    UserCreateView,
    UserDeleteView,
    UserGetByIdView,
    UserUpdateView,
    UserGetAllView,
)

urlpatterns = [
    path('all/', UserGetView.as_view()),
    path('id/<int:pk>', UserDeleteUpdateGetView.as_view()),
    path('all/', UserGetAllView.as_view()),
    path('getid/<int:pk>', UserGetByIdView.as_view()),
    path('delete/<int:pk>', UserDeleteView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('create/', UserCreateView.as_view()),
]

