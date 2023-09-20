from django.urls import path
from.views import (
    CreateAPiView2,
    ListAPiView2,
    UpdateStatus2,
)


urlpatterns = [
    path('create2/', CreateAPiView2.as_view()),
    path('list2/', ListAPiView2.as_view()),
    path('update2/<int:news_id>/',UpdateStatus2.as_view()),
]