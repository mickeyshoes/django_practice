from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# string to dict
from ast import literal_eval

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
