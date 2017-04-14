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

## 3. 클래스 기반 뷰
클래스 기반 뷰는 일반적인 기능을 재사용하게 해주며 코드 중복(DRY)를 막아줍니다.

### 클래스 기반 뷰로 API 재작성하기

```python
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# CBV(APIView)으로 리팩토링
class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

```
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# CBV사용으로 .as_view() 사용
urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),

    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

### 믹스인 사용하기
클래스 기반 뷰를 사용하여 얻는 가장 큰 이점은 기능들을 손쉽게 조합할 수 있다는 점입니다.  

```
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *arg, **kwargs):
        return self.list(request, *arg, **kwargs)
    
    def post(self, request,*args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

기본 뷰(GenericAPIView)는 핵심 기능을 제공하며, 믹스인 클래스들은 .list(), .create() 기능 등을 제공합니다. 위 코드에서는 get, post 메서드에 적절히 연결하였습니다.

### 제네릭 클래스 기반 뷰 사용하기
믹스인 클래스를 사용하여 뷰의 코드를 꽤 많이 줄였지만 더 줄일 수 있습니다.
REST 프레임워크에서는 믹스인과 연결된 **제네릭 뷰**를 제공합니다.

```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```
 큰 노력 없이 아주 많은 기능을 구현했는데도 코드는 더 깔끔하고 더 Django다워졌습니다.
 
## 4. 인증과 권한
앞에서 만든 API에서는 누구나 편집, 삭제 할수 있습니다.

#### 지금 필요한 기능들

- 코드 조각은 만든 사람과 연관이 있다.
- 인증받은 사용자만 코드 조각을 만들 수 있다.
- 해당 코드 조각을 만든 사람만, 이를 편집, 삭제할 수 있다.
- 인증받지 않은 사용자는 '읽기 전용'으로만 사용 가능하다.

### 모델에 속성 추가하기

```python
# models.py Snippet 모델에 추가

