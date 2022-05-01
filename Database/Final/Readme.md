기말고사 자료 정리
=================

# Chap 6. ER Model

## 6-1. Weak Entity Sets
* 관계를 없애는 것 대신 중복을 없애는 방법은 중복된 attribute를 지워버리는 것이다.
  - 이 때 attribute를 지워버리면 해당 entity를 구분하는데 문제가 생긴다.
* weak entity
  - 본인이 가지고 있는 attribute들로만은 식별이 불가능하고 관계를 가지고 있는 다른 entity (identifying entity)를 참조를 해야만 식별이 가능하다
  - weak entity는 identifying entity와 discriminator 라고 불리는 attribute들이 필요하다. 예시로 section의 course_id를 제외한 다른 attributes
* weak entity sets
  - 모든 weak entity는 반드시 identifying entity와 관계를 맺고 있다.
  - weak entity 집합들은 식별해주는 entity 집합에 의존하여 존재한다
  - 식별해주는 entity set은 그것이 식별하는 weak entity 집합을 가지고 있다
  - 식별해주는 개체 집합과 약한 entity 집합은 identyfying relationship을 형성하고 있다고 할 수 있다.

* Expressing Weak Entity Sets
  - weak entity set은 두 줄로 된 사각형으로 나타낸다.
  - 한줄은 strong entity set
  - discriminator들은 점선으로 나타낸다 (기본 키는 실선으로 나타냄)
  - 약한 개체 집합은 반드시 관계를 맺고 있어야 하므로 관계선도 두 줄로 되어 있다.
  - 약한 개체 집합의 식별을 도와주는 관계 또한 두 줄로 나타낸다.

  ![image](https://user-images.githubusercontent.com/59719632/166109166-8a5f981d-2c3a-4f63-8b47-60fc2d2d1e9d.png)

  ![image](https://user-images.githubusercontent.com/59719632/166110205-6ba0aa46-143f-4a5a-a3a2-556bbf76e94e.png)

  - classroom 과 time_slot entity는 section의 identifying entity가 아니다.
* Redundant Attributes
  - student 입장에서는 관계를 나타내면 dept_name attribute가 더 이상 필요 없다. => ER diagram에서 student.dept_name 없어진다.
  - 관계형 데이터베이스 모델에서 테이블로 만들 때는 지워진 attribute가 다시 살아날 수 있다.
  
## 6-2. Reduction to Relation Schemas
* weak entity set이 schema로 변환 할 때, 약한 개체집합을 식별해주는 primary key, 약한 개체 집합의 discriminator들이 모두 attribute로 들어가야한다. 

  ![image](https://user-images.githubusercontent.com/59719632/166109475-83d661f3-4dd0-49d1-a21a-646dd9d4bf97.png)

* Complex Attributes
  - Composite attributes를 다룰 때는 가장 하위 항목들만 저장한다.
  
  ![image](https://user-images.githubusercontent.com/59719632/166109555-645dcb47-a558-4777-bc76-6ed7f2a3a137.png)

  - multivalued attributes는 무시한다.

  ![image](https://user-images.githubusercontent.com/59719632/166109605-167f06a1-3e51-4a90-adf8-530baefdf71b.png)

* Multivalued Attributes
  - Multivalued attribute M, 이러한 attribute를 가지고 있는 entity E, 이 둘로 구성된 schema EM을 만들어 준다.
  - Schema EM은 E의 primary key, M으로 구성되어 있다. 
  - 여기서는 전화번호가 같을 수도 있고, 한 전화번호를 여러 명이 같이 사용할 수 있다고 생각해서 ID와 같이 구성한다.
  
  ![image](https://user-images.githubusercontent.com/59719632/166112126-01f9c185-cf90-4a34-b408-95e8c6fcaf2a.png)

* Relationship sets를 Schema로 변환
  - one to one에서는 둘 중 한 쪽 primary key
  - many to many에서는 양쪽에서 선택
  - 나머지는 many 쪽 선택
  - many to one이나 one to many에서는 many쪽에 one의 primary key를 나타내는 attribute를 추가해주면 된다.
    + 학생의 입장에서는 지도교수가 한명만 있으면 되므로 advisor 라는 attribute를 하나 추가해주면 된다.
  - many 쪽에서 반드시 관계에 참여할 필요가 없다면 null value를 허용해주어야 한다.

  ![image](https://user-images.githubusercontent.com/59719632/166109827-45bdf978-861c-4655-8ea4-926daf10e357.png)

  ![image](https://user-images.githubusercontent.com/59719632/166109950-03a9457f-b208-43eb-a50b-8430af2fffaa.png)

  ![image](https://user-images.githubusercontent.com/59719632/166109969-3beb830e-f22e-441f-9398-65148abd9341.png)

  
  - 약한 개체 집합을 schema로 변환하는 과정에는 은연 중에 식별 해주는 entity의 primary key가 schma에 들어가기 때문에 식별해주는 관계를 굳이 schema로 변환할 필요가 없다.

## 6-3. Extended E\-R Features
* Specialization
  - Top down 방식
  - 속이 빈 화살표로 표시
  - 하위 레벨 개체 집합은 상위 레벨 개체집합의 attribute를 상속 받는다.
  - instructor 개체는 person, employee의 attribute를 모두 가지고 있다.
  - 화살표가 따로 되어 있으면 화살표 별로 전문화가 가능하지만 화살표가 하나로만 되어 있으면 양쪽 중 하나만 가능
  
  ![image](https://user-images.githubusercontent.com/59719632/166111269-91034421-4b19-4d26-bfb0-6756506b5463.png)

* Specialization을 Schema로 변환
  - Method 1
    + 하위로 내려갈 수록 꼭 필요한 것들만 저장 (상위 primary key 포함)
    + 전문화가 깊게 들어간 상태라면 상위의 모든 schema의 정보를 다 얻어와야한다.
  
  ![image](https://user-images.githubusercontent.com/59719632/166111515-b4ab4c8b-6a62-4eba-b243-86ff9a15b663.png)

  - Method 2
    - local attribute와 inherited attribute 모두를 schema에 기재
    - 단점은 정보들이 중복되서 저장될 수 있다
    - 데이터 불일치 문제가 있을 수 있다
    - 디자인이 잘못 되어서 데이터 변경이 student에만 적용이 되고 person에는 적용이 안될 수 있다. 
  
  ![image](https://user-images.githubusercontent.com/59719632/166111529-fddfb1a7-bc77-4198-99e0-8f5b72f2ca3e.png)

  - Method 1 이 정보를 얻어오는데 번거롭더라도 더 나은 디자인이라고 할 수 있다.
  
* Generalization
  - Bottom up 방식
  - Specialization과 Generalization은 서로 역의 관계이고 ER Diagram에서 그림이 동일하기 때문에 엄격하게 구분하지는 않는다.
  - 상위에서 하위로 전문화 했다고 해도 되고 하위에서 상위로 일반화 했다고 표현해도 된다.

* Completeness Constraint
  - Partial이 default 이다. 반드시 전문화가 수행될 필요는 없다.
  - total 표시가 붙으면 total이고 없으면 partial이다.
  
  ![image](https://user-images.githubusercontent.com/59719632/166111778-707a7405-d0d0-475d-8e6c-9783573699ed.png)

  - total: 상위 레벨의 개체 집합이 하위 레벨 개체 집합에 속해야하는 경우
  - partial: 속하지 않고 그 상태로 머물러 있어도 됨
  
* Aggregation
  - 관계는 무조건 개체 간에 발생한다.
  








