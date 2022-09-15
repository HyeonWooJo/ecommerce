# 목차

1. e-commerce
2. 구현사항
3. 기술 스택
4. API Endpoints
5. ERD
6. 참조 문서

<br>

---

# 1. e-commerce
- 회원가입/로그인부터 제품 포스팅, 주문까지 할 수 있는 사이트
- 개발 기간: 2022.09.09 ~ 2022.09.14

<br>

---


# 2. 구현 사항

## 1) 회원가입/로그인

- 회원가입
- 로그인
    - SimpleJWT 사용
    - 로그인 시 access token 발급

<br>

## 2) 제품 CRUD

- 제품 Create
    - 관리자가 아닐 경우 생성 불가
    - 썸네일과 나머지 이미지를 나눠서 저장
- 제품 Read
    - 모든 유저 조회 가능
    - 제품 리스트, 상세 조회 기능 구현
- 제품 Update
    - 관리자가 아닐 경우 수정 불가
- 제품 Delete
    - 관리자가 아닐 경우 삭제 불가


<br>

## 3) 상세주문 CRUD

- 상세 주문 Create
    - 모든 유저 생성 가능
- 상세 주문 Read
    - 모든 유저 조회 가능
    - 상세 주문 리스트, 상세 조회 기능 구현
- 상세 주문 Update
    - 상세 주문 생성 유저와 관리자만 수정 가능
- 상세 주문 Delete
    - 상세 주문 생성 유저와 관리자만 삭제 가능

<br>

## 4) 주문 CRUD

- 주문 Create
    - 모든 유저 생성 가능
- 주문 Read
    - 모든 유저 조회 가능
    - 주문 리스트, 상세 조회 기능 구현
- 주문 Update
    - 주문 생성 유저와 관리자만 수정 가능
- 주문 Delete
    - 주문 생성 유저와 관리자만 삭제 가능

<br>

## 5) 결제 CRUD

- 결제 Create
    - 모든 유저 생성 가능
- 결제 Read
    - 모든 유저 조회 가능
    - 결제 리스트, 상세 조회 기능 구현
- 결제 Update
    - 결제 생성 유저와 관리자만 수정 가능
- 결제 Delete
    - 주문 생성 유저와 관리자만 삭제 가능



<br>

---

# 3. 기술 스택
Language | Framwork | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | 
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 


<br>

---

# 4. API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /api/users/register/  | POST   | 회원가입 |  username: string <br/> password: string <br/> age: string | 유저 정보 |
| /api/users/signin/  | POST     | 로그인  | sername: string <br/> password: string  | 성공 여부 메시지 <br/> access_token <br/> refresh_token  |
| /api/users/delete/:int:/  | DELETE   | 계정 삭제 |  없음  | 계정 삭제 성공 여부 |
| /api/products/mixin/post/ | POST   | 제품 생성 |  name: string <br/> price: int<br/> content: string <br/> origin: string <br/> quantity: int <br/> mainimage: image <br/> image: image  | 제품 상세 |
| /api/products/mixin/post/  | GET   | 제품 리스트 조회 |  없음  | 제품 리스트 |
| /api/products/mixin/post/:int:/  | GET   | 제품 상세 조회 |  없음  | 제품 상세 |
| /api/products/mixin/post/:int:/  | PUT   | 제품 상세 수정 |  없음  | 제품 상세 |
| /api/products/mixin/post/:int:/  | DELETE   | 제품 삭제 |  없음  | 제품 삭제 성공 여부 |
| /api/orders/  | POST   | 주문 생성 |  user: int  | 주문 상세 |
| /api/orders/  | GET   | 주문 리스트 조회 |  없음  | 주문 리스트 |
| /api/orders/:<int>/  | GET   | 주문 상세 조회 |  없음  | 주문 상세 |
| /api/orders/:<int>/  | PUT   | 주문 상세 수정 |  없음  | 주문 상세 |
| /api/orders/:<int>/  | DELETE   | 주문 상세 삭제 |  없음  | 주문 상세 |
| /api/orders/detail/  | POST   | 상세 주문 생성 |  user: int  | 상세 주문 상세 |
| /api/orders/detail/  | GET   | 상세 주문 리스트 조회 |  없음  | 상세 주문 리스트 |
| /api/orders/detail/:int:/  | GET   | 상세 주문 상세 조회 |  없음  | 상세 주문 상세 |
| /api/orders/detail/:int:/  | PUT   | 상세 주문 상세 수정 |  없음  | 상세 주문 상세 |
| /api/orders/detail/:int:/  | DELETE   | 상세 주문 상세 삭제 |  없음  | 상세 주문 상세 |
| /api/orders/payment/  | POST   | 결제 생성 |  user: int  | 결제 상세 |
| /api/orders/payment/  | GET   | 결제 리스트 조회 |  없음  | 결제 리스트 |
| /api/orders/payment/:int:/  | GET   | 결제 상세 조회 |  없음  | 결제 상세 |
| /api/orders/payment/:int:/  | PUT   | 결제 상세 수정 |  없음  | 결제 상세 |
| /api/orders/payment/:int:/  | DELETE   | 결제 상세 삭제 |  없음  | 결제 상세 |

<br>

---

# 5. ERD
![](https://user-images.githubusercontent.com/65996045/190115818-72ead3fd-ac7d-47e9-a1a9-73c590a362fc.png)

<br>

---

# 6. 참조 문서
- [Postman API Docs](https://documenter.getpostman.com/view/21254145/2s7YYvYgZn)


