from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework import views, status, response
from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Success!")

def check_data(request):
    data = {
        "ID" : "hello",
        'email' : 'qwerty@naver.com',
        'password' : "hello"
    }
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return HttpResponse(serializer.data)

    else:
        return HttpResponse('False')

# class based view 는 APIView 로 Function based view 는 데코레이터 추가 @api_view(['http_method_list'])
class classViewTest(views.APIView):
    from rest_framework import permissions
    # 해당 view 에 퍼미션 관련
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getDataFromReact(views.APIView):
    from rest_framework import permissions
    permissions_class = [permissions.AllowAny]

    def get(self, request):
        return HttpResponse(request.data)