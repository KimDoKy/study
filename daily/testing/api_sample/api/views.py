from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint as r
import time

count = 0

@csrf_exempt
def test1(request):
    global count
    try:
        if request.method == 'POST':
            count += 1
            print(count)
            return HttpResponse(count)
        elif request.method == 'GET':
            return HttpResponse('get')
    except:
        return HttpResponse(status=408)

@csrf_exempt
def test2(request):
    global count
    try:
        time.sleep(r(0,5))
        if request.method == 'POST':
            count += 1
            print(count)
            return HttpResponse(count)
        elif request.method == 'GET':
            return HttpResponse('get')
    except:
        return HttpResponse(status=408)

post_count = 0

@csrf_exempt
def test3(request):
    global post_count
    if request.method == 'POST':
        post_count += 1
        print(post_count)
        return HttpResponse(post_count)
    elif request.method == 'GET':
        temp = [x for x in range(10)]
        print(temp)
        return HttpResponse(temp)
