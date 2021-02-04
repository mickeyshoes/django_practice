from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# string to dict
from ast import literal_eval
#request url
import urllib.parse # url decode and manipulate
import urllib.request # http request

# Create your views here.

def main(request):
    return render(request,"main.html")

def response_info(request):
    print('worked')
    return HttpResponse(json.dumps("{'value': 'success'}"))

@csrf_exempt
def return_info(request):

    if request.method == 'POST':
        print(request.POST)
        name = json.loads(request.body.decode("utf-8"))
        print(name)
        print(name['value'])
        name = name['value']
        name = literal_eval(name)
        name['value'] = 'change in django'
        return HttpResponse(json.dumps(name))

    else:
        return HttpResponse("error")

def get_rest_api_info(request):

    # https 로 하게 되면 ssl 관련 인자 urlopen 안에 만들어서 넣어주어야 함
    url = 'http://localhost:8000/api-test/users'
    # 아직까지 다른 http method 로 하는 방법은 못찾음 default 는 get 인듯 함
    request_url = urllib.request.urlopen(url)
    byte_data = request_url.read()
    decode_data = byte_data.decode('utf-8')

    return HttpResponse(json.dumps(decode_data))
