import os
from django.conf import settings
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


def post_list3(request):
    return JsonResponse({
        'message': 'JsonResponse Type',
        'items': ['HttpResponse', 'JsonResponse', 'render'],
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = '.../travel_blog/sample.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'sample.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
