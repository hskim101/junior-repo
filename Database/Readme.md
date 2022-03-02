Database
========
시험 공부 자료 정리
---------------

# Chap 1. Introduction
* Data Models
  - Relational Model
    + 표로 데이터를 나타냄
    + Table 각각을 Relation 이라고 부른다.
  - Entity\-Relationship data model

<p align="center">
 <img width="300" height="300" alt="스크린샷 2022-03-02 오후 5 10 37" src="https://user-images.githubusercontent.com/59719632/156321264-31d8cba2-2ca5-417c-a9df-405903688dfa.png"> <img width="300" height="300" alt="스크린샷 2022-03-02 오후 5 10 13" src="https://user-images.githubusercontent.com/59719632/156321456-48612304-1426-4cb6-bc5f-a308f289dab2.png">
<p/>

* Instances and Schemas
  - Insatnaces (variable) : 틀을 따르는 Table
    + Instance : 실제 데이터베이스의 특정 시점에서의 내용
  - Schemas (type) : 어떠한 틀을 제공
    + Logical Schema : column name
    + Physical schema : 생략

* Physical Data Independence
  - physical level에서 수정된 내용이 logical level에 영향을 미치지 않음

* Data Definition Language (DDL)
  - Specification notation for defining the database schema
  - DDL compiler는 table 정보를 data dictionary에 저장한다.
  - Data dictionary는 metadata (data에 대한 data)를 담고있다.
    + Database schema (columns data)
    + Integrity constraints
      * Primary key (각 행들을 구분하기 위해 unique한 data로 이루어진 column)
    + Authorization : 접근 권한 조건
 
```mysql
CREATE TABLE instructor (
       ID char(5),
       name varchar(20), 
       dept_name varchar(20), 
       salary numeric(8,2) # 소숫점 2자리 포함
       )
```

* Data Manipulation Language (DML)
  - Query라고도 불린다.
  - Procedural DML : 내가 원하는 답을 얻기 위해 절차를 일일이 다 써줌
  - Declarative DML : 내가 원하는 답을 얻기 위한 절차는 신경쓰지 않음
    + 사용하기 쉽다.
    + SQL이 선언적 DML에 포함된다.
  
* SQL Query Language
  - nonprocedural
  - **always returns a single table**
  - 다른 상위 레벨의 언어와 같이 사용해야한다.
 
* Database Design
  - Logical Design
    + Business decision : 어떠한 attributes가 필요한지 결정
    + Computer Science decision : 효율성 중요시함, 공간적 측면과 시간적 측면 고려

* Database Engine
  - Storage manager
    + OS file manager와 interaction
      * Data files \- database table들 자신
      * Data dictionary \- metadata 저장, schema 저장
      * Indices \- 빠른 접근을 위해 index 제공
    + 효율적으로 data를 저장, 업데이트
  - Query processor component
    + DDL interpreter \- DDL을 해석해서 Data dictinary에 저장
    + DML compiler \- DML을 처리하기 위한 명령어를 번역해서 기계에 전달, cost가 가장 적은 방법으로 처리
  - Transaction management component
    + Transaction : 하나의 함수처럼 동작해야하는 명령어들의 집합
    + transaction에 문제가 생겼을 때 correct state를 유지하도록 만들어주는 component
    + Concurrency\-control manager : 여러 개의 transaction들이 실행되도 database에 문제가 없도록 유지해줌
<img width="400" height="400" alt="스크린샷 2022-03-02 오후 6 28 19" src="https://user-images.githubusercontent.com/59719632/156333774-2d77d943-7191-4aa8-8d29-3f4c7558266d.png">

* Database Applications
  - Two\-tier architecture
    + 사용자가 직접 database system에 query를 날림
    + 보안에 취약
  - Three\-tier architecture
    + 사용자가 application server와 교신해서 직접적으로 query를 날리지는 않음

* Database Users

<img width="400" height="400" alt="스크린샷 2022-03-02 오후 6 40 55" src="https://user-images.githubusercontent.com/59719632/156335988-3553cdc9-f6b3-49f4-bf4b-b455a34ec36b.png">

* Database Administrator (DBA)
  - Schema 정의
  - database를 어디에 저장할지, 어떻게 접근할지 정의
  - Schema and physical\-organization 변경
  - data access 권한 부여
  - 주기적 백업
  - database가 커질 수록 disk 용량 부족함 없도록 업그레이드
  - 성능 모니터링



