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
    + '_ _ _' : 정확히 3개의 문자
    + '_ _ _ %' : 3개의 문자 뒤에 어떠한 문자열 (최소 3개의 문자열이 있어야한다.)

```mysql
SELECT name
FROM instructor
WHERE name LIKE '%dar%;  # dar 앞뒤로 어떤 문자나 문자열이 와도 매칭
```

* Ordering the Display of Tuples
```mysql
SELECT DISTINCT name
FROM instructor
ORDER BY name ASC;
```

* WHERE Clause
```mysql
SELECT name, course_id
FROM instructor, teaches
WHERE (instructor.ID, dept_name) = (teaches.ID, 'Biology'); # 튜플로 한번에 비교해도 된다.
```

* Set Operations
  - 기본적으로 중복되지 않은 값들로만 이루어져 있다.
  - 중복된 값 포함시키려면 all을 붙이면 된다. (UNION ALL)
  
```mysql
(SELECT course_id FROM section WHERE sem = 'Fall' AND year = 2017)
UNION
(SELECT course_id FROM section WHERE sem = 'Spring' AND year = 2018); # 합집합

# 교집합 : INTERSECT
# 차집합 : EXCEPT
```

* Null Values
  - 5 + null = null
  - null 인지 확인하려면 IS NULL 또는 IS NOT NULL 을 써야한다. True or False로 반환
 - 5<null, null<>null, null=null 다 unknown으로 나오고 unknown은 false로 판단한다.
```mysql
SELECT name
FROM instructor
WHERE salary IS NULL; # salary=null 이렇게 쓰면 안된다.
```

