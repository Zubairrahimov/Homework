from django.urls import path
from.views import (
    CreateNewsAPIView,
    ListNewsAPIView,
    UpdateStatusNewsAPIView,
)


urlpatterns = [
    path('create/', CreateNewsAPIView.as_view()),
    path('list/', ListNewsAPIView.as_view()),
    path('update/<int:pk>/',UpdateStatusNewsAPIView.as_view()),
]