# TDD (Test-Driven Development, 테스트 주도 개발)

Functional test(FT) : 기능 테스트
셀레늄을 이용하 테스트에서는 실제 웹 브라우저를 실행해서 애플리케이션이 어떻게 "동작(functiona)"하는지 사용자 관점에서 확인 할 수 있다.
FT는 사람이 이해 할 수 있는 스토리를 가지고 있어야 한다. 이것을 분명하게 정의하기 위해 테스트 코드에 주석을 기록한다. 프로그래머가 아니더라도 이해할 수 있어야한다.(애플리케이션 요구사항과 특징을 FT를 보고 논의 할 수 있을 정도)

```
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

부분적 설명

`setUp`와 `tearDown`은 특수한 메소드이다. 각 테스트 시작 전과 후에 실행된다.  
여기선는 브라우저를 시작하고 닫을 때 사용하고 있다. 테스트에 에러가 발생해도 tearDown이 실행된다.

```
        self.fail('Finish th test!')
        # 강제적으로 테스트 실해를 발생시켜 에러 메세지를 출력한다
        # 테스트가 끝났다는 것을 알리기 위해 사용하고 있다
```


```
        self.browser.implicitly_wait(3)
        # 셀레늄 테스트의 기본적인 로직이다
        # 페이지 로딩이 끝날때까지 기다렸다가 테스트를 실행한다
        # 하지만 완벽하지 않다
        # 이후에 '명시적인' 대기 알고리즘을 별도로 작성해야한다
```
