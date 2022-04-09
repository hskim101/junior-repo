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

<img width="884" alt="스크린샷 2022-04-09 오후 2 55 37" src="https://user-images.githubusercontent.com/59719632/162558706-d15f1b0e-6304-4cfb-b50f-5335ffa641c3.png">

<img width="653" alt="스크린샷 2022-04-09 오후 2 55 44" src="https://user-images.githubusercontent.com/59719632/162558713-352b82a8-dfdf-4687-918b-a9e0833da825.png">

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

<img width="977" alt="스크린샷 2022-04-09 오후 2 57 28" src="https://user-images.githubusercontent.com/59719632/162558745-54bf4456-15cb-47b5-81f8-352896221861.png">

<img width="975" alt="스크린샷 2022-04-09 오후 2 58 37" src="https://user-images.githubusercontent.com/59719632/162558779-9f580cc9-4a70-4dee-8144-b92fcafbca68.png">

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

<img width="735" alt="스크린샷 2022-04-09 오후 2 59 24" src="https://user-images.githubusercontent.com/59719632/162558840-6b214c90-c78f-49df-9b77-84f141918aa7.png">

<img width="981" alt="스크린샷 2022-04-09 오후 3 00 02" src="https://user-images.githubusercontent.com/59719632/162558845-cc2e1c68-75a6-4f6c-9920-2473854c2905.png">

<img width="972" alt="스크린샷 2022-04-09 오후 3 00 09" src="https://user-images.githubusercontent.com/59719632/162558847-88a6a49e-c72e-487c-a2db-604c70fd6c93.png">

<img width="979" alt="스크린샷 2022-04-09 오후 3 00 14" src="https://user-images.githubusercontent.com/59719632/162558856-43c0c9f4-1c22-4522-93db-d2420e9ddd1c.png">

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

<img width="897" alt="스크린샷 2022-04-09 오후 3 01 43" src="https://user-images.githubusercontent.com/59719632/162558899-45547886-ece6-422d-ba7f-668015d95573.png">

<img width="899" alt="스크린샷 2022-04-09 오후 3 02 48" src="https://user-images.githubusercontent.com/59719632/162558911-9280873c-9ba1-4ea2-9d7e-c0f95b6438fb.png">

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

<img width="680" alt="스크린샷 2022-04-09 오후 3 03 56" src="https://user-images.githubusercontent.com/59719632/162558963-dfbd43e7-1c80-498d-8b1a-30092d20fd4f.png">

<img width="690" alt="스크린샷 2022-04-09 오후 3 04 18" src="https://user-images.githubusercontent.com/59719632/162558969-32095207-888a-48e1-98dd-d24960685655.png">

<img width="684" alt="스크린샷 2022-04-09 오후 3 04 23" src="https://user-images.githubusercontent.com/59719632/162558973-59b68a8e-553a-4de3-9ac4-d8b379778901.png">

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


