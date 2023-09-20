from django.urls import path
from.views import (
    CreateAPiView5,
    ListAPiView5,
    UpdateStatus5,
)


urlpatterns = [
    path('create5/', CreateAPiView5.as_view()),
    path('list5/', ListAPiView5.as_view()),
    path('update5/<int:news_id>/',UpdateStatus5.as_view()),
]