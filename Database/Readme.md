Database
========
시험 공부 자료 정리
---------------

# Chap 1. Introduction
## 1-1. Data Models
  * Relational Model
    - 표로 데이터를 나타냄
    - Table 각각을 Relation 이라고 부른다.
  * Entity\-Relationship data model

<p align="center">
 <img width="300" height="300" alt="스크린샷 2022-03-02 오후 5 10 37" src="https://user-images.githubusercontent.com/59719632/156321264-31d8cba2-2ca5-417c-a9df-405903688dfa.png"> <img width="300" height="300" alt="스크린샷 2022-03-02 오후 5 10 13" src="https://user-images.githubusercontent.com/59719632/156321456-48612304-1426-4cb6-bc5f-a308f289dab2.png">
<p/>

## 1-2. Instances and Schemas
  * Insatnaces (variable) : 틀을 따르는 Table
    + Instance : 실제 데이터베이스의 특정 시점에서의 내용
  * Schemas (type) : 어떠한 틀을 제공
    + Logical Schema : column name
    + Physical schema : 생략

## 1-3. Physical Data Independence
  - physical level에서 수정된 내용이 logical level에 영향을 미치지 않음

## 1-4. Data Definition Language (DDL)
  * Specification notation for defining the database schema
  * DDL compiler는 table 정보를 data dictionary에 저장한다.
  * Data dictionary는 metadata (data에 대한 data)를 담고있다.
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

## 1-5. Data Manipulation Language (DML)
  * Query라고도 불린다.
  * Procedural DML : 내가 원하는 답을 얻기 위해 절차를 일일이 다 써줌 (Relational Algebra)
  * Declarative DML : 내가 원하는 답을 얻기 위한 절차는 신경쓰지 않음
    + 사용하기 쉽다.
    + SQL이 선언적 DML에 포함된다.
  
## 1-6. SQL Query Language
  * nonprocedural
  * **always returns a single table**
  * 다른 상위 레벨의 언어와 같이 사용해야한다.
 
## 1-7. Database Design
  * Logical Design
    + Business decision : 어떠한 attributes가 필요한지 결정
    + Computer Science decision : 효율성 중요시함, 공간적 측면과 시간적 측면 고려

## 1-8. Database Engine
  * Storage manager
    + OS file manager와 interaction
      - Data files \- database table들 자신
      - Data dictionary \- metadata 저장, schema 저장
      - Indices \- 빠른 접근을 위해 index 제공
    + 효율적으로 data를 저장, 업데이트
  * Query processor component
    + DDL interpreter \- DDL을 해석해서 Data dictinary에 저장
    + DML compiler \- DML을 처리하기 위한 명령어를 번역해서 기계에 전달, cost가 가장 적은 방법으로 처리
  * Transaction management component
    + Transaction : 하나의 함수처럼 동작해야하는 명령어들의 집합
    + transaction에 문제가 생겼을 때 correct state를 유지하도록 만들어주는 component
    + Concurrency\-control manager : 여러 개의 transaction들이 실행되도 database에 문제가 없도록 유지해줌
<img width="400" height="400" alt="스크린샷 2022-03-02 오후 6 28 19" src="https://user-images.githubusercontent.com/59719632/156333774-2d77d943-7191-4aa8-8d29-3f4c7558266d.png">

## 1-9. Database Applications
  * Two\-tier architecture
    + 사용자가 직접 database system에 query를 날림
    + 보안에 취약
  * Three\-tier architecture
    + 사용자가 application server와 교신해서 직접적으로 query를 날리지는 않음

## 1-10. Database Users

<img width="400" height="400" alt="스크린샷 2022-03-02 오후 6 40 55" src="https://user-images.githubusercontent.com/59719632/156335988-3553cdc9-f6b3-49f4-bf4b-b455a34ec36b.png">

## 1-11. Database Administrator (DBA)
  * Schema 정의
  * database를 어디에 저장할지, 어떻게 접근할지 정의
  * Schema and physical\-organization 변경
  * data access 권한 부여
  * 주기적 백업
  * database가 커질 수록 disk 용량 부족함 없도록 업그레이드
  * 성능 모니터링


# Chap 2. Intro to Relational Model

## 2-1. Relation Schema and Instance
 * Schema는 타입, Instance는 특정 시점의 테이블 값
 * Schema는 attributes의 순서쌍
 * r(R)의 의미는 schema R을 따르는 r이라는 테이블이 있다.
 * 어떠한 테이블의 현재 값들은 테이블로 나타난다.
 * 각 행들은 순서쌍으로 나타내진다. (tuple)

## 2-2. Attributes
 * domain은 각 attribute들이 허용되는 값들의 집합
 * Attribute 값은 한 칸에 하나의 값만 적는다.
 * null 이라는 특별한 값이 있다. 모든 domain에는 null이 포함된다.

## 2-3. Relations are Unordered
 * 열 하나 하나는 순서를 지켜야 하지만 행 단위로 봤을 때는 순서 상관 없다.

