# Jenkins Pipeline

## 서술적 파이프라인 문법

### 서술적 파이프라인의 기본 구조

- 노드 블록
 - 스테이지 블록, 디렉티브, 스텝이 실행될 젠킨스 에이전트를 정의한다.
 - 정의: 스테이지, 디렉티브, 스텝이 실행될 노드
 - 구성: 여러 개의 스테이지 블록, 디렉티브 또는 스텝
 - 필수
 - 파라미터: any, label

```
node ('<parameter>') {<constituents>}
```

- 스테이지 블록
 - 같은 목적을 가진 스텝과 디렉티브의 모음
 - 정의: 스텝과 디렉티브의 모음
 - 구성: 여러 개의 노드 블록, 디렉티브 또는 스텝
 - 필수
 - 파라미터: 스테이지의 이름(필수)
 
 ```
 stage ('<parameter>') {<constituents>}
 ```
 
 - 디렉티브
  - 환경변수, 옵션, 파라미터, 트리거, 툴을 제공해 노드 블록과 스테이비 블록, 스텝을 지원한다.
  - 정의: 스테이지가 실행될 노드
  - 구성: 환경변수, 옵션, 파라미터, 트리거, 툴
  - 필수 아님. 모든 CI/CD 파이프라인이 디렉티브를 가지고 있음
  - 파라미터: 없음
  
- 스텝
 - 정의: 젠킨스에서 무엇을 할지 명령을 내리는 것
 - 구성: 명령어, 스크립트 등 파이프라인의 핵심 요소
 - 필수는 아니지만, 모든 CI/CD 파이프라인이 디렉티브를 가지고 있음
 - 파라미터: 없음
 
 ```
 // Node block
 node ('master') {
   // Directive 1
   def mvnHome
   
   // Stage block 1
   stage('Preparation') {
     // Step 1
     git 'https://github.......git'
     // Directive 2
     mvnHome = tool 'M3'
   }
   
   // Stage block 2
   stage('Build') {
     // Step 2
     sh "'${mvnHome}/bin/mvn' clean install"
   }
   
   // Stage block 3
   stage('Results') {
     // Step 3
     junit '**/target/su.....xml'
     // Step 4
     archive 'target/*.jar'
   }
 }
 ```
 
 any 파라미터로 사용하면 모든 스테이지 노드와 스텝, 디렉티브의 임의의 젠킨스 슬레이브 중 하나에서 수행된다.
 
## 젠킨스 파이프라인 문법 도구

- 전역도구 환경 설정 에서 메이븐 도구 설정해야 함
- 파이프라인 메이븐 통합 플러그인 설치

### 파이프라인 메이븐 통합 플러그인 설치

- 플러그인 관리에서 Pipeline Maven Integration 을 설치

### 파이프라인 문법 도구를 이용해 젠킨스 파이프라인 만들기

1. 파이프라인 영역에서 Pipeline Syntax를 선택하면, 새로운 창이 열린다.  
2. Step의 Sample Step에서 node:Allocate node를 선택한다.  
3. Label에 master를 입력한다. 이를 통해 젠킨스가 젠킨스 마스터를 이용해 파이프라인을 실행하게 졍의한다.  
4. Generate Pipeline Script를 클릭해 코드를 생성한다.
5. 생성된 코드를 텍스트 에디터에 보관한다.

```
node('master') {
    // some block
}
```

Preparation, Build 두 개의 스테이지 블록을 생성
- Pipeline Syntax 페이지의 Step 아래 Sample Step 에서 stage: Stage를 선택
- Stage Name에 Preparation 추가
- Generate Pipeline Script 를 클릭하여 코드를 생성
- 생성된 코드를 복사해 이전에 생성한 노드 블록안에 복사
- build 라는 이름의 스테이비지 블록을 생성하여, 같은 과정을 반복한다.

현재까지의 파이프라인 코드

```
node('master') {
    stage('Preparation') {
    }
    
    stage('Build') {
    }
}
```

