# TDD (Test-Driven Development, 테스트 주도 개발)

## 1부

## 2장 unittest 모듈을 이용한 기능 테스트 확장
### Functional test(FT) : 기능 테스트
셀레늄을 이용하 테스트에서는 실제 웹 브라우저를 실행해서 애플리케이션이 어떻게 "동작(functiona)"하는지 사용자 관점에서 확인 할 수 있다.
FT는 사람이 이해 할 수 있는 스토리를 가지고 있어야 한다. 이것을 분명하게 정의하기 위해 테스트 코드에 주석을 기록한다. 프로그래머가 아니더라도 이해할 수 있어야한다.(애플리케이션 요구사항과 특징을 FT를 보고 논의 할 수 있을 정도)

```python
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 앱 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        self.assertIn('To-Do', self.browser.title)

```

#### 부분적 설명

`setUp`와 `tearDown`은 특수한 메소드이다. 각 테스트 시작 전과 후에 실행된다.  
여기선는 브라우저를 시작하고 닫을 때 사용하고 있다. 테스트에 에러가 발생해도 tearDown이 실행된다.

```python
        self.fail('Finish th test!')
        # 강제적으로 테스트 실해를 발생시켜 에러 메세지를 출력한다
        # 테스트가 끝났다는 것을 알리기 위해 사용하고 있다
```


```python
        self.browser.implicitly_wait(3)
        # 셀레늄 테스트의 기본적인 로직이다
        # 페이지 로딩이 끝날때까지 기다렸다가 테스트를 실행한다
        # 하지만 완벽하지 않다
        # 이후에 '명시적인' 대기 알고리즘을 별도로 작성해야한다
```

### 유용한 TDD 개념
#### 사용자 스토리(User story)
사용자 관점에서 어떻게 애플리케이션이 동작해야 하는지  기술한 것이다. 기능 테스트 구조화를 위해 사용한다.

#### 예측된 실패(Expected failure)
의도적으로 구현한 테스트 실패를 의미한다.

## 3장 단위 테스트를 이용한 간단한 홈페이지 테스트

### 단위 테스트와 기능 테스트의 차이
**기능 테스트**는 **사용자 관점에서 애플리게이션 외부**를 테스트하는 것이고, **단위 테스트**는 **프로그래머 관점에서 그 내부**를 테스트한다는 것이다.

#### 작업 순서

1. 기능 테스트를 작성해서 사용자 관점의 새로운 가능성을 정의하는 것부터 시작한다.
2. 기능 테스트가 실패하고 나면 어떻게 코드를 작성해야 테스트를 통과할지(또는 적어도 현재 문제를 해결할 수 있는 방법)을 생각해본다. 이 시점에서 하나 또는 그 이상의 단위 테스트를 이용해서 어떻게 코드가 동작해야 하는지 정의한다(기본적으로 모든 코드가(적어도) 하나 이상의 단위 테스트에 의해 테스트 되어야 한다.)
3. 단위 테스트가 실패하고 나면 단위 테스트를 통과할 수 있을 정도의 최소한의 코드만 작성한다. 기능 테스트가 완전해질 때까지 과정 2,3을 반복해야 할 수도 있다.
4. 기능 테스트를 재실행해서 통과하는지 또는 제대로 동작하는지 확인한다. 이 과정에서 새로운 단위 테스트를 작성해야 할 수도 있다.

이 과정을 보면, 기능 테스트는 상위 레벨의 개발을 주도하고, 단위 테스트는 하위 레벨을 주도한다는 것을 알 수 있다.
기능 테스트와 단위 테스트가 전혀 가른 목적을 가지고 있어서 서로 다른 결과를 초래할 수 있기 때문에 꼭 필요한 과정이다.

기능 테스트는 제대로 된 기능성을 갖춘 애플리케이션을 구축하도록 도우며, 그 기능성이 망가지지 않도록 보장해준다. 반면, 단위 테스트는 깔끔하고 버그 없는 코드를 작성하도록 돕는다.

### Django에서의 단위 테스트
#### Django의 처리 흐름
1. 특정 URL에 HTTP "요청"을 받는다.
2. Django는 특정 규칙을 이용해서 해당 요청에 어떤 뷰 함수를 실행항지 결정한다.
3. 이 뷰 기능이 요청을 처리해서 HTTP "응답"으로 반환한다.

#### 따라서 우리가 테스트해야 할 것