# Chap 4. Intermediate SQL
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
* Outer Join
  - 정보 손실을 피하면서 join
  - inner join에서는 정보 손실이 생김
  - Three forms of outer join
    + left outer join : 왼쪽 테이블의 정보손실을 없앰
    + right outer join : 오른쪽 테이블의 정보손실을 없앰
    + full outer join : 양쪽 모두 정보 손실을 없앰
    
    ![image](https://user-images.githubusercontent.com/59719632/160062573-e7f5499f-cd74-42e5-9c47-f5f997c6f34a.png)

  - Examples
    + inner join을 하면 cs 315와 cs 347은 사라진다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160122587-d72648f4-21c1-4fb7-8de8-8ae169787ccb.png)
    
    + Outer join을 하면 정보 손실이 발생하지 않는다. natural을 사용하면 공통된 attribute는 한번만 나타난다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160123053-5ef2eb2e-3245-4023-93d3-3039ac46cb12.png)


    ![image](https://user-images.githubusercontent.com/59719632/160123009-c5b7ce3c-75ae-462f-9629-1934d8866ce2.png)

    + Full outer join
    
    ![image](https://user-images.githubusercontent.com/59719632/160123650-c8649f44-d11e-4170-a5ae-264a3227124c.png)
    
    ![image](https://user-images.githubusercontent.com/59719632/160123267-ce4792e0-9fae-4923-890d-62934adca9c6.png)
   
    ![image](https://user-images.githubusercontent.com/59719632/160123393-952c1119-0bff-4717-a64a-c365c5c023b1.png)


    + sqlite는 left outer만 구현했다. 테이블의 순서를 바꿔서 right를 left로 표현할 수 있다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160123550-a07c67eb-5ecc-4220-95aa-4abe089910a0.png)

* Joined Types and Conditions

  ![image](https://user-images.githubusercontent.com/59719632/160123896-088c6f28-011f-440d-a1d7-c8a15309f6a0.png)

  - using
    + using 안에는 어떤 attribute 를 사용해서 join을 하겠다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160217379-f208a94c-ebe3-4db7-9dfe-dffef0c39180.png)


  - on
    + 조건이 만족되면 inner join
    + natural과 수행하는 것은 비슷하지만 natural은 중복되는 열을 한번만 쓰지만 on은 중복되게 표시한다.

    ![image](https://user-images.githubusercontent.com/59719632/160217094-28d6165b-7187-4f7f-a7f0-d24ee5e6d5f1.png)

    + 조건식에 서로 다른 attribute를 비교하면 뒤에 나오는 attribute에 대한 정보가 자세하게 표현이 된다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160217142-9d1ab7ed-5eee-4612-9697-03ad5beaef04.png)

    ![image](https://user-images.githubusercontent.com/59719632/160217195-a2addc25-c777-4020-800a-8f491dddec0e.png)
    
* Views
  - 모든 사용자들에게 모든 데이터베이스 정보를 보여줄 필요가 없다.
  - Virutual Relation (가상 테이블)
  - 뷰는 새로운 테이블을 만들어서 disk에 저장하는 것이 아니다.
  - 프로그래밍에서 inline function과 비슷
  - 뷰를 정의할 때 뷰를 써도 된다 => 테이블 처럼 사용해도 된다. 
  - 실체화된 뷰를 사용할 수도 있지만 이 경우 원본 테이블이 변하면 뷰도 업데이트 시켜줘야한다. 
  - 실체화를 시키지 않고 뷰를 사용하면 뷰는 자동으로 업데이트 된다.
  
  ![image](https://user-images.githubusercontent.com/59719632/160217475-392f8ff5-e310-4f19-801d-4ab7ebc5a1ed.png)

  ![image](https://user-images.githubusercontent.com/59719632/160217550-09043eea-68ec-4f68-98a3-1ac42bdb982d.png)

  ![image](https://user-images.githubusercontent.com/59719632/160218592-db35b563-907f-4142-8fd8-cbd0e872a745.png)

  - 뷰를 업데이트할 때 삽입하려는 tuple에 모든 attribute에 대한 값이 순서쌍으로 있어야한다. 없는 경우 null로 채워야함
  
  - 두 개의 relation에 기반한 뷰를 만들 때 이 뷰에 tuple을 삽입할 때 어떤 attribute에 해당하는 값인지 모름
   
    ![image](https://user-images.githubusercontent.com/59719632/160756324-9d11e9e1-a3c3-49be-a3c7-3d37afffb005.png)

  - 뷰에 직접 업데이트는 굉장히 제한적인 상황에서만 허용한다.
  - 뷰 조건에 해당하지 않는 튜플을 insert한 경우 뷰에서 그 튜플을 볼 수 없다.

    ![image](https://user-images.githubusercontent.com/59719632/160767397-98cdc864-e5a3-448f-8556-f74adbae60b2.png)

  - 대부분의 SQL은 오직 simple views 만 업데이트를 허용한다.
    + FROM 절에 relation이 하나만 있어야함
    + SELECT 절에 오직 original column만 사용 가능 (distinct 같은 거 사용하면 안됨)
    + SELECT 절에서 등장하지 않은 attribute들은 null로 값이 세팅될 수 있어야 한다.
    + Query는 group by나 having이 없어야한다. (집계함수를 못 쓰기 때문)
* Transactions
  - 여러 작업을 하나의 작업으로 여겨지게하는 작업
  - Transaction은 반드시 두 명령 중 하나로 끝나야한다.
    + Commit work: transaction의 시작부터 끝날 때까지 수행된 모든 쿼리를 데이터베이스에 영구적으로 업데이트함
    + Rollback work: transaction의 시작부터 끝날 때까지 수행된 모든 쿼리를 취소함
* Integrity Constraints
  - 데이터베이스에 어떠한 잘못된 값이 들어와서 데이터베이스를 망가뜨리는 일을 방지하는 역할
  - 하나의 Relation 제약 조건에 넣을 수 있는 제약
    + not null
    + primary key
    + unique: attribute들에 대해서 똑같은 튜플이 존재하지 않는다.
    + check (P): 조건 p에 부합하는지 체크
  - 두 개의 Relation 제약 조건에 넣을 수 있는 제약
    + foreign key
    + cascade: 참조 무결성 제한 조건이 깨지는 것을 허용하고, 제한 조건이 깨지는 튜플들에 대해서도 명령이 실행

    ![image](https://user-images.githubusercontent.com/59719632/160782179-01075788-252d-4d96-bb29-c32b2493c49f.png)

* Complex check contidion (시험에 안나옴)
  - check문 괄호 안에 쿼리가 들어가 있음

  ![image](https://user-images.githubusercontent.com/59719632/160783224-8b3de894-42a6-463e-b43c-028e6ab12abf.png)

  - Assertions (시험에 안나옴)
    
* Built\-in Data Types in SQL
  ![image](https://user-images.githubusercontent.com/59719632/160783602-00867ed4-6bb8-41f4-ba4a-e619205b14f6.png)

  - interval : 시간에서 시간을 빼줌
  
* Large\-Object Types
  - blob: binary large object, binary로 저장된 파일
  - clob: character large object, 굉장히 긴 text 문서
  - 쿼리가 large object를 return할 때 데이터를 전부 넘겨주는 것이 아닌 pointer를 넘겨준다.

* Domains, User\-Defined Types (시험에 안나옴)
* Index Creation
  - 특정 데이터를 빠르게 찾아오기 위해 존재함
  - 쿼리에서 요청이 있을 때, 테이블 전체를 스캔해서 찾으면 너무 비효율적임
  - 처음 만들 때 index를 생성해서 사용해야하고, 데이터가 업데이트되면 index를 업데이트 해줘야한다.
  
  ![image](https://user-images.githubusercontent.com/59719632/160788149-a4daf652-34f0-4498-b91e-cbb755ef6a6a.png)
  
  ![image](https://user-images.githubusercontent.com/59719632/160788429-e3c8997c-f08e-462a-9db5-926801aab0a9.png)

* Authorization
  - Read: 읽기는 가능하지만 수정할 수는 없다
  - Insert: 새로운 데이터를 삽입하지만 이미 있는 데이터를 수정할 수는 없다
  - Update: 수정이 가능하지만 삭제는 못 한다
  - Delete: 삭제를 할 수 있다
  - 이러한 권한을 privilege라고 한다.
  - 어떤 테이블, 뷰에 대해서 이러한 권한을 부여할 수 있다
  - SQL에서 권한을 설정하는 방법
    + GRANT 명령어
    + GRANT \<privilege list> on \<relation or view> to \<user list>
    + user list에 public을 사용하면 권한을 부여할 수 있는 모든 user
    + GRANT SELECT ON department TO Amit, Satoshi
  - 권한을 뺏을 때는 GRANT 대신 REVOKKE 사용, 형식은 grant 와 동일

* Roles
  - 그룹을 만들어 줌
  ![image](https://user-images.githubusercontent.com/59719632/160789915-1a165ad2-d9e2-4aa4-93a9-bf78a62f330a.png)

* 뷰에 대한 권한 (강의 다시 봐야함)

# Chap 5. Advanced SQL
## 5-1. Accessing SQL from a programming language
* SQL의 표현력에 한계가 있다.
* SQL을 통한 입출력이 힘들다.
* 일반적인 프로그래밍 언어에서 SQL을 사용하는 방법
  - Embedded SQL
    + 컴파일 할 때 SQL 명령어가 번역된다.
    + 런타임이 되면 이미 번역된 function을 API를 사용해서 SQL 명령을 실행된다.
  - Dynamic SQL
    + 대부분의 쿼리를 string 형태로 저장
    + 컴파일 타임에는 어떠한 쿼리가 실행되는지 확인하지 않는다
    
## 5-2. JDBC (API)
* JDBC는 Java API 이다.
* 데이터의 수정을 할 수 있다
* JDBC 사용
  - connection을 open
  - Create a "statement" object
  - 쿼리를 실행하고, 쿼리를 데이터베이스에 보내고 받아오는 작업
  - 에러 exception mechanism

  ![image](https://user-images.githubusercontent.com/59719632/160839967-ad414288-6d41-4de1-bf36-a112b0b472c5.png)

  ![image](https://user-images.githubusercontent.com/59719632/160841351-5fa1449d-644a-4dd0-92d7-b235205b1aca.png)

  - 처음에 ResultSet은 첫번째 item 바로 직전을 가리키고 있음
  - while 문을 통해 한 줄 한 줄 읽어올 수 있다.  
  
  ![image](https://user-images.githubusercontent.com/59719632/162113242-59053464-46ea-4f63-958a-ce60fef0e12a.png)

* JDBC Code Details
  - getInt를 통해 값이 0이 나왔을 경우 0인지 null 인지 판단할수 없기 때문에 wasNull() 함수로 null 인지 확인해준다.
* Prepared Statement
  - 특수문자 같은 것이 포함된 문자열
  - 백슬래시가 알아서 삽입됨
  
  ![image](https://user-images.githubusercontent.com/59719632/162114262-4ce3feb7-5ae5-48ed-bdb9-fdf6a71cddab.png)

* SQL Injection
  - 원래 의도했던 것은 name을 입력하는 것인데 2번째 줄 같은 값이 들어와버리면 항상 참이되서 의도 하지 않은 결과가 나타나버린다.
  - Prepared statements를 사용하면 항상 프로그래머가 의도했던 대로만 결과가 나타나게 할 수 있다.
  - sql 문을 입력해도 sql문이 string 형태로 입력된다. 문자열 그대로 받아들인다.

  ![image](https://user-images.githubusercontent.com/59719632/162114840-f92b6fc0-7b6c-463d-b919-053edcec9fc0.png)

* Metadata Features
  - ResultSet metadata
  - 각 열의 이름과 타입을 알 수 있다.
  - 코드를 재활용하기 유연해진다.
  - getTables 함수를 사용하면 Table에 대한 Metadata를 얻어올 수 있다.

  ![image](https://user-images.githubusercontent.com/59719632/162117664-47db3ec8-0d33-4445-8058-bb4e69ce7a80.png)

  ![image](https://user-images.githubusercontent.com/59719632/162117612-d7140952-be56-40a8-9037-f4d96a56e91a.png)


* Transaction Control in JDBC
  - 한문장 한문장을 Transaction 취급하면 안되고 setAutoCommit을 false로 turn off 시켜줘야 한다.
  - 각 문장이 쭉 쌓이고 모든 작업을 다 했을 때 commit (적용) 또는 rollback (삭제)을 해준다
  
* Other feature (넘어감)

## 5-3. ODBC (Open DataBase Connectivity) , Microsoft (수업에서 자세하게 다루지 않음)
* Embedded SQL 
 
  ![image](https://user-images.githubusercontent.com/59719632/162123140-95b11497-4f9b-461a-bc22-fbb088edfe77.png)

  ![image](https://user-images.githubusercontent.com/59719632/162123260-0bf1a703-d1ce-493d-bae1-6eadab5b06d1.png)

  -SQLSTATE가 '02000'이 되면 더 이상 fetch 해 올 튜플이 없다는 것을 의미하므로 쿼리를 close 해야한다.

  ![image](https://user-images.githubusercontent.com/59719632/162123830-2db47d1c-c2fb-42db-9ba9-34db1a77dbbc.png)
 
* Updates Through Embedded SQL (넘어감), Database와 host language에 따라 다르기 때문에

## 5-4. Functions and Procedures
* Functions and Procedures
  - Functions는 값을 return하지만 Procedures는 값을 return하지 않는다.
* Declaring SQL Functions (DB마다 구조가 다르기 때문에 구문을 이해할수 있을 정도만 되면 된다.)
   
![image](https://user-images.githubusercontent.com/59719632/162124627-8ee5a665-ef92-43b0-9d9c-12c9a86df113.png)

* Table Functions

![image](https://user-images.githubusercontent.com/59719632/162124965-9ab04480-fd3f-4d63-b71e-6ee6de930fbb.png)

* Procedures (강의 자료에 없기 때문에 생략)

* Language Constructs (for문 사용할 수 있다 정도만, ppt에 문제 있어서 넘김)
* External Language Routines
  - SQL 말고도 다른 언어로 작성된 Function이나 procedure를 호출 할 수 있구나 정도만

* Security with External Language Routines
  - 메모리를 공유하면 overheads가 발생함

## 5-5. Triggers
* Trigger
  - Database에 변경 사항이 생겼을 때 자동으로 실행되는 명령
  - Trigger를 사용하려면 trigger가 실행되는 조건을 명시해야함, 어떠한 동작을 할 것인가도 명시해야함
  - 각 시스템별로 작성하는 방법이 다름

* Trigger to Maintain credits_earned value
  - Trigger를 만드는데 언제 작동하는지 예제
  - 새로운 행 nrow, 이전 행 orow
  - atomic : 하나의 명령어 처럼 행동해야된다. = transaction
  - 성적이 변경 되었을 때 update 부분이 모두 실행되어야 실행, 아니면 rollback
  
