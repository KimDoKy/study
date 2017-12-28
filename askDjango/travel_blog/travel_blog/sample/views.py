import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def post_list1(request):
    type = 'http response type'
    return HttpResponse('''
        <h1>View Test Page</h1>
        <p>{type}</p>
        <p>{type} 테스트 페이지입니다.</p>'''.format(type=type)) 


def post_list2(request):
    type = 'render type'
    return render(request, 'sample/post_list.html', {'type':type})

