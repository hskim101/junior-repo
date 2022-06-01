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
  - Composite attributes를 schema로 변환할 때는 가장 하위 항목들만 저장한다.
  
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
  - 관계가 중복되어 저장될 때 
  - Aggregation된 집합을 하나의 개체로 판단
  
  ![image](https://user-images.githubusercontent.com/59719632/166180846-ca5d2bc3-68f3-4251-9efc-bb5806fe7219.png)

  ![image](https://user-images.githubusercontent.com/59719632/166180855-d2d641b8-0380-410a-b72c-89c7f9d4bd18.png)


  - 어떠한 관계를 추상적인 개체로 취급
  - 관계와 관계가 관계를 허용하도록 함
  - Schema로 변환하면 Aggregation을 한 것과 하지 않은 것에 차이가 없다.
  - 다른 개체 집합의 primary key가 필요하다 (위에서는 evaluation의 key)
  
  ![image](https://user-images.githubusercontent.com/59719632/166181013-e8d91d74-d6af-453e-af7e-713edd0627e0.png)

  - 보기 편하고 나중에 제약조건 넣기 편하기 때문에 사용한다.

* Design Issues
  - E\-R diagram에서는 관계를 형성하는 개체의 attribute 넣을 필요가 없다. 넣으면 중복 발생
  
  ![image](https://user-images.githubusercontent.com/59719632/166181173-d950f60b-f580-4255-83df-26f7136e326e.png)

  - Multivalued attribute가 필요한데 single valued를 사용하는 경우
    + 아래 그림에서 b가 single valued를 사용한 경우, d가 알맞게 수정한 경우이다.
    + c는 weak entity를 이용해서 수정한 경우
    + assignment 각각에 대해서 어떠한 정보를 저장할 때에는 c 방법이 더 선호된다.
  ![image](https://user-images.githubusercontent.com/59719632/166181230-a9869abf-f2be-482d-9de7-7c71c94be7f5.png)

* 관계 집합을 별도의 Entity set으로 만들지 말지 선택

  ![image](https://user-images.githubusercontent.com/59719632/167309897-12dc46f1-a30c-4e9c-9469-cbd48598b243.png)

  - 관계 집합을 Entity로 만들었다는 것은 many to many에서 관계 선 하나하나가 개체가 되었다는 의미
    + 무조건 연결되어 있어야한다.
  - 일반적인 가이드라인은 entity들 사이에 어떠한 action이 있다 하면 관계 집합으로 만들어라

* non binary를 binary로 바꾸는법은 자세히 알 필요 없다

* 표기법은 각자 익히기

# Chap 7. Normalization
## 7-1. First normal form (시험에는 안나오는데 자격증 시험에는 나옴, 퀴즈에는 나올 수 있음)
* 값이 atomic하기만 하면 된다.

## 7-2. Second normal form (시험에는 안나오는데 자격증 시험에는 나옴, 퀴즈에는 나올 수 있음)
* atomic
* 후보키의 일부만 가지고 다른 항목들이 결정되어서는 안된다.


## 7-3. Decomposite
* 정보가 중복되는 문제가 있는데 이를 해결하기 위해 큰 테이블을 두 개의 schema로 나누는 것이다.
  - 테이블을 나누었다가 다시 합칠 때 원래 테이블로 복구를 하지 못하면 정보 손실이 발생한다. (정보가 잃어버리지는 않더라도 쓸데 없는 정보가 추가되었을 때도 정보 손실이라고 본다. 정확한 정보를 얻기 어려워졌을 경우)

* 정보 손실 없이 Decomposition하는 방법
  - 원래 테이블과 정확하게 일치하는 테이블이 나오면 lossless decomposition이라고 한다. 
  - 원본보다 튜플들이 더 많아지면 decomposition이 lossy 하다.
  
  ![image](https://user-images.githubusercontent.com/59719632/167068545-7673ae09-16bd-4a73-b2f2-c33a0b24402e.png)

  ![image](https://user-images.githubusercontent.com/59719632/167068805-fa190764-c588-4f70-8b82-f6251b5ad72b.png)


## 7-4. Functional Dependencies

* Functional Dependencies

  ![image](https://user-images.githubusercontent.com/59719632/167245327-66ba6da8-23ef-494f-9a45-866030dafc2f.png)

  ![image](https://user-images.githubusercontent.com/59719632/167245341-8cd2660a-ce4f-4e23-b7e8-4074ffaa5a8f.png)

  - 한 attribute 값을 알 때 다른 attribute 값을 알 수 있는 경우
  - 현실 세계의 여러가지 constraints를 만족하는 instance를 legal instance라고 한다.
  - 어떠한 기본 키가 주어졌을 때 해당 키로 모든 것을 구분할 수 있다.
  
  ![image](https://user-images.githubusercontent.com/59719632/167245448-1613d281-23b7-4624-be80-db9ca0f3923e.png)

* Closure
  - 다른 functional dependencies를 통해 유추할 수 있는 것
   
  ![image](https://user-images.githubusercontent.com/59719632/167245542-6229f952-7272-43d3-aa1c-6f58eeb082cf.png)

* Key와 functional dependencies
  - 슈퍼 키가 동일하면 해당하는 relation 아래 있는 모든 attribution 값이 같다
  - 슈퍼 키의 일부만 가지고 모든 튜플을 구분지을 수 있으면 해당 집합은 후보 키가 될 수 없다.
  - 예시에서는 ID,name이 슈퍼키 집합인데 ID 만으로 모든 튜플을 구분할 수 있기 때문에 ID,name 은 후보 키는 될 수 없지만 ID는 후보키가 될 수 있다.
  
  ![image](https://user-images.githubusercontent.com/59719632/167245671-7b80176a-be2c-4aea-8fb4-20fb7aedcf56.png)

* Use
  - 함수적 종속성이 없는데 함수적 종속성이 있는 것 처럼 보일 때가 있다.
  - 예를 들면 name \-> ID
  
* Lossless Decomposition
  - 겹치는 attribute인 B가 R1을 결정 짓거나 R2를 결정지으면 된다. (둘 중에 하나만 만족하면 무손실 분해가 성립)
  
  ![image](https://user-images.githubusercontent.com/59719632/167245818-f693d699-4377-4fd1-934b-4ca7c892d759.png)

  - B \-> B 성립, B \-> BC => B \-> B , B \-> C
  
  ![image](https://user-images.githubusercontent.com/59719632/167245926-a2c51cc5-14ed-4f1e-82bf-0ab1e0e39139.png)

  ![image](https://user-images.githubusercontent.com/59719632/167246045-333687ad-f6c5-4781-a75d-444209e6c36f.png)

* Dependency Preservation
  - natural join 은 비용이 큰 연산이다.
  - 여러 테이블을 합쳐서 dependency를 만족하는지 판단해야하는 경우 비용이 크기 때문에 dependency가 보존된다고 하지 않는다.
  - 

  ![image](https://user-images.githubusercontent.com/59719632/168395282-b132d331-bdf0-4ece-948d-dad69312f482.png)

* Boyce\-Codd Normal Form (BCNF)
  - 제 3정규형보다 조건은 간단하지만 더 엄격하다
  - 모든 함수적 종속성에 대해서 2가지 중 하나를 만족해야한다.
    
    ![image](https://user-images.githubusercontent.com/59719632/168395476-0e44b28b-df18-4295-86e1-c5f94c736e60.png)

    - trivial 하려면 좌변이 우변보다 더 큰 집합이면 된다. => 우변이 좌변의 부분집합
    - 좌변이 superkey 이면 된다.
  - 슈퍼키가 아닌데 다른 것을 결정짓는다면 정보가 중복되었다는 뜻이다 => 분해를 시켜 버린다. => 함수의 종속성이 깨진다. => 정보 중복 문제는 해결된다.
  - BCNF라고 해서 무조건 함수적 종속성이 깨지는 것이 아니고 깨질 가능성이 있다는 것이다.
  
  ![image](https://user-images.githubusercontent.com/59719632/168396807-c6fe6da8-433f-4237-b92a-c2a15eb425fc.png)

* Third Noraml Form
  - BCNF 조건 OR 베타에만 있는 attribute들이 후보키에 속해있다. 각 attribute는 서로 다른 후보 키에 속해 있을 수 있다.
  - 각각이 어떠한 후보 키에만 속해 있으면 된다. (하나의 후보키에 속해있을 필요 없음)
  
  ![image](https://user-images.githubusercontent.com/59719632/168482944-ad891adb-b8db-4f5d-9956-79967a32710e.png)
  
  - 위에서 dept_name은 BCNF는 만족하지 않지만 제3정규형은 만족한다. 분해했을 때 한쪽의 후보 키에 속해 있기 때문이다.
  - BCNF 이면 제3정규형이다. 제3정규형이면 무조건 BCNF인 것은 아니다.
  
* Redundancy in 3NF
  - 함수적 종속성을 만족하기 위해 테이블을 분해하지 않으면 정보 중복되어 저장된다.
  - null value를 써야한다.

* Comparison of BCNF and 3NF
  - 제3정규형의 장점: decomposition을 했을 때 정보손실 이나 dependency preservation을 깨지 않고도 제3정규형을 만족시킬 수 있다.
  - BCNF는 위의 내용을 허용하지 않음
  - 제3정규형의 단점: null value를 써야하는 경우가 생김, 어느 교원이 어느 학과에 속해있는지 계속 반복적으로 나타내줘야하는 단점이 있다.
  - 둘 다 loseless decomposition이 되지만, 제3정규형은 정보 중복 문제가 발생할 수 있고, BCNF는 dependency가 보존되지 않을 수 있다.
  
* Goals of Normalization
  - relation이 좋은 형태인지 판별해주는 것이 정규화이다.
  - schema가 좋은 형태가 아니면 그 schema를 여러 개의 schema로 나누고 각각의 schema에 대해 다시 좋은 형태인지 검샇나다.
  - 좋은 형태, 무손실 분해 (lossless decomposition), 가급적이면 dependency가 보존되어야한다. (마지막은 필수 조건은 아님, BCNF는 dependency를 깨버린다)
  
* How good is BCNF?
  - BCNF는 모든 함수적 종속성에 대해 trivial 인지, a \-> b로 갈 때 a가 슈퍼 키인지 검사
  - 함수적 종속성이 아에 존재하지 않는 경우 BCNF가 된다. => 모든 함수적 종속성이 만족된다고 봄, 좋은 table이 아닐 수 있다.
  - 이 문제를 해결하기 위해 제 4 정규형이 등장한다.

* Functional\-Dependency Theory Roadmap (수업에서 생략)

* Design Goals
  - BCNF이면 좋다
  - Lossless이면 좋다
  - Dependency가 보존되면 좋다
  - 위 내용을 만족하지 못하는 경우, dependency 보존이 안된 상태로 BCNF로 가던가, 정보 중복이 발생해도 3NF로 가던가한다.
  - 슈퍼 키 이외에 함수적 종속성을 직접적으로 표현할 수 있는 방법이 없다.
  - assertion을 활용할 수있지만 test 비용이 비싸다.
  - SQL 입장에서는 함수적 종속성을 test하는 것이 만만치 않다.
  - 이론적으로 함수적 종속성이 중요하지만, 이것이 깨지더라도 BCNF가는게 좋지만 나중에 생길 문제가 확실히 보이면 BCNF보다 3NF로 가는게 편할 수 있다.
  
* Multivalued Dependencied (MVDs)
  - 함수적 종속성에서는 하나의 값만 결정 지었는데 여기서는 여러 개의 값을 결정지을 수 있다.
  - ID\->\->child_name
    + 모든 조합에 대해서 튜플들이 모두 있는지 확인하는 과정
    + a\->\->b 에서 b가 t1에 있으면 b가 아닌 attribute는 t1이 아닌 t2에 있어야한다.
  - ID가 정해졌을 때 child_name이 유일하게 정해지는 것 => 함수적 종속성
  - 화살표 두 개 : 모든 조합에 대해 튜플들이 생김, ID가 child_name을 여러 개 가지고 있다 라는 의미

  ![image](https://user-images.githubusercontent.com/59719632/168484321-92dae435-9f0e-4223-9bbc-74f37371d5cf.png)

  - 가능한 조합 중 일부 튜플이 없을 때, 화살표 두 개 종속성이 없어진다.
  - a가 b를 다중결정하게 되면 a는 R-b-a를 다중결정하기도 한다.
    + a\->\->b => a\->\->R-b-a 이다.
    
  - t1, t2를 어떻게 잡던간에 이로인해 생성되는 t3, t4가 무조건 존재해야한다.
  - 직관적으로 Multivalued attribute들이 있을 때 가능한 모든 조합의 튜플들이 존재하면 Multivalued Dependency가 만족된다.
  
  ![image](https://user-images.githubusercontent.com/59719632/169448224-d0f6374f-dfed-4f2d-8e43-7bccc0c66c12.png)

  - a\->\->b => a\->\->R-b-a 이다.
  
  ![image](https://user-images.githubusercontent.com/59719632/169449331-00eef7c9-9baf-43bd-b949-f26b2f13f1f7.png)

* Use of Multivalued Dependencies
  - relation을 test 하기 위함
  - 제약조건을 명시한다.
  - relation이 MVDs를 만족하지 않았을 경우, 튜플들을 추가함으로써 MVDs를 만족하게 할 수 있다.

* Theory of MVDs
  - If a → b, then a →→ b
  - Closure
    + Closure를 구할 때는 간단한 경우는 추론할 수 있지만, 복잡한 경우 기계적으로 추론법칙을 통해 구한다(이 부분은 자세히 다루지 않음)

  ![image](https://user-images.githubusercontent.com/59719632/169449798-fde8bfbe-3553-4b30-958c-4ae5727b8ac8.png)


* Fourth Normal Form
  - a \->\-> b 가 trivial (a union b = R) => R-a-b = 공집합
  - a가 schema R의 superkey
  
* Further Normal Forms (넘어감)

* Overall Database Design Process
  - R이 E\-R diagram을 통해 만들어진 table 일 수도 있고
  - 필요로하는 attribute를 모두 담고 있는 하나의 table이 될 수도 있다
  - R을 작게 쪼개는 과정이 들어감
  - ad hoc design을 쓸 수도 있다. 
  
* ER Model and Normalization
  - ER diagram을 정말 잘 사용했다면 Normalization이 필요 없을 수 있다.
  - 현실세계에서는 정규화과정이 필요할 수 있다. 정규화를 통해 별도의 table로 만들어주는 것이 좋다.

* Denomalization for Performance
  - 시간적 효율성을 위해 table을 합쳐 놓는 것
    + 빠르게 찾을 수 있다
    + Update 할 때 시간이 많이 걸린다
    + 프로그래머가 관리하기 힘들어서 버그가 생길 수 있다.
  - use materialized view (실체화된 view)
    + 빠르게 찾을 수 있다
    + Update 할 때 시간이 많이 걸린다
    + 프로그래머가 감당해야되는 에러에 대한 걱정은 없다.
  
* Other Design Issues
  - 연도 마다 tabel을 따로 만들면 좋지 않은 design이다.
  - column이 따로 있는 경우도 좋지 않은 design 이다.

* Modeling Temporal Data
  - 시간과 관련된 Data
  - snapshot을 찍어서 특정 시점의 값을 기재한다.
  - But no accepted standard
  - 제약조건을 넣을 수 있지만 강제하기 힘들다.
  - 외래키 참조를 현재 시점을 참조할지, 특정 시점을 참조할지 정할 수 있다.
  
# Chap 8. ComplexDataTypes

## 8-1. Semi\- Structured Data
* 상황에 따라 schema를 유동적으로 바꿔가면서 보여줄 필요가 있음
* 특징
  - Flexible schema
    + Wide Column: 많은 종류의 값을 넣을 수 있고 언제든지 새로운 attribute를 추가할 수 있다.
    + Sparse Column: 많은 attribute가 있지만 선택되는 것은 아주 적은 수 이다.
  - Multivalued Data Types
    + Sets, multisets
    + Key\-value map
    + Arrays
  
    ![image](https://user-images.githubusercontent.com/59719632/169708061-2526132b-3766-4cd0-adeb-d47a32cffdb8.png)

## 8.2 Nested Data Types
  - JSON: Text file
    + key\-value 형식으로 되어 있다.
    + 많은 웹에서 사용되고 있다.
    + 일반적인 JSON 형태는 사람이 읽을 수 있도록 되어 있어서 기계적으로는 굉장히 비효율적이다. 바이너리 형태로 압축하면 용량이 줄어든다.
    
    ![image](https://user-images.githubusercontent.com/59719632/169708172-bfae5517-07ec-47c2-b73b-4a25cdf29897.png)

  - XML: tag를 사용하는 mark up language이다.
    + JSON과 마찬가지로 사람이 쉽게 읽고 쓸 수 있다.
    
    ![image](https://user-images.githubusercontent.com/59719632/169708215-2e6eb34f-ea28-43d9-bc07-f0c69d172238.png)

* Knowledge Representation
  - RDF: Resource Description Format (시험에 안나옴)

## 8.3 Object Orientation (깊게 다루지 않음)
* 객체지향형 프로그래밍을 사용하는 언어에서 사용하는 Type들이 관계형 데이터베이스의 Type 들과 매칭이 안된다.
* 객체지향형 관계형 데이터베이스를 만들어서 객체지향언어를 받아들이도록 추가해준다.
* Object\-Relational Mapping: 기본적인 data 형식으로 다 변환을 해준다.
 
## 8-4. Textual Data (넘어감)

## 8-5. Spatial Data (지도)
* Geographic data
  - Geographic information systems (GIS) : 지리적 정보를 담고 있는 시스템
* Geometric data: 위도 경도
* Representation of Geometric Constructs : 삼각형으로 분할하는 것이 중요하다. (시험에 안나옴)

# Chap 9. Application Development
## 9.1 Application Programs and User Interfaces
* 응용프로그램이 사용자와 데이터베이스를 연결해주는 역할을 한다.
* Front\-end : user interfaces
* Backend: 데이터베이스 시스템과 직접 교신하는 역할
* Web Interface
  - 웹브라우저를 통해 수많은 유저들이 어디서든 데이터베이스에 접근 가능
  - 불필요한 다운로드, 설치를 피한다.
* Three\-Layer Web Architecture
  - web server: 사용자의 요청을 받고 요청을 전달해줌
  - application server: 주로 코딩이 일어나는 곳
  - database server: mysql, oracle 등
  - Two Layer를 많이 사용함
    
  ![image](https://user-images.githubusercontent.com/59719632/169708777-3e54c84f-bf6a-4ea6-8bf8-e37d0c38e075.png)

* HTTP and Sessions
  - 웹문서를 볼 때 인터넷을 끊어도 계속 볼 수 있다 => HTTP가 connectionless 이기 때문
  - 서버에 부하를 줄이기 위함
  - 각 사용자의 session 정보가 필요할 때 문제가 된다. => solution : cookie
* Sessions and Cookies
  - Cookie는 식별 정보를 담고 있는 작은 Text 조각이다.
  - 사용자는 쿠키를 가지고 있다가 서버에 정보를 요청할 때 쿠키를 보낸다.
  - 쿠키는 영구적으로 저장할 수도 있고, 일정 기간동안 저장할 수도 있다.
  
## 9.2 Sevelets
* Servlets: 자바로 웹 페이지의 문서를 동적으로 만드는 것
  - 누가 접속을 하든지 간에 똑같은 화면을 나타내는 경우 그냥 웹문서로 작성하면 된다.
  - 사용자로부터 정보를 받아서 사용자에게 특화된 웹 페이지를 보여주고자 하면 Servlet을 사용하면 된다.

## 9.3 Server\-Side Scripting
* Server \- Side Scripting
  - HTML 문서 안에 script가 들어가 있는 형태
  - Javascript: 자바랑 상관 없음
  - Cross Site Scripting: 보안에 취약하다
    

# Chap 15. Query Processing (join)
* Basic Steps in Query Processing
  - Parsing and translation
    + Parser가 query를 번역해서 관계 대수 표현식으로 번역해줌
    + 수식 실행 전에 optimizer가 있어서 효율적으로 실행하게 분석한 후 execution plan을 만듦
    + evaluation engine이 결과를 사용자에게 보내줌
    + 똑같은 쿼리라고 하더라도 실행 할 수 있는 방법이 다를 수 있다.
  - Query Optimization: Cost가 낮은 plan을 선택한다. 정확히 알 수 는 없고 추정을 할 수 있다.

* Measures of Query Cost
  - response time: 추정하기 힘들다
  - CPU cost는 무시한다. (복잡한 연산은 안하기 때문), 실제로는 고려해야한다.
  - 똑같은 결과가 나오기 때문에 같은 결과를 디스크에 저장하는 cost는 어차피 똑같기 때문에 무시한다.
  - Disk Cost
  
  ![image](https://user-images.githubusercontent.com/59719632/170696951-91a327da-ba8d-45de-977b-3f7bac9acf43.png)

  - 버퍼에서 읽어올 경우 디스크의 입출력을 하지 않기 때문에 추정한 cost와 다를 수 있다. (고려하기 힘들다)
  - 디스크마다 버퍼가 다르기 때문에 Worst case 추정을 하지 않을 수도 있다.
  - 버퍼가 있을 경우 버퍼에 의해 상당한 성능 향상이 있다고 생각하면 Average Case로 분석을 해도 된다.
 
* Selection Operation
  - File Scan
  - Linear Search
    + Cost estimate = 1 seek (원하는 테이블이 저장되어있는 곳으로 가기 위한) \+ 연속된 b_r 개의 블록을 읽음 transfer
    + key attribute로 selection을 하는 경우: b_r/2 block tranfers \+ 1 seek, 평균 b_r/2개 
    + selection 조건, 순서, 인덱스의 유무 => 상관 없다
  - binary search: 데이터들이 정렬된 상태라고 보장할 수 없기 때문에 적용할 수 없고 적용할 수 있더라도 이동할 때 seek를 계속 해줘야하기 때문에 적용하지 않는다.
    + block tranfer 시간보다 seek 시간이 수십배 많이 걸리기 때문
  
* Sorting (자세히 다루지 않음)
  - index를 이용해서 sorting을 수행: seek time
  - 퀵소트나 다른 정렬 알고리즘 사용하면 되는데 tabel이 너무 크면 external merge sort를 사용하면 된다.
  
  ![image](https://user-images.githubusercontent.com/59719632/171415478-5ae6fb0c-eeec-4f7e-9574-b9db7c6c31a9.png)

* Join Operation
  - join을 수행하는 여러가지 알고리즘
    + Nested\-loop join : for loop을 2번 돔 => 1번 테이블에서 1번, 2번 테이블에서 1번 => 비용이 비싸다, 모든 조합에 대해 다 살펴봄
      - worst case: 메모리에 한 블록만 올릴 수 있다고 가정한 경우, n_r \* b_s \+ b_r \+ seek time(n_r + b_r)
      - b_r=100, b_s=400, n_r=5000, n_s=10000
      - 바깥의 loop를 어떤걸 선택하냐에 따라 비용이 달라짐
      - 작은 테이블이 메모리에 완벽하게 들어가는 경우, 작은 테이블을 inner loop에 넣어라
      
      ![image](https://user-images.githubusercontent.com/59719632/171417488-45666b31-8753-41ce-8bca-2fae60d8fe0b.png)
      
      ![image](https://user-images.githubusercontent.com/59719632/171417723-8c71b2b9-4004-480c-a1d5-8107b5c5b300.png)

      ![image](https://user-images.githubusercontent.com/59719632/171416758-9edbb7b7-f8e2-4adb-9f83-78cfb824bf8a.png)
    
      - Block 단위로 nested loop : 한 블록에 대해 full scan 하는 장점이 있다. full scan 횟수가 줄어든다. => 모든 block pair에 대해 join할지 말지 살펴봄
      
      ![image](https://user-images.githubusercontent.com/59719632/171420326-a3509543-9a7f-444f-be09-350fe8dd270c.png)


    + Block nested\-loop join : 
    + Indexed nested\-loop join
    + Merge\-join
    + Hash\-join
 
 


