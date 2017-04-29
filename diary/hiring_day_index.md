# FastCampus Project | PM 0603 - Web Programming 김도경

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