- URL의 사이트 루트("/")를 해석해서 특정 뷰 기능에 매칭시킬 수 있는가?
- 이 뷰 기능이 특정 HTML을 반환하게 해서 기능 테스트를 통과할 수 있는가?

```python
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
```
#### 부분적인 설명
resolve는 Django가 내부적으로 사용하는 함수로, URL을 해석해서 일치하는 뷰 함수를 찾는다. 여기서는 "/"(사이트 루트)가 호출될 때 resolve를 실행해서 home_page라는 함수를 호출한다.

### 트레이스백 읽기
트레이스백(Traceback)은 TDD에 있어 중요한 역할을 하는것으로 자주 접하게 된다. 트레이스백을 빠르게 읽어서 필요한 단서를 찾는 방법을 금방 배울수 있다.

```
======================================================================
ERROR: test_root_url_resolves_to_home_page_view (lists.tests.HomePageTest)1
 ---------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/superlists/lists/tests.py", line 8, in
test_root_url_resolves_to_home_page_view
    found = resolve('/')2
  File "/usr/local/lib/python3.4/dist-packages/django/core/urlresolvers.py",
line 522, in resolve
    return get_resolver(urlconf).resolve(path)
  File "/usr/local/lib/python3.4/dist-packages/django/core/urlresolvers.py",
line 388, in resolve
    raise Resolver404({'tried': tried, 'path': new_path})
django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLResolver3
<RegexURLPattern list> (admin:admin) ^admin/>]], 'path': ''}4
 ---------------------------------------------------------------------
[...]
```


3.4. 먼저 확인해야 할 것이 **에러**다. 이 에러 부분이 핵심인데, 어떤 때는 이 부분만 읽고 바로 문제를 파악할 수 있다. 하지만 이 예제의 경우는 에러만으로는 충분히 문제 파악이 어렵다.
1. 다음으로 확인할 것은 **"어떤 테스트가 실패하고 있는가?"**다. 이 실패가 예측된 실패인지를 확인해야 한다. 이 예에서는 예측된 실패이다.
2. 마지막으로 **실패를 발생시키는 "테스트 코드"를 찾는다.** 트레이스백 상단부터 아래로 내려가면서 테스트 파일명을 찾는다. 그래서 어떤 테스트 함수의 몇 번째 코드 라인에서 실패가 발생하는지 확인한다. 이 예에선 resolve 함수를 호출해서 "/" URL을 해석하는 부분이다.

문제 있는 코드를 확인할때 일반적으로 사용하는 4단계 과정이다.
이렇게 모든 정보를 취합해 트레이스백을 해석한 결과, "/"를 확인하려고 할 때 Django가 404 에러를 발생시키고 있다는 것을 알 수 있다.

#### 부분적인 설명
```python
 def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #1
        response = home_page(request)  #2
        self.assertTrue(response.content.startswith(b'<html>'))  #3
        self.assertIn(b'<title>To-Do lists</title>', response.content)  #4
        self.assertTrue(response.content.endswith(b'</html>'))  #5
```
1. HttpRequest 객체를 생성해서 사용자가 어떤 요청을 브라우저에 보내는지 확인한다.
2. 이것을 home_page 뷰에 전달해서 응답을 취득한다. 이 객체는 HttpResponse라는 클래스의 인스턴스이다. 응답내용(HTML 형태로 사용자에세 보내는것)이 특정 속성을 가지고 있는지 확인한다.
3.5. 그 다음은 응답 내용이 <html>으로 시작하고  </html>으로 끝나는지 확인한다. response.content는 byte형 데이터로, 파이썬 문자열이 아니다. 따라서 b''구문을 사용해서 비교한다.
4. 반환 내용의 `<title>` 태그에 "To-Do lists"라는 단어가 있는지 확인한다. 앞선 기능 테스트에서 확인한 것이기 때문에 단위 테스트로 확인해주어야 한다. 

여기서부터 **TDD 단위 테스트 - 코드 주기** 에 대해 생각해야 한다.

1. 터미널에서 단위 테스트를 실행해서 어떻게 실패하는지 확인한다.
2. 편집기상에서 현재 실패 테스트를 수정하기 위한 최소한의 코드를 변경한다.

코드 품질을 높이고 싶다면 코드 변경을 최고화해야한다. 또한 이렇게 최소화한 코드는 하나하나 테스트에 의해 검증돼야 한다. 매우 고된 작업이라고 생각될 수 있지만, 한번 익숙해지기 시작하면 속도는 빨라진다. 따라서 아무리 자신 있는 부분이라도 작은 단위로 나누어 코드를 변경하도록 한다.

