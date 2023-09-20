from django.urls import path
from.views import (
    CreateAPiView3,
    ListAPiView3,
    UpdateStatus3,
)


urlpatterns = [
    path('create/', CreateAPiView3.as_view()),
    path('list/', ListAPiView3.as_view()),
    path('update/<int:news_id>/',UpdateStatus3.as_view()),
]