![sql퀴즈](https://user-images.githubusercontent.com/59719632/158791036-8b44a270-5ecb-4fa9-98a4-0c56a2fdc46a.PNG)

![sql2](https://user-images.githubusercontent.com/59719632/158791060-910d2e4e-938b-4768-8c9d-bfa73ee9311d.PNG)

![sql3](https://user-images.githubusercontent.com/59719632/158791069-17711dca-897b-4daf-94f7-0fb659cd80d9.PNG)

* Aggregate Functions
  - avg
  - min
  - max
  - sum
  - count

  ```mysql
  SELECT AVG(salary)
  FROM instructor
  WHERE dept_name= 'Comp. Sci.';
  ```

  ```mysql
  SELECT COUNT(distinct ID)
  FROM teaches
  WHERE semester = 'Spring' AND year = 2018;
  ```

  - Group By
    + 집계 함수를 사용할 때 SELECT 부분에서 집계 함수가 쓰이지 않은 Attributes는 모두 GROUP BY 항목에 들어가 있어야한다.
  ```mysql
  # 집계를 할 때 어떤 그룹 단위로 집계를 할지 정함
  SELECT dept_name, AVG(salary) AS avt_salary
  FROM instructor
  GROUP BY dept_name; # ID가 없으므로 에러
  ```

  - Having Clause
    + where와 having의 차이는 having은 집계함수를 먼저 실행한 후 조건을 적용한다.
    + where는 집계함수 이전에 적용이 된다.
    + where와 having은 다르다.
  ```mysql
  SELECT dept_name, AVG(salary) AS avg_salary
  FROM instructor
  GROUP BY dept_name
  HAVING AVG(salary) > 42000;
  ```

 - 다음의 두 질의문 모두 dept_name: 학과 이름과 avg_salary: 평균 연봉을 출력합니다.
 ```mysql
 SELECT dept_name, AVG(salary)
 FROM instructor
 GROUP BY dept_name
 HAVING AVG(salary) > 42000
 ```
 
 - HAVING은 GROUP BY 이후에 실행되므로 학과별 평균 연봉을 구한 후 평균 연봉이 42000보다 큰 학과 이름과 평균 연봉을 출력합니다.
 
 ```mysql
 SELECT dept_name, avg(salary)
 FROM instructor
 WHERE salary > 42000
 GROUP BY dept_name
 ```

 - WHERE는 GROUP BY로 평균을 내기 전에 실행하므로 연봉이 42000보다 큰 교원들만 추려낸 후 학과별 평균을 구해 학과 이름과 평균 연봉을 출력합니다.

* Nested Subqueries
```mysql
SELECT A1, A2, ..., An
FROM r1, r2, ..., rm
WHERE P;
```

* Set Membership
```mysql
SELECT DISTINCT course_id
FROM section
WHERE semester = 'Fall' AND year= 2017 AND
      course_id IN (SELECT course_id
                    FROM section
                    WHERE semester = 'Spring' AND year= 2018);
```

```mysql
SELECT DISTINCT name
FROM instructor
WHERE name NOT IN ('Mozart', 'Einstein') # 튜플 형태로 명시

SELECT COUNT(distinct ID)
FROM takes
WHERE (course_id, sec_id, semester, year) IN # 여러개의 membership을 튜플 형태로 걸러낼 수 있다.
                   (SELECT course_id, sec_id, semester, year
                    FROM teaches
                    WHERE teaches.ID= 10101);
```

* Set Comparison
  - SOME Clause
    + =some = in
    + !=some != not in
  ```mysql
  # 하나하나 비교
  SELECT DISTINCT T.name
  FROM instructor AS T, instructor AS S
  WHERE T.salary > S.salary AND S.dept name = 'Biology';
  
  # 한 사람과 전체 비교, 그 다음사람과 전체 비교
  SELECT name
  FROM instructor
  WHERE salary > SOME(SELECT salary # salary > some => 가장 낮은 값보다 크면 참
                      FROM instructor
                      WHERE dept_name='Biology');
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/159105051-766c4be3-c02a-4d66-b96a-de78887397bb.png)

  - ALL Clause
    + !=all = not in
    + =all != in
  ```mysql
  # 가장 큰 값과 비교
  SELECt name
  FROM instructor
  WHERE salary > ALL(SELECT salary
                     FROM instructor
                     WHERE dept name = 'Biology');
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/159105117-bfe85075-888e-495a-9120-6d03d5b7380b.png)

* EXISTS Clause
  - 공집합이 아닌 경우만 만족
  - exists => 공집합인 아닌 경우
  - not exists => 공집합인 경우
```mysql
# Find all students who have taken all courses offered in the Biology department.
# 문제에 all이 있다고 위의 all과 같다고 생각하며 안된다.
SELECt course_id
FROM section AS S
WHERE semester = 'Fall' AND year = 2017 AND
      EXISTS (SELECT *
              FROM section AS T
              WHERE semester = 'Spring' ANd year= 2018
                    ANd S.course_id = T.course_id);
```

* UNIQUE
  - subquery에 만족하는 값이 최대 하나의 값만 있는 경우만 만족
  - 중복이 있는지 없는지만 체크, subquery 조건에 아에 해당하지 않는 경우도 만족
  
```mysql
SELECT T.course_id
FROM course AS T
WHERE UNIQUE (SELECT R.course_id
              FROM section AS R
              WHERE T.course_id= R.course_id
                    AND R.year = 2017);
```
  
![dsafasdfasdf](https://user-images.githubusercontent.com/59719632/159105683-e3bc3083-f638-47a1-bb66-4edafb3b0c42.PNG)

![2](https://user-images.githubusercontent.com/59719632/159105688-f0e21c0e-556c-430b-bf99-6a4f31c5ec0b.PNG)

![3](https://user-images.githubusercontent.com/59719632/159105691-ead5f250-d836-4b28-a09f-fc42d33e84f5.PNG)

* Subqueries in the Form Clause
```mysql
SELECT dept_name, avg_salary
FROM (SELECT dept_name, AVG(salary) AS avg_salary
      FROM insturctor
      GROUP BY dept_name)
WHERE avg_salary > 42000;      
```

```mysql
# subqueriy의 결과를 AS로 rename해줌

SELECT dept_name, avg_salary
FROM (SELECT dept_name, AVG(salary)
      FROM instructor
      GROUP BY dept_name)
      AS dept_avg(dept_name, avg_salary)
WHERE avg_salary > 42000;
```
* With Clause
  - with 절은 쿼리에서 사용될 임시 relation을 만들어준다.
  - 주어진 Table로부터 바로 정보를 추출하기 힘든 경우 중간 단계의 table을 만들어서 계산을 할 수 있게 도와주는 역할
```mysql
WITH max_budget(value) AS
     (SELECT MAX(budget)
      FROM department)
SELECT department_name
FROM department, max_budget
WHERE department.budget = max_budget.value;
```      

* Complex Queries using With Clause
```mysql

WITH dept_total(dept_name, value) AS
     (SELECT dept_name, SUM(salary)
      FROM insturctor
      GROUP BY dept_name),
dept_total_avg(value) AS
    (SELECT AVG(value)
     FROM dept_total)
SELECT dept_name
FROM dept_total, dept_total_avg
WHERE dept_total.value > dept_total_avg.value;
```

* Scalar Subquery
  - Select 문에서 쓸 수 있는 Scalar subquery
  - Table 형태가 아닌 하나의 값으로 결과가 나옴
  - 1 tuple보다 많은 결과가 나오면 Runtime Error가 발생한다.
```mysql
SELECT dept_name,
       (SELECT COUNT(*)
        FROM insturctor
        WHERE department.dept_name = instructor.dept_name)
      AS num_insturctors
FROM department
```

* Modification ofr the Database
  - Deletion
  ```mysql
  # Where 안쓰면 instructor table 삭제
  DELETE FROM insturctor
  WHERE dept_name='Finance';
  ```

  ```mysql
  # Problem : tuple이 삭제될 때마다 평균값이 달라진다.
  # Solution : 평균을 구한 후 평균보다 낮은 tuple들을 체크한다음에 avg를 다시 구하지 않고 한번에 삭제
  DELETE FROM insturctor
  WHERE salary < (SELECT AVG(salary)
                  FROM instructor);
  ```

  - Insertion
    + Attribute에 대한 정보를 안쓰면 values에 모든 값들을 다 넣어야한다.
    + 원하는 열만 값을 넣고 싶으면 원하는 열만 쓰면 된다. 나머지 열의 값은 null로 채워진다.
  ![image](https://user-images.githubusercontent.com/59719632/159903391-a01f8d5f-53f8-458d-8f0b-c7520dcfd58a.png)

  ![image](https://user-images.githubusercontent.com/59719632/159904102-51d8c431-69a8-4308-8f7a-54b3596fc4f6.png)

 
  - Updates
    + 값을 수정
    + update set
    + update를 연속으로 할 때는 순서가 중요하다.
    + case statement를 쓰면 더 좋다.
    
    ![image](https://user-images.githubusercontent.com/59719632/159915177-b018598a-f174-4e9a-aadf-fc2915ffaf81.png)

    ![image](https://user-images.githubusercontent.com/59719632/159915391-b0255805-39bc-449b-b244-8dae2311745d.png)

  - Updates with Scalar Subqueries
  
   ![image](https://user-images.githubusercontent.com/59719632/159915952-78b29ce7-ec40-4183-a9d9-eb235427b968.png)


## Chap 4. Intermediate SQL
* Join Operation
  - Cartesian Product
    + 가능한 모든 경우의 수를 출력
    + 엉뚱한 조합까지 다 이어 붙이는 단점이 있다.
  - Join은 가능한 모든 조합을 구한 후 조건식에 만족하는 경우만 뽑아낸다.
  - 콤마(Cartesian) 대신 NATURAL JOIN 사용
  ![image](https://user-images.githubusercontent.com/59719632/159916947-a74b5685-c3a0-4d8e-bda5-0786c1cf34e9.png)

  ```mysql
  # ID가 같은 것 끼리 조합
  # Natural join은 공통된 attribute가 일치하는 경우만 이어 붙인다.
  SELECT *
  FROM instructor NATURAL JOIN teaches; 
  ```
  - 앞에 2개 table에서 natural join된 결과 table과 뒤 table과 순차적으로 natural join
  
  ![image](https://user-images.githubusercontent.com/59719632/159918016-e9ea2250-f506-4faa-b2fb-9edb85a8bfb4.png)

  - Natural Join의 위험성
    ![image](https://user-images.githubusercontent.com/59719632/159919017-bb8a8f2b-d893-4b3f-a626-9dd4128f93e7.png)

  - 공통인 부분이 일치하는 경우만 natural join => natural inner join
  - natural은 자연스럽게 공통인 attribute만 사용해라
  - inner는 공통인 attribute가 매칭될 때만 사용해라