### 기억해두면 좊은 명령어
##### 기능 테스트 실행
python3 functional_test.py
##### 단위 테스트
python3 manage.py test

## 4장 왜 테스트를 하는 것인가?
TDD가 훌륭한 이유 중 하나가 다음에 무엇을 해야 할지 잊어버릴 걱정이 없다는 것이다. 테스트를 다시 실행하기만 하면 다음 작업이 무엇이닞 가르쳐준다.

```python

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 앱 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-Do'를 표시하고 있다
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 그녀는 바로 추가하기로 한다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # "공작깃털 사기"라고 텍스트 상자에 입력한다
        # (에디스의 취미는 날치 잡이용 그물을 만드는 것이다)
        inputbox.send_keys('Buy peacock feathers')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 공작깃털 사기" 아이템이 추가된다
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다
        # 대시 "공작깃털을 이용해서 그물 만들기"라고 입력한다(에디스는 매우 체계적인 사람이다)
        self.fail('Finish the test!')
```

셀레늄이 제공하는 다양한 메소드를 사용하고 있다. `find_element_by_tag_name`, `find_element_by_id`, `find_elements_by_tag)bane`등이다. 셀레늄의 입력 요소를 타이핑하는 방법인 `send_keys`라는 것도 사용한다.
> element와 elements의 차이점에 유의해야한다. 전자는 하나의 요소만 반환하며 요소가 없으면 예외를 발생시킨디. 반면 후자는 리스트를 반환하며 이 리스트가 비어 있어도 괜찮다.

### "상수는 테스트하지 마라"는 규칙과 탈출구로 사용할 템플릿
단위 테스트는 로직이나 흐름 제어, 설정 등을 테스트하기 위한 것이다. 정확히 어떤 글자들이 HTML 문자열이 배열되어 있는지 체크하는 어썰션은 아무 의미가 없다.

#### 템플릿을 사용하기 위한 리팩터링
리팩터링(Refactoring)이란 **"기능(결과물)은 바꾸지 않고"** 코드 자체를 개선하는 작업을 일컫는다.


#### 트래이스백 분석

```
$ python3 manage.py test
[...]
======================================================================
ERROR: test_home_page_returns_correct_html (lists.tests.HomePageTest) #1
 ---------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/superlists/lists/tests.py", line 17, in
test_home_page_returns_correct_html
    response = home_page(request) #2
  File "/workspace/superlists/lists/views.py", line 5, in home_page
    return render(request, 'home.html') #3
  File "/usr/local/lib/python3.3/dist-packages/django/shortcuts.py", line 48,
in render
    return HttpResponse(loader.render_to_string(*args, **kwargs),
  File "/usr/local/lib/python3.3/dist-packages/django/template/loader.py", line
170, in render_to_string
    t = get_template(template_name, dirs)
  File "/usr/local/lib/python3.3/dist-packages/django/template/loader.py", line
144, in get_template
    template, origin = find_template(template_name, dirs)
  File "/usr/local/lib/python3.3/dist-packages/django/template/loader.py", line
136, in find_template
    raise TemplateDoesNotExist(name)
django.template.base.TemplateDoesNotExist: home.html #4 

 ---------------------------------------------------------------------
Ran 2 tests in 0.004s
```
4. 먼저 에러를 확인하자: 템플릿을 발견할 수 없어서 에러가 발생하고 있다.
1. 어떤 테스트가 실패하는지 다시 확인한다: HTML 뷰 테스트 부분이다.
2. 테스트의 어느 코드에 문제가 있는지 확인한다: home_page 함수 호출에 문제가 있다.
3. 마지막으로 애플리케이션의 어느 부분에서 에러가 발생하는지 확인한다: render 호출 부분에서 에러가 발생한다.

```python
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expexted_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expexted_html)
```
`.decode()`를 이용해서 `response.content` 바이트 데이터를 파이썬 유니코드 문자열로 반환한다. 이를 통해 바이트와 바이트를 비교하는것이 아니라 문자열과 문자열을 서로 비교할 수 있다.
여기서 중요한것은 상수를 태스트하는 것이 아니라 구현 결과물을 비교하는 것이다.

### 리팩터링에 관해

리팩터링 시에는 앱 코드와 테스트 코드를 한 번에 수정하는 것이 아니라 하나씩 수정해야 한다.

