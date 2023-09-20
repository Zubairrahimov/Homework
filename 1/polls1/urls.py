from django.urls import path
from.views import (
    CreateAPIView,
    ListAPiView,
    UpdateStatus,
)


urlpatterns = [
    path('create/', CreateAPIView.as_view()),
    path('list/', ListAPiView.as_view()),
    path('update/<int:news_id>/',UpdateStatus.as_view()),
]