## 2-4. Instance 
 * Instance는 특정 시점의 database의 snapshot이다.

## 2-5. Keys
 * superkey : 각 행을 구분할 수 있는 Column
 * candidate key(후보 키) : superkey 중 불필요한 요소가 없는 것
   - ex) 학번, 주민등록번호
 * primary key(기본 키) : 가급적이면 변하지 않는 고유의 값
 * Foreign key(외래 키) : Table이 여러 개가 있을 때 다른 table에 존재하는 key
 * Schema Diagram 

<img width="718" alt="스크린샷 2022-03-09 오전 12 12 07" src="https://user-images.githubusercontent.com/59719632/157266525-4f5d9195-b3f7-4b66-ba87-c34157505e89.png">

## 2-3. Relational Algebra
* 관계 대수는 절차적 언어이다.
* 하나 또는 두개의 relation을 input으로 받아 하나의 새로운 relation으로 반환한다.
* Select : p는 조건문, r은 table
  - 조건문에 비교 연산자 (=,!=,>,>=,<,<=) 사용 가능
  - and, or, not 으로 길게 사용할 수도 있다.

<img width="457" alt="스크린샷 2022-03-09 오전 12 16 57" src="https://user-images.githubusercontent.com/59719632/157267532-825b8653-1063-4a02-8b52-0ba69ed1069e.png">


