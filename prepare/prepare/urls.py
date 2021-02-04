"""prepare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from page1 import urls as page1_urls
from main import urls as main_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# 맨날 리턴해서 queryset 이나 모델 인스턴스로 오던거를 json,xml로 바꿔주시는 엄청난 분이시다.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

#공통적인 view logic 을 다 구현해놓은 viewset 을 제공한다는데 아직은 모르겠음(CRUD 관련)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#url mapping 아래 urlpatterns 에 include 해주면 알아서 묶임
router = routers.DefaultRouter()
router.register(r'users', UserViewSet) # 왜 r 이 들어갈까 정규표현식이라 하긴 하던데


urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/',include(page1_urls), name='page_1'),
    path('', include(main_urls), name='main'),
    path('api-test/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
