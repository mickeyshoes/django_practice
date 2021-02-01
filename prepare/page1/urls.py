from django.urls import path
from . import views

app_name = 'page_1'

urlpatterns = [
    path('main',views.main, name="page_1_main"),

]