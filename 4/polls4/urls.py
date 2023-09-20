from django.urls import path
from.views import (
    CreateAPiView4,
    ListAPiView4,
    UpdateStatus4,
)


urlpatterns = [
    path('create4/', CreateAPiView4.as_view()),
    path('list4/', ListAPiView4.as_view()),
    path('update4/<int:news_id>/',UpdateStatus4.as_view()),
]