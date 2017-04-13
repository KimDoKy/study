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
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
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


