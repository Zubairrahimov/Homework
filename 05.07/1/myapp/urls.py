from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('all/', views.all_data, name ='all_data'),
    path('detail/<int:product_id>', views.detail, name ='detail'),
]