![스크린샷 2022-03-09 오전 12 19 52](https://user-images.githubusercontent.com/59719632/157268073-52f07b93-e9bd-406b-87b9-c41a5620de8e.png)

* Project : 주어진 relation에서 특정한 attribute들만 보여줌

<img width="525" alt="스크린샷 2022-03-09 오전 12 21 27" src="https://user-images.githubusercontent.com/59719632/157268342-18b13d01-d6bb-443b-a743-1c073c458ca7.png">

* Select와 Project 연산을 중첩해서 사용할 수 있다.

<img width="324" alt="스크린샷 2022-03-09 오전 12 22 34" src="https://user-images.githubusercontent.com/59719632/157268621-572bdd66-b1ed-436b-beef-069e76a01690.png">

* Cartesian\-Product : 가능한 모든 조합의 행으로 이루어진 테이블 생성
  - table X table
  - Attribute name이 겹치면 table.attribute 식으로 renaming이 일어난다.

<img width="647" alt="스크린샷 2022-03-09 오전 12 28 30" src="https://user-images.githubusercontent.com/59719632/157269781-709c8e0d-592c-4fa2-9333-bcd6890a2c20.png">

* Join : Cartesian Product의 단점을 보완하기 위한 연산자
  - 쓸데 없는 튜플들을 제외시키기 위함
  - Cartesian\-Product 한 결과에서 Select로 의미 있는 튜플만 남긴다.
  - 나비넥타이 모양
 
<img width="665" alt="스크린샷 2022-03-09 오전 12 31 11" src="https://user-images.githubusercontent.com/59719632/157270306-cefd85cf-2138-4e5b-8d4e-778850680161.png">

<img width="634" alt="스크린샷 2022-03-09 오전 12 32 59" src="https://user-images.githubusercontent.com/59719632/157270634-a30ba716-acbf-4546-97ba-40b2387c8752.png">

* Union : 합집합
  - 두 테이블의 attribute가 같아야한다.
  - 직관적으로 똑같은 모양의 테이블
 
<img width="434" alt="스크린샷 2022-03-09 오전 12 36 23" src="https://user-images.githubusercontent.com/59719632/157271232-558711f5-1772-4c04-9542-4ea11181e6ca.png">

* Set\-Intersection  : 교집합
  - 직관적으로 똑같은 모양의 두 테이블

<img width="643" alt="스크린샷 2022-03-09 오전 12 37 37" src="https://user-images.githubusercontent.com/59719632/157271492-040ef4a3-7141-4c99-aeb8-190655543258.png">

* Set Difference : 차집합
  - 직관적으로 똑같은 모양의 두 테이블

<img width="680" alt="스크린샷 2022-03-09 오전 12 38 27" src="https://user-images.githubusercontent.com/59719632/157271635-290e1379-4788-40a7-809d-ba34eaf40c63.png">

* Assignment : 간단하게 화살표는 assignment 이다. 
  - AS와 같음
<img width="609" alt="스크린샷 2022-03-09 오전 12 39 37" src="https://user-images.githubusercontent.com/59719632/157271899-8ea4ee67-b958-4e29-88f9-03fbb2e66c52.png">

* Equivalent Queries : 같은 결과의 테이블이라도 식이 다를 수 있다.
  - The two queries are not identical(수행 절차가 다르다.); they are equivalent
 
 <p align="center">
<img width="500" alt="스크린샷 2022-03-09 오전 12 43 15" src="https://user-images.githubusercontent.com/59719632/157272573-660cf870-f863-4d3b-bcec-eccb508d70cd.png">

<img width="500" alt="스크린샷 2022-03-09 오전 12 43 21" src="https://user-images.githubusercontent.com/59719632/157272589-286791db-53a2-41d9-a95c-946660bf7d87.png">
</p>


# Chap 3. Introduction to SQL
## 3-1. SQL Parts
* Data Definition Language
  - 각 relation의 schema 정의
  - 각 column들의 data type 정의
  - 제약조건(primary key)을 걸어서 옳지 않은 데이터가 들어오는 것을 막아줌
  - Index를 만들어서 검색을 빠르게 할 수 있다.
  - 각 table에 대한 보안이나 권한
  - 어떠한 물리적 구조로 저장될지 정해줌

* Domain Types in SQL
  - char(n) : **고정된 길이**의 string, 마지막에 널문자 안 들어감
  - varchar(n) : 가변 길이 (Variable length) string, 마지막에 널문자 들어간다.
  - int, smallint
  - numeric(p,d) : p 숫자의 총 갯수 (precision), d는 소수부분(decimal)에 올 수 있는 숫자 갯수
  - real, double
  - float(n) : 최소 n개의 precision을 가지고 있는 소수

## 3-2. Create Table Construct

```mysql
CREATE TABLE instructor(
     ID char(5),
     name varchar(20),
     dept_name varchar(20),
     salary numeric(8,2)
)
```
  - 제약조건
    + primary key(A_1, ..., A_n)
    + foreign key(A_m, ..., A_n) references r : table r에 있는 column에 있는 값만 사용하게 제한
    + not null

![스크린샷 2022-03-09 오전 11 38 49](https://user-images.githubusercontent.com/59719632/157361922-469047cc-0e0d-4eb1-8e92-d45851ade83a.png)


![스크린샷 2022-03-09 오전 11 43 48](https://user-images.githubusercontent.com/59719632/157362539-56d583fe-498c-4377-b503-36bbe2da7b94.png)

## 3-3. Updates to tables
  - Insert
    + INSERT INTO instructor VALUES('10211','Smith','Biology',660000);
  - Delete (빈 테이블로 만드는 것)
    + Remove all tuples
    + DELETE FROM student
  - Drop (테이블 자체를 삭제하는 것)
    + DROP TABLE r
  - Alter (테이블 변경)
    + ALTER TABLE r ADD A D
    + D라는 Domain을 가지는 A라는 attribute를 추가하겠다. 기존에 있던 tuple들의 A에 대한 값은 null로 할당된다.

![스크린샷 2022-03-09 오전 11 58 19](https://user-images.githubusercontent.com/59719632/157382698-28c37ec1-f27d-483e-a5ee-44ae18b11150.png)


![스크린샷 2022-03-09 오전 11 58 38](https://user-images.githubusercontent.com/59719632/157382707-f5344d64-a8c1-4f20-88fe-9a4b766458da.png)

![스크린샷 2022-03-09 오후 12 01 50](https://user-images.githubusercontent.com/59719632/157382715-cc30211b-1885-4ca0-ae54-68e6abec45dc.png)

##3-4. Basic Query Structure

![스크린샷 2022-03-09 오전 11 52 05](https://user-images.githubusercontent.com/59719632/157363443-94807920-a9f5-4e7b-8c8b-de36266e48d2.png)

* SELECT Clause (Projection)
```mysql
SELECT name
FROM instructor;
```
```mysql
# 중복되지 않은 값만 SELECT
SELECT DISTINCT dept_name
FROM instructor;
```
```mysql
SELECT '437' ;# 열 이름이 '437' 이고 값이 437인 행 하나 반환
```
```mysql
SELECT 'A'
FROM instructor; # 'A'로 이루어진 행을 instructors 행 갯수만큼 반환
```

* WHERE Clause (Selection)
```mysql
SELECT name
FROM instructor
WHERE dept_name='Comp. Sci';
```
```mysql
SELECT name
FROM instructor
WHERE dept_name = 'Comp. Sci.'
AND salary > 70000;
```

```mysql
# Cartesian product
SELECT *
FROM instructor, teaches;

# 쓸데 없는 튜플들이 생긴다.
# Attribute 이름이 겹치면 이름이 바뀐다. ex) instructor.name, teaches.name
SELECT name, course_id
FROM instructor , teaches
WHERE instructor.ID = teaches.ID
AND instructor. dept_name = 'Art';
```

* Rename Operation
```mysql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = 'Comp. Sci.';
```
* Self Join
```mysql
SELECT S.supervisor
FROM emp-super AS T, emp-super AS S
WHERE T.person='Bob' AND T.supervisor=S.person;
```

* String Operations
  - \% : 모든 문자와 substring과 매칭
  - \_ : 모든 문자와 매칭
    + '___' : 정확히 3

```mysql
SELECT name
FROM instructor
WHERE name LIKE '%dar%;  # dar 앞뒤로 어떤 문자나 문자열이 와도 매칭
```












