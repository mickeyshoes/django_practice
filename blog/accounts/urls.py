from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='account_index'),
    path('check/', views.check_data, name='check_datas'),
    path('class_based_views/', views.classViewTest.as_view()),
    path('test/', views.getDataFromReact.as_view()),
]