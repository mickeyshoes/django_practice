from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path("",views.main, name='main'),
    path('response_info/', views.response_info, name='response_info'),
    path('return_info/', views.return_info, name='return_info'),
    path('req_data/', views.get_rest_api_info, name='request_data'),
]