### 정리: TDD 프로세스

- 기능 테스트(Functional tests)
- 단위 테스트(Unit tests)
- 단위 테스트-코드 주기(Unit-test/code cycle)
- 리팩터링(Refectoring)

![](./images/tdd_cycle.png)

## 5장 사용자 입력 저장하기

기능 테스트에서 예측하지 못한 에러가 발생하면, 다음과 같은 사항을 디버깅해야한다.

- print문을 사용해서 현재 페이지 텍스트 등을 확인해본다.
- 에러 메세지를 개선해서 더 자세한 정보를 출력하도록 한다.
- 수동으로 사이트를 열어본다.
- time.sleep을 이용해서 실행 중에 있는 테스트를 잠시 정지시킨다.

Django의 CSRF(Cross-Site Request Forgery)보호는 사이트의 각 폼이 생성하는 POST 요청을 확인할 수 있는 토큰을 자동 생성한다. 이것은 중괄호와 퍼센트 표시를 사용해서 기술한다.  `{% ... %}` 세상에서 가장 입력하기 어려운 두 가지 키 조합이라고도 알려져 있다.

### 서버에서 POST 요청 처리

HttpRequest에 몇 가지 특수한 속성들을 사용하고 있는 것을 알 수 있다. 바로 .method와 .POST이다.(Django의 'request and response'참조)
또한 POST 요청에 의해 반환되는 HTML에서 텍스트를 확인한다. 이 테스트는 예측한 결과를 보여준다.

### 레드/그린/리팩터와 삼각법
단위 테스트-코드 주기를 레드(Red), 그린(Green), 리팩터(Refactor)로 설명하는 경우도 있다.

- 실패할 단위 테스트를 작성함으로써 작업을 시작한다(레드).
- 이 테스트를 통과할 최소 코드를 작성한다(그린). 편법이라도 상관없다.
- 코드를 리팩터링해서 이해할 수 있는 코드로 만든다.

그러면 리팩터 단계에서는 무얼하면 될까? '편법'이라고 한 것을 모두가 만족하는 방법으로 변경하기 위해선 어떻게 해야 할까?

한 가지 방법은 "중복을 제거"하는 것이다. 테스트가 마법의 상수(아이템 앞의 "1:" 같이)를 사용하고, 애플리케이션도 동일한 코드를 사용한다면 기술이 중복되기 때문에 정당화가 가능하다. 하지만 마법의 상수를 애플리케이션 코드에서 제거한다면 편법 사용을 중단해야 한다.
이 방법은 애매한 측면이 있다. 그래서 필자가 선호하는 방법은 "삼각법"(Triangulation)이다. 테스트가 마법의 상수 같은 편법 코드를 허용하지 않는다면, 다른 테스트를 작성해서 더 나은 코드를 작성하는 방법이다. 즉, "2:"로 시작하는 두 번째 아이템이 추가되더라도 이것을 확인할 수 있도록 FT를 확장하는 것이다.

### 스트라이크 세 개면 리팩터
무언가 나쁜 "코드 냄새"를 FT를 통해 맡을 수 있다.
DRY(Don't Repeat Yourself)라는 원리가 있는데, 즉 한번 정도는 복사-붙여넣기를 해줄 수 있지만, 같은 코드가 세번 등장하게 되면 중복을 제거해야한다는 이론이다.

기능 테스트를 리팩터링 한다. 핼퍼(Helper)메소드를 이용한다. `test_`으로 시작하는 메소드만 테스트로 실행된다는 것을 기억하자. 즉 `test_`외의 이름을 사용해서 사용자 정의 메소드를 만들 수 있다는 것이다.

### Django ORM과 첫 모델
객체 관계형 맵핑(Object-Relational Mapper, ORM)은 데이터베이스의 테이블, 레코드, 칼럼 형태로 저장돼 있는 데이터를 추상화한 것이다. 이것을 이용하면 익숙한 객체 지향 코드 방식을 이용해서 데이터베이스를 처리할 수 있다. 데이터베이스는 클래스로 표현하고, 칼럼은 속성, 레코드는 각 클래스의 인스턴스로 표현한다.

Django는 훌륭한 ORM을 탑재하고 있다. 또한 ORM을 이용해서 단위 테스트를 작성하면, 실제 ORM 사용법을 배울 수 있어서 좋다. 단위 테스트는 예측된 동작을 코드로 작성해야 하기 때문에 충분한 연습이 된다.

