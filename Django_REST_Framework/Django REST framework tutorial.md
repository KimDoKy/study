# Django REST framework tutorial

## 1. serializer

### 시리얼라이저 사용하기

```
>>> from snippets.models import Snippet
>>> from snippets.serializers import SnippetSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

# snippet 인스턴스 생성
>>> snippet = Snippet(code='foo = "bar"\n')
>>> snippet.save()
>>> snippet = Snippet(code='print "hello, world"\n')
>>> snippet.save()

# snippet serializer
>>> serializer = SnippetSerializer(snippet)
>>> serializer.data
{'code': 'print "hello, world"\n', 'pk': 2, 'title': '', 'linenos': False, 'language': 'python', 'style': 'friendly'}

# json으로 변환
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"pk":2,"title":"","code":"print \\"hello, world\\"\\n","linenos":false,"language":"python","style":"friendly"}'

# python data type으로 파싱
>>> from django.utils.six import BytesIO
>>> stream = BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> stream
<_io.BytesIO object at 0x1064d8a40>
>>> data
{'code': 'print "hello, world"\n', 'pk': 2, 'title': '', 'linenos': False, 'language': 'python', 'style': 'friendly'}

# data를 인스턴스화, serializer 유효성 검사
>>> serializer = SnippetSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('title', ''), ('code', 'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
>>> serializer.save()
<Snippet: Snippet object>

# many=True 으로 쿼리셋도 serializer 함
>>> serializer = SnippetSerializer(Snippet.objects.all(), many=True)
>>> serializer.data
[OrderedDict([('pk', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('pk', 2), ('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('pk', 3), ('title', ''), ('code', 'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
>>> 

```

### ModelSerializer 사용하기

```
>>> from snippets.serializers import SnippetSerializer
>>> serializer = SnippetSerializer()
>>> print(repr(serializer))
SnippetSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(allow_blank=True, max_length=100, required=False)
    code = CharField(style={'base_template': 'textarea.html'})
    linenos = BooleanField(required=False)
    language = ChoiceField(choices=[('abap', 'ABAP'), ('abnf', 'ABNF'),...
    style = ChoiceField(choices=[('abap', 'abap'), ('algol', 'algol'), ...
```
> 필드를 자동으로 인식한다.  
> create() 메서드와 update() 메서드가 이미 구현되어 있다.


### Serializer 사용하는 django view 만들기

#### views setting

```
from django.http import HttpResponse  
from django.views.decorators.csrf import csrf_exempt  
from rest_framework.renderers import JSONRenderer  
from rest_framework.parsers import JSONParser  
from snippets.models import Snippet  
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):  
    """
    콘텐츠를 JSON으로 변환한 후 HttpResponse 형태로 반환합니다.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):  
    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):  
    """
    코드 조각 조회, 업데이트, 삭제
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
```

#### url settings

```
from django.conf.urls import url  
from snippets import views

urlpatterns = [  
    url(r'^snippets/$', views.snippet_list),
    # ex) http://127.0.0.1:8000/snippets/
    url(r'^snippets/(?P<pk>[0-9]+)/$', 
    # ex) http://127.0.0.1:8000/snippets/2/views.snippet_detail),
]
```

### 첫 웹 API 테스트 하기

```
 http http://127.0.0.1:8000/snippets/

HTTP/1.0 200 OK
Content-Length: 317
Content-Type: application/json
Date: Thu, 13 Apr 2017 16:42:11 GMT
Server: WSGIServer/0.2 CPython/3.5.2
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "print \"hello, world\"\n",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "print \"hello, world\"",
        "id": 3,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]


http http://127.0.0.1:8000/snippets/2/
HTTP/1.0 200 OK
Content-Length: 108
Content-Type: application/json
Date: Thu, 13 Apr 2017 16:43:05 GMT
Server: WSGIServer/0.2 CPython/3.5.2
X-Frame-Options: SAMEORIGIN

{
    "code": "print \"hello, world\"\n",
    "id": 2,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}
```

## 2. 요청과 응답

#### request 객체
request 객체의 핵심부는 request.data 속성입니다.
request.POST와 비슷하지만 웹 API에 좀더 적합합니다.

```
request.POST # 폼 데이터만 다루며, 'POST' 메서드에서만 사용 가능
request.data # 아무 데이터나 다룰수 있고, 'PUT', 'PATCH' 메서드에서도 사용 가능
```
#### response 객체
렌더링되지 않은 콘텐츠를 불러와 클라이언트에게 리턴한 콘텐츠 형태로 변환합니다.

