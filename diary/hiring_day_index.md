## 보유 기술

프로그래밍언어

 - Python
 - HTML
 - CSS

프레임워크

 - Django

그 외 기술

- REST ful : API 제작 시스템
- TDD : 프로그램 개발방법
- AWS : 서버 배포 서비스
- PostgreSQL : DBMS의 일종
- Docker : 프로그램 이미지화 // 여러 서버를 사용할 때 프로그램 전체를 하나의 파일로 바꿔줌

f

## 프로젝트1. DB 설계 - DB 전체 구조 설계 - Base model 구축2. 컨텐츠 - 공공데이터 open API에서 제공되는 xml 데이터를 dict으로 변환하여 DB에 저장 - 컨텐츠의 각각 정보를 분류하여 필드에 저장하고 사용자 요청에 따라 serializer하여JSON형식으로 API 제공3. 검색 - 지역별, 공연일자별, 장르(콘서트, 미술, 무용 등) 필터링 제공 - 제목이나 콘텐츠 상세정보, 공연장 등 모든 관련 정보로 검색 제공4. 평가댓글 - 관심있는 컨텐츠에 대하여 댓글로 평가등록 제공 - 스팸차단을위해로그인한사용자만작성가능 - 댓글은모든사람이조회할수있음 - 댓글수정및삭제는댓글작성자만가능### 프로젝트 사용기술1. Python2. Django3. Django REST framework4. AWS(EC2, RDS, S3, ElasticBeanstalk)5. Docker6. PostgresSQL7. 공공데이터 open api### 기능1. 소셜(페이스북)으로 로그인2. 이메일로 일반 가입시 인증메일 발송3. 공공데이터 API에서 컨텐츠들을 DB에 저장4. 컨텐츠 요청 조건에 따라 필터링 (카테고리)5. 컨텐츠 상세정보 제공6. 컨텐츠댓글기능제공7. 원하는 정보 북마크 제공

-

## 프로젝트 설명
프로젝트명은 **PM 0603** (<http://www.pm0603.com/>)으로 퇴근후 퇴근길에 문화 생활을 즐길 수 있도록 종합 문화 컨텐츠 정보를 제공해주는 서비스

프로젝트 Git
<https://github.com/pm0603/backend2/tree/demo>

![](./images/pm0603.png)

## 프로젝트 전체 동작 원리
공공데이터  open API를 사용하여 컨텐츠 정보를 프로젝트 DB에 저장하고 사용자의 요청에 따라 컨텐츠 정보를 제공합니다.
이메일이나 페이스북으로 가입 및 로그인이 가능합니다. 페이스북으로 가입시 회원의 기본정보는 페이스북으로부터 제공받습니다.
이메일로 가입시 인증메일을 발송하여 인증을 받습니다.

로그인을 하지 않아도 사이트의 기능들은 사용이 가능하지만 댓글과 북마크 기능은 로그인을 해야만 사용이 가능합니다.


### 회원가입 인증  

#### 가입인증 메일 발송  
![](./images/send_email.png)

#### 가입인증메일 수신  
![](./images/valid_email1.png)

#### 인증메일 내용  
![](./images/valid_email2.png)

### 소셜(페이스북) 로그인
![](./images/facebook.png)

### Content Search

#### 지역별 검색(카테고리)  
<http://api.pm0603.com/api_content/?area=경기>

#### 장르별 검색(카테고리)  
<http://api.pm0603.com/api_content/?realm_name=콘서트>

#### 상세정보  
<http://api.pm0603.com/api_content/?seq= 114864>

#### 종합검색(메인검색)  
<http://api.pm0603.com/api_content/?q=어린이>

### 북마크
![](./images/bookmark1.png)

![](./images/bookmark2.png)

![](./images/bookmark3.png)

![](./images/detail.png)
### Comment

### 댓글조회  
![](./images/comment_list.png)

### 댓글등록  
![](./images/comment_create.png)

### 댓글수정  
![](./images/comment_update.png)

### 댓글삭제  
![](./images/comment_del.png)

<iframe width=900 height=563 src="https://www.youtube.com/embed/dnJTiUT_WdE"></iframe>

위 모든 내용은 
[API Documentation](https://kimdoky.gitbooks.io/pm0603-project-api-document/)에 기술해두었습니다.