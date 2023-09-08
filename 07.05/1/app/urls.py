from django.urls import path
from .views import InDetail, ListedVersion , UpadateQuestionView, DeleteQuestionView

urlpatterns = [

    path("all/" , ListedVersion.as_view()),
    path("det/<int:savol_id>", InDetail.as_view()),
    path('change/<int:savol_id>', UpadateQuestionView.as_view()),
    path('delete/<int:savol_id>', DeleteQuestionView.as_view())
]