- 깃헙에서 소스코드 내려 받기
 - Pipeline Syntax에서 Sample Step에서 git: Git 선택
 - 깃헙 주소 입력 (예제: https://github.com/jglick/simple-maven-project-with-tests.git)
 - 나머지는 놔두고 코드를 생성하고 파이프라인 코드의  Preparation 스테이지 블록안에 붙여넣는다.

```
node('master') {
    stage('Preparation') {
      git 'https://github.com/jglick/simple-maven-project-with-tests.git'
    }
    
    stage('Build') {
    }
}
```

- 전역 도구 환경성정에서 설정한 메이븐을 사용
 - Pipeline Syntax의 Sample Step에서 withMaven: Provide Maven environment 선택
 - Maven 영역에 이전에 전역 도구 환경 설정에서 설정하나 M3를 선택
 - 나머지 옵션은 그대로두고 코드를 생성
 - Build 스테이지 블록에 붙여넣기
 
```
node('master') {
    stage('Preparation') {
      git 'https://github.com/jglick/simple-maven-project-with-tests.git'
    }
    
    stage('Build') {
      withMaven(maven: 'M3') {
      }
    }
}
```

- 메이븐 빌드 명령을 위한 파이프라인 코드 생성
 - Pipeline Syntax의 Sample Step에서 sh: Shell Script 선택
 - Shell Script에 `mvn -Dmaven.test.failure.ignore clean package`를 입력. 빌드, 테스트, 코드의 패키징을 위한 메이븐 명령어임.
 - 코드를 생성하여 withMaven 디렉티브 안에 붙여 넣는다.
 
```
node('master') {
    stage('Preparation') {
      git 'https://github.com/jglick/simple-maven-project-with-tests.git'
    }
    
    stage('Build') {
      withMaven(maven: 'M3') {
        sh 'mvn -Dmaven.test.failure.ignore clean package'
      }
    }
}
```

위 코드를 파이프라인 잡 설정 페이지의 Pipeline 섹션의 Script 영역에 붙여넣고 save 한다.

## 멀티브랜치 파이프라인

2.x 릴리스에서 새로 추가된 기능.  
멀티브랜치 파이프라인은 사용자가 소스코드 저장소의 모든 브랜치에 대해 파이프라인을 자동으로 생성하게 해줌.  
깃이나 깃허브 저장소의 브랜치 중 어떤 곳에서 변경이 발생하면 자동으로 빌드를 시작하기 위해 설계됨.

### 깃허브 인증을 젠킨스에 추가

젠킨스의 Credentials plugin을 통해 진행.

- 대시보드에서 Credentials -> System -> Global credentials(unrestricted)를 선택
- 왼쪽 사이드에서 Global credentials(unrestricted)에서 Add Credentials 링크를 클릭
 - kind: Username with password
 - Scope: Global(Jenkins nodes, items, all child items, etc)
 - Username: 사용자의 깃허브 사용자명
 - Password:  깃헙 비번
 - ID: 문자열을 입력해 인증을 위한 고유한 ID를 생성
 - Description: 설명 입력
 - Save
 
### 젠킨스에서 깃허브 Webhooks 설정

- 젠킨스 대시보드에서 Manage Jenkins -> Configure System
- GitHub 섹션에서 Add Github Server 클릭하고, GitHub Servers를 목록에서 선택
 - Name: 깃허브 서버의 이름
 - 공용 깃헙 계정이라면 API URL 영역에 기본값인 https://api.github.com 을 작성. 
 - Manage Hooks 옵션 체크
 - Advanced 클릭 (같은 이름의 버튼이 2개임. 두번째꺼)
 - Additional actions에서 Manage additional GitHub actions 클릭 후 Convert login and password to token을 선택
 - From credentials 옵션 선택. 깃허브 인증을 선택
 - Create token credentials 버튼을 클릭. 깃허브 계정에 접근하기 위한 새로운 개인 접속 토큰이 생성됨
- 깃헙에서 개인 접속 토큰을 확인하려면, 깃헙에서 Settings -> Developer settings -> Personal access tokens 로 이동
- 완료한 후 젠킨스 환경 설정 페이지 하단의 Save
- 해당하는 개인 접속 토큰이 젠킨스 인증에도 추가됨. 이를 확인하려면 Jenkins dashboard -> Credentials -> System -> api.github.com 으로 이동 후 Kind 영역의 secret text에서 확인 가능

> 이 부분이 잘안되는데...구글링해보니 그냥 깃헙에서 토큰을 발행하고, 젠킨스에 입력하는 방식으로 해야 하는 듯.


- 젠킨스 대시보드에서 Manage Jenkins -> Configure System
- GitHub -> Credentials 영역에 새롭게 생성된 Kind 영역의 secret text(젠킨스의 개인 접ㅈ속 토큰)을 선택
- Test Connection으로 연동 체크
- 완료후 Save

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

### 새로운 깃허브 저장소 만들기

### Jenkinsfile 이용하기

### 젠킨스에서 멀티브랜치 파이프라인 생성하기

### Webhooks 재등록

### 젠킨스 멀티브랜치 파이프라인 인 액션

### 멀티브랜치 파이프라인 테스트를 위해 새로운 기능 브랜치 만들기

## 젠킨스 블루오션

### 젠킨스 블루오션 플러그인 설치

### 블루오션에서 기본적인 젠킨스 파이프라인 살펴보기

### 블루오션에서 파이프라인 생성하기