owner = models.ForeignKey('auth.User', related_name='snippets')  
highlighted = models.TextField()  
```
모델이 저장될 때 하이라이트 된 코드를 highlighed 핖ㄹ드에 저쟝하야 합니다. 코드 하이라이팅에는 pygments 라이브러리를 사용합니다.

.save() 메소드를 작성합니다.

```python
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
```

### 사용자 모델에 엔드포인트 추가하기

사용자를 추가했으니 사용자를 보여주는 API도 추가합니다.

```python
rom django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):  
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
```
snippets는 사용자 모델과 반대방향으로 이어져 있기 때문에 ModelSerializer에 기본적으로 추가되지 않습니다. 따라서 명시적으로 필드를 지정해주어야합니다.

사용자와 관련된 뷰도 추가해야합니다. 읽기 전용 뷰만 있으면 되기 떄문에 제네릭 클래스 기분 뷰중에 ListAPIView와 RetriveAPIView를 사용합니다.

### 사용자가 만든 코드 조각 연결하기
지금까지 만든 코드조각은 사용자와 아무 관계도 맺지 않았습니다. 사용자는 직렬화된 표현에 나타나지 않았고ㅡ 요청하는 측에서 지정하는 속성이었을 뿐입니다.

이를 해결하기 위해 코드 조각 뷰에서 .perform_create() 메서드를 오버라이딩해야합니다.
이 메서드는 인스턴스를 저장하는 과정을 조정하며, 따라서 요청이나 요청 URL에서 정보를 원하는대로 다룰 수 있습니다.

SnippetList 뷰 클래스에 내용 추가합니다.

```
def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```
우리가 만든 시리얼라이저의 create()메서드는 검증한 요청 데이터에 더하여 'owner' 필드도 전달합니다.

### 시리얼라이저 업데이트하기
이제 코드 조각이, 해당 코드 조각을 작성한 사용자와 연결되었습니다.
SnippetSerializer에도 이를 반영합니다. serializers.py의 SnippetSerializer에 추가합니다.

```
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
```
source 인자로는 특정 필드를 지정할 수 있습니다. 여기에는 직렬화된 인스턴스의 속성뿐만 아니라 위의 코드에서처럼 마침표 표기 방식을 통해 특정 속성을 탐색할 수도 있습니다.

이 필드는 CharField나 BooleanField와는 달리 타입이 없는 ReadOnlyField 클래스로 지정했습니다. 타입이 없는 ReadOnlyField는 직렬화에 사용되었을땐 언제나 읽기전용이므로, 모델의 인스턴스를 업데이트할 때는 사용할 수 없습니다. CharField(read_only=True)도 이와 같은 기능을 수행합니다.

### 뷰에 요청 권한 추가
이렇게 해서 코드 조각이 사용자와 연결되었습니다. 이제 인증 받은 사용자만 코드 조각을 생성/업데이트/삭제를 할 수 있습니다.

REST 프레임워크는 특정 뷰에 제한을 걸 수 있는 권한 클래스를 제공하고 있습니다. 그중 한가지인 IsAuthenticatedOrReadOnly는 인증 받은 요청에 읽기와 쓰기 권한을 부여하고, 인증 받지 않은 요청에 대해서는 읽기 권한만 부여합니다.

뷰 파일에 내용을 추가합니다.

```
# SnippetList, SnippetDetail에 필드 추가
permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
```

### 탐색 가능한 API에 로그인 추가하기
지금 시점에 브라우저에 API에 접속하면 더이상 새 코드 조각을 만들수 없음을 알 수 있습니다. 이를 해결하려면 사용자 로그인 기능이 필요합니다.

urls.py를 수정하면 탐색 가능한 API 에 사용한 로그인 뷰를 추가할 수 있습니다.

```
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```
여기에는 한가지 제약이 따르는데, namespace에 'rest_framework'를 지정해야합니다.
다시 브라우저로 돌아가 API에 접근해보면 오른쪽 상단에 'Login' 링크를 확인할 수 있습니다.

### 객체 수준에서 권한 설정하기
코드 조각은 아무나 볼 수 있어야 하지만, 업데이트와 삭제는 해당 코드를 만든 사용자만 할 수 있어야합니다.

이를 위한 커스텀 권한을 만들어봅니다.

snippet앱 안에 permissions.py을 만들고 내용을 입력합니다.

```python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):  
    """
    객체의 소유자에게만 쓰기를 허용하는 커스텀 권한
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모두에게 허용하므로,
        # GET, HEAD, OPTIONS 요청은 항상 허용함
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 코드 조각의 소유자에게만 부여함
        return obj.owner == request.user
```
SnippetDetail 클래스에 permission_classes 속성을 추가합니다.

```
permission_classes = (permissions.IsAuthenticatedOrReadOnly,  
                      IsOwnerOrReadOnly,)
```
 
### API에 인증 붙이기
API에 권한을 설정했으므로, 이지는 코드 조각을 수정할 수 있는 인증 절차가 필요합니다. 니금까지는 인증 클래스를 만들지 않고 기본으로 제공되는 SessionAuthentication과 BasicAuthentication을 사용했습니다.  

웹 브라우저 API를 사용하는 경우, 로그인을 하면 브라우저의 세션에 인증 정보가 저장됩니다.

프로그램 상에서 API를 사용하는 경우, 인증에 필요한 내용을 명시적으로 전달해야만 합니다.

인증 없이 코드 조각을 생성하려는 경우, 다음과 같이 에러를 보여줍니다.

```
http POST http://127.0.0.1:8000/snippets/ code="print 123"

{
    "detail": "Authentication credentials were not provided."
}
```

사용자의 계정과 비밀번호를 포함하여 요청한다면, 이 요청은 성공합니다.

```
http -a tom:password POST http://127.0.0.1:8000/snippets/ code="print 789"

{
    "id": 5,
    "owner": "tom",
    "title": "foo",
    "code": "print 789",
    "linenos": false,
    "language": "python",
    "style": "friendly"
}
```

## 5. 관계 & 하이퍼링크

지금까지 우리가 만든 API에서 '관계'는 primary Key로 나타내고 있었습니다.
이번 튜토리얼에서는 API의 발견성과 응집력을 향상시키고자 관계를 하이퍼링크로 나타내보겠습니다.

#### API의 최상단에 대한 엔드 포인트 만들기
'코드조각'과 '사용자'에 대한 엔드 포인트를 만들었지만, 아직까지 이렇다할 API의 시작점은 없었습니다.
이를 만들기 위해 평범한 함수 기반 뷰와  @api_view 데코레이터를 사용하겠습니다.

```
# views.py

@api_view(('GET,'))
def api_root(request, format=None):
    return Response({
        'user': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
```
URL을 만드는데 reverse함수를 사용한 점을 주목하세요.

#### 코드 조각의 하이라이트 버전에 대란 엔드 포인트 만들기
API에서 아직까지 만들지 않은 부분은 코드 조각의 하이라이트 버전을 볼 수 있는 방법입니다.

API의 다른 부분과는 달리 이번에는 JSON 대신 HTML 형태로 나타내겠습니다 REST 프레임워크에서 HTML로 렌더링하는 방식은 두 가지 정도가 있는데, 하나는 템플릿을 사용하는 것이고, 다른 하나는 미리 렌더링 된 HTML 을 사용하는 것입니다. 후자를 사용하겠습니다.

하이라이트 된 코드 조각을 보여주려고 할 때 주의해야할 점은, 우리가 사용할 만한 제네릭 뷰가 없다는 것입니다. 오브젝트 자체가 아니라, 오브젝트의 속성 하나를 반호나할 것이기 때문입니다.

제네릭 뷰 대신 평범한 클래스를 사용하고, .get() 메서드를 구현합니다.

```
# views.py

from rest_framework import renderers  
from rest_framework.response import Response

class SnippetHighlight(generics.GenericAPIView):  
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
```

url도 연결

```
# 최상단 url
url(r'^$', views.api_root), 
# 하이라이트 조각 url
url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),  
```

#### 하이퍼링크로 API 연결하기

관계를 표현하는 방법은 다양합니다.

- 주 키(primary key)
- 하이퍼링크
- 관계 요소의 식별 가능한 슬러그(slug)필드
- 관계 요소의 기본 문자열 표현
- 포함된 관계 요소에 대한 표현
- 이 외에도 사용자화된 표현

REST 프레임워크는 모든 방법을 지원합니다.


하이퍼링크 방식을 사용하려면 기존에 사용했던 ModelSerializer를 HyperlinkedModelSerialzer로 변경해야합니다.

HyperlinkedModelSerializer는 다음과 같은 점들이 다릅니다.

- pk 필드는 기본 요소가 아닙니다.
- HyperlinkedIndentityField 대신 HyperlinkedRelatedField를 사용하여 나타냅니다.

```
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highllight', format='html')
    
    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('user', 'usernama', 'snippets')
```

'highlight' 필드가 추가되었습니다. 이 필드는 url 필드와 같은 타입이며, 'snippet-detail' url 패턴 대신 'snippet-highlight' url패턴을 가리킵니다.

앞에서 URL의  format 접미어로 '.json'을 붙엿듯이, highlight 필드에는 format 접미어로 '.html'을 붙였습니다.

### URL 패턴에 이름 붙이기
하이퍼링크 API를 만들려면 URL 패턴에 이름을 붙여야 합니다.

- API의 최상단은 'user-list'와 'snippet-list'를 가리킵니다.
- 코드 조각 시리얼라이저에는 'snippet-highlight'를 가리키는 필드가 존재합니다.
- 사용자 시리얼라이저에는 'snippet-detail'을 가리키는 필드가 존재합니다.
- 코드 조각 시리얼라이저와 사용자 시리얼라이저에는 'url' 필드가 존재합니다. 이 필드는 기본적으로 '{모델_이름}-detail'을 가리키며 따라서 'snippet-detail'과 'user-detail'을 가리킵니다.

```
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'users/$', views.UserList.as_view(), name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),



]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

### 페이징 기능 추가하기

REST 프레임워크의 모든 설정은 'REST_FRAMEWORK'라는 딕셔너리에 넣어야합니다.
이렇게 해야 프로젝트의 다른 설정들과 분리 할 수 있습니다.
필요에 따라 페이징 스타일을 바꿀수도 있습니다.

```
REST_FRAMEWORK = {  
    'PAGE_SIZE': 10
}
```

### 탐색 가능한 API
탐색 가능한  API를 브라우저에서 열어서 링크들을 이리저리 눌러보면, API의 구석구석을 둘러볼 수 있습니다.

## 6. 뷰셋과 라우터

REST 프레임워크는 ViewSets이라는 추상클래스를 제공ㄹ합니다, 이를 통해 개발자는 API의 상호작용이나 상태별 모델링에 집중할 수 있고, URL 구조는 기본 관럐에 따라 자동을 성정됩니다.

ViewSet 클래스는 Views 클래스와 거의 비슷하지만, get, put 메서드는 지원하지 않고 read, update 메서드를 지원합니다.

ViewSet 클래스는 앞서 만든 핸들러 메서드가 실제 뷰로 구체화 될때 이를 연결해주기만 합니다, 이 떄 보통은 Router 클래스를 사용하여 복잡한 URL 설정을 처리합니다.

### 뷰셋을 사용하여 리팩터링하기

UserList와 UserDetail 뷰를 UserViewSet 하나로 모읍니다.

```
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```
ReadOnlyModelViewSet 클래스는 '읽기 전용' 기능을 자동으로 지원합니다. queryset과 serializer_class 속성은 여전히 설정해야하지만 두개의 클래스에 중복으로 설정할 필요는 없어졌습니다.

SnippetList와 SnippetDetail, SnippetHighlight 뷰를 리팩터링합니다.

```
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

읽기 기능과 쓰기 기능을 모두 지원하기 위해 ModelViewSet 클래스를 사용했습니다.

추가한 highlight 기능에는 여전히 @detail_router 데코레이터를 사용했습니다. 이 데코레이터는 create나 update에 해당하지 않는 기능에 대해 사용하면 됩니다.

@detail_router 데코레이터를 사용한 기능은 기본적으로 GET 요청에 응답합니다. method 인자를 설정하면 POST 요청에도 응답할 수 있습니다.

추가 기능의 URL은 기본적으로 메서드 이름과 같습니다. 이를 변경하고 싶다면 데코레이터에 url_path 인자를 설정하면 됩니다.