#### 상태코드
REST 프레임워크에서는 각 상태 코드에 대해 좀더 명확한 식별자를 제공합니다.
ex) status 모듈의 HTTP_400_BAD_REQUEST 같은 식별자

#### API 뷰 감싸기
REST 프레임워크는 API 뷰를 작성하는데 사용할 수 있는 두가지 래퍼를 제공합니다.

1. @api_view : CBV에서 사용
2. APIView : FBV에서 사용

이 래퍼들은 뷰에서 받은 Request에 몇몇 기능을 더하거나, 콘텐츠가 잘 변환되도록 Response에 특정 context를 추가합니다.  

때에 따라 405 Method Not Allowed를 반환하거나, request.data가 깨진 경우 ParseError 예외를 던지는 등의 일도 수행합니다.

#### 이 모든 것을 한 군데 모으기

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

request.data는 json 요청 뿐만 아니라 yaml과 같은 다른 포맷도 다룰 수 있습니다.  
응답 객체에 데이터를 담아 리턴하는 것과 비슷하면서도, REST 프레임워크에서는 우리가 원하는 형태로 응답 객테를 렌더링해 줍니다.

### URL의 접미어를 통해 다른 포맷 제공하기

하나의 콘텐츠 형태에 묶여 있지 않다는 응답 객체의 장점을 활용하기 위해 API에서도 여러 형태의 포맷을 제공할 수 있습니다.


```
http://example.com/api/items/4.json
```
포맷의 접미어를 URL 형태로 전달받으려면 위와 같은 URL을 다룰수 있어야합니다.

#### format 키워드 추가

```python
# views.py

def snippet_list(request, format=None):  

def snippet_detail(request, pk, format=None):  
```

#### 기존 URL에 format_suffix_patterns 라는 패턴을 추가

```python
from django.conf.urls import patterns, url  
from rest_framework.urlpatterns import format_suffix_patterns  
from snippets import views

urlpatterns = [  
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

### 어떻게 되었을까?

앞에서 했던 동작과 비슷해보이지만, 이번엔 잘못된 요청에도 잘 대응합니다.

```
http http://127.0.0.1:8000/snippets/  
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 210
Content-Type: application/json
Date: Thu, 13 Apr 2017 17:28:56 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "print \"hello, world\"\n",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]

```
Accept 헤더를 사용하여 응답 받을 데이터의 포맷도 지정할 수 있습니다.

```
# Request JSON  
http http://127.0.0.1:8000/snippets/ Accept:application/json
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 210
Content-Type: application/json
Date: Thu, 13 Apr 2017 17:31:07 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "print \"hello, world\"\n",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]


# Request HTML  
http http://127.0.0.1:8000/snippets/ Accept:text/html
HTTP/1.0 200 OK
Allow: POST, OPTIONS, GET
Content-Length: 7014
Content-Type: text/html; charset=utf-8
Date: Thu, 13 Apr 2017 17:31:16 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

<!DOCTYPE html>
<html>
...
 
</html>

```

포맷 접미어를 붙여도 잘 동작합니다.

```
http http://127.0.0.1:8000/snippets.json  # JSON suffix  
http http://127.0.0.1:8000/snippets.api   # Browsable API suffix 
```

Content-Type 헤더를 사용해도 응답 받을 데이터의 포맷을 지정할 수 있습니다.

```
# 데이터를 넘기면서 POST 요청
http --form POST http://127.0.0.1:8000/snippets/ code="print 123"
HTTP/1.0 201 Created
Allow: POST, OPTIONS, GET
Content-Length: 93
Content-Type: application/json
Date: Thu, 13 Apr 2017 17:34:59 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": "print 123",
    "id": 5,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}

# JSON으로 POST 요청
http --json POST http://127.0.0.1:8000/snippets/ code="print 456"
HTTP/1.0 201 Created
Allow: POST, OPTIONS, GET
Content-Length: 93
Content-Type: application/json
Date: Thu, 13 Apr 2017 17:35:18 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "code": "print 456",
    "id": 6,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}
```

### 탐색 가능한 API
API는 클라이언트의 요청에 따라 데이터의 포맷을 결정하여 응답합니다. 따라서 웹브라우저의 요청에는 기본적으로 HTMl 형태로 응답합니다. 이 덕분에 API를 웹브라우저에서 탐색할 수 있습니다.



