# serializer 는 django query set 같은 결과물들을 python data type 으로 변환해준다.
# => 이는 쉽게 json, xml로 변환이 가능한 상태로 바꾸어 줌을 의미한다.
# viewset 은 요청을 처리하여 응답을 해준다.
from rest_framework import serializers, viewsets
from .models import User

#django 의 forms 와 비슷하게 선언해주어야 한다 (비슷하게 동작함).
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['ID', 'email']

    def return_to_json(self):
        from rest_framework.renderers import JSONRenderer

        json = JSONRenderer().render(self.data)
        return json

