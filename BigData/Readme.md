빅데이터언어
=========

시험 자료 정리
-----------

# Chap 1. Introduction to Python
* Interpreted Languages
  - 기계어 변환 과정 없이 바로 명령어를 실행
   
  ![스크린샷 2022-03-10 오후 2 21 13](https://user-images.githubusercontent.com/59719632/157594958-51a1d98e-c1e1-4ed2-817b-e4bb1b43fe82.png)
  
* Dynamic typing
  - 한 변수에 어떠한 타입의 객체도 다 참조할 수 있다.
  - 변수의 타입을 헷갈릴 수 있다.
* Multiple Assignment
  - x,y=2,3
* Naming Rules
  - 대소문자 구분한다. (case sensitive)
  - 숫자가 맨 앞에 올 수 없다.
  - 특수문자를 사용할 수 없다.
  - 언더바는 맨 앞에 올 수 있다.
  - reserved words(예약어)를 변수명으로 사용할 수 없다. (and, assert, break, class, continue 등)

  <img width="700" alt="스크린샷 2022-03-10 오후 3 21 25" src="https://user-images.githubusercontent.com/59719632/157601539-ca188d38-a920-4ec4-977f-a5ef81d38c53.png">


* Expression
  
![스크린샷 2022-03-10 오후 3 23 19](https://user-images.githubusercontent.com/59719632/157601787-058dcbc2-d6c5-4902-bd12-3d8c977aaa8e.png)

# Chap 2. Basic Operators and Control Statement
* CLI : 사용자 인터페이스
  - GUI (Graphical User Interface)
  - CLI (Command Line Interface)
* Input()
  - 항상 string type을 return한다.
  - ex) name=input("What is your name?")
* print()
* Type casting with input()
```python3
age = int(input("How old are you? "))
print("Your age is", age)
print(65 - age, "years to retirement")
```

* Basic Operator
  - Arithmetic Operators
    + \+
    + \-
    + \*
    + \/ : Division
    + \% : Modulus (나머지)
    + \*\* : power
    + \/\/ : Floor Division (몫)
  - Comparison Operator : True, False 값 반환
    + ==
    + !=
    + <> == !=
    + >
    + <
    + <=
    + >=
  - Other Basic Operator
    + Bitwise Operator : 많이 사용하지 않음, 이런게 있다라는 것만 알아두면 됨, &, |, ~, <<, >>
    + Logical Operator : and, or, not
    + Membership Operator : in, not in
  - 괄호를 이용해서 연산자 우선순위 원하는대로 사용 가능

* Control Statement
  ![image](https://user-images.githubusercontent.com/59719632/158604945-50150616-3c07-46ca-b424-efc8f6e457f5.png)
  
  - Sequential structure : 순차적 구조
  - Selection structure : 선택적 구조
    + if
    + if else : 둘 중 하나를 반드시 선택한다.
    + if elif else : 여러 조건 중 하나를 선택한다.
    + 조건문을 사용하게 되면 콜론과 들여쓰기를 사용해야한다.

  ```python3
  # 윤년 판단
  if (year%4==0 and year%100!=0) or year%400==0:
      print("윤년입니다.")
  else:
      print("윤년이 아닙니다.")
  ```

  ![image](https://user-images.githubusercontent.com/59719632/158605034-0f644ef8-582a-4e9c-bbba-a63a36335aee.png)
  

  - Repetition structure : 반복적 구조, while, for
    + while : 조건에 의한 반복
    + for : 횟수에 의한 반복

  ```python3
  # 최대공약수 계산하기
  x=int(input()) # 큰수
  y=int(input()) # 작은수
  
  while y!=0: # 일종의 그리디 알고리즘
    r=x%y # 나머지
    x,y=y,r
  print("최대 공약수 = " , x) # + 로 concat 하려면 str로 casting 해줘야한다.
  ```
  ```python3
  # factorial
  n=int(input())
  
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print(f'{n}! = {fact}')
  ```
  
  - break statement
  - continue statement
 
# Chap 3. Function
## 3-1. Function Definition
* 함수는 입력을 받는 reusable code 이다.
  - ex) Max / Min
  
* Random\-Number Generation
```python3
# Rolling a Six\-sided Die
import random

for roll in range(10):
  print(random.randrange(1,7),end=' ')
```

## 3-2. Defining Functions

![image](https://user-images.githubusercontent.com/59719632/159862268-f3974188-984b-4f22-98e0-32f09ccad9d3.png)

* Arguments (함수의 입력값) f(2)
* Parameters (변수) f(x)

![image](https://user-images.githubusercontent.com/59719632/159863082-24373642-5d3b-48e8-8b1c-d8600b495c5f.png)

* Return Values

![image](https://user-images.githubusercontent.com/59719632/159863418-e6600f77-d3ac-4019-8f06-50853ab42ab1.png)

* 함수 작성 시 주의할 점
  - 파이썬 인터프리터는 함수가 정의되면 함수 안의 문장들은 즉시 실행하지 않는다.
  - 함수 정의가 아닌 문장들은 즉시 실행하게 된다.

```python3
# 패스워드 생성기
import random

def genPass():
    alphabet='abcdefghijklmnopqrstuvwxyz0123456789'
    password=""
    
    for i in range(6):
        index=random.randrange(len(alphabet))
        password=password+alphabet[index]  
    return password
for i in range(3):
    print(genPass())
```

* Passing Arguments to Functions
  - Call\-by\-value
    + 함수가 argument 값의 복사본을 전달 받는다. (원본은 바뀌지 않는다.)
    + 변수를 쓸 때는 Call by value를 쓴다.
  - Call\-by\-reference
    + 함수가 argument 값을 직접적으로 전달받는다. (원본이 바뀐다.)
    + 리스트, 딕셔너리, 튜플 같은 자료구조 값들은 Call by reference를 쓴다.

  ![image](https://user-images.githubusercontent.com/59719632/159865391-c20649b0-1f12-41a1-939d-df2998b41479.png)

  ![image](https://user-images.githubusercontent.com/59719632/159865741-c040c525-4048-4ca2-ac22-0b2bf709df17.png)

* Default Parameter Values

![image](https://user-images.githubusercontent.com/59719632/159866120-8980e2d3-84b6-48c8-aa4f-e4446ed438d6.png)

* Keywrod Argument

![image](https://user-images.githubusercontent.com/59719632/159866422-89b70730-fcd8-47a3-a380-70fe413a1415.png)

* Scope Rules
  - Local Scope
  
  ![image](https://user-images.githubusercontent.com/59719632/159868973-8822e1fc-87c4-46c1-b5ac-8186b8f0cfbe.png)

  - Global Scope
    + global keyword 추가
  ![image](https://user-images.githubusercontent.com/59719632/159869326-aad6e285-ed9f-4cec-bf43-97c38f163b4a.png)

* Returning Multiple Values
  - 파이썬의 중요한 장점 중 하나
  
  ![image](https://user-images.githubusercontent.com/59719632/159870498-c306fdc1-a25c-4bd7-bbb3-a78854bf7edb.png)


# Chap 4. List and Dictionary
## 4-1. List
  - 리스트는 Ordered 객체이다
  - 리스트는 모든 타입의 객체를 담을 수 있다
  - 리스트는 하나의 이름을 공유한다
  - 리스트는 mutable이다
  - \+ 연산자 : concat
  - \* 연산자 : 반복

  ![image](https://user-images.githubusercontent.com/59719632/160813665-d8d7a913-2101-475b-ba4f-0b3bbb1d5abe.png)

  - len, in
  - append : list 끝에 추가
  - insert(index, value)
  - remove(value) : 삭제할 원소를 알 때
  - del lst[index] : 삭제할 원소의 index를 알 때
  - sort : 오름차순으로 정렬

## 4-2. 문자열
  - 문자열은 문자들의 시퀀스로 정의된다.
  - split() 으로 단어 분리
  - immutable
  
## 4-3. Tuples
  - immutable
  - Item을 추가하거나 삭제하려면 다시 선언해야한다
  - 소괄호() 사용
  
  ![image](https://user-images.githubusercontent.com/59719632/160822768-d53639df-fb8f-4d96-9d95-1404aefca0fc.png)

## 4-4. Set
* 집합은 중복되지 않은 항목들이 모인 것
* 집합의 항목 간에는 순서가 없다
* 중괄호{} 사용
* | 합집합
* & 교집합
* \- 차집합

## 4-5. Dictionary
* key, value 집합
* 순서가 없다
* key로 value 접근
* mutable
* key는 immutable 이다, hashing 구조이기 때문
* 중괄호{} 사용
* key는 집합 안에 있기 때문에 순서가 없다
  
  ![image](https://user-images.githubusercontent.com/59719632/160825428-4efaeb27-6016-4d09-b0b6-d9fd08320d6f.png)

  ![image](https://user-images.githubusercontent.com/59719632/160825474-28928107-5e3c-4891-a77d-392cfa42bfa4.png)

  ![image](https://user-images.githubusercontent.com/59719632/160825367-e550325e-5384-49c9-a793-67193a315094.png)

* keys(): 모든 key를 리스트형태로 출력
* values(): 모든 value를 리스트 형태로 출력

## 4-6. Deep Copy

![image](https://user-images.githubusercontent.com/59719632/160825914-d4c13ff5-6c39-448e-91ba-1edfe12c6c1a.png)

# Chap 5. Files and Exceptions
## 5-1. Files
* 파일의 필요성
  - 데이터를 영구히 보관하려면 파일에 저장해야 한다.
* 파일의 구조
  - 파일 안에는 바이트들이 순차적으로 저장되어 있고 끝에는 EOF (end of file) 마커가 있다. EOF는 운영체제별로 다 다름
  - 모든 파일은 입출력 동작이 발생하는 위치를 나타내는 위치 표시자 (position indicator)를 가지고 있다. 음악파일 보면 재생 위치 표현
* 파일의 종류
  - 텍스트 파일 (text file)
  - 이진 파일 (binary file)

  ![image](https://user-images.githubusercontent.com/59719632/162237225-a2ef8352-c572-40c8-8f39-b88d547b6d57.png)

* Opening Files
  - 파일을 연다
  - 파일을 처리한다
    + 읽기
    + 쓰기 (읽기 포함)
  - 파일을 닫는다, 명시적으로 close 해주는걸 지향, 파일을 열면 lock이 걸리기 때문에 close를 통해 lock을 해제해줘야 외부에서 파일 접근이 가능해진다.

  - 파일 읽기
  
  ![image](https://user-images.githubusercontent.com/59719632/162238131-d0802cd4-eb59-4f5f-8d4a-50783dd03c52.png)

  ![image](https://user-images.githubusercontent.com/59719632/162238347-c8c5a324-48d9-4474-841f-791d784da14d.png)

  ![image](https://user-images.githubusercontent.com/59719632/162239197-03cc5144-3bd3-4224-9526-f8566a064c80.png)

  ![image](https://user-images.githubusercontent.com/59719632/162240118-bd881940-b196-4167-8554-85ea65d6814f.png)

  ![image](https://user-images.githubusercontent.com/59719632/162241112-05816a88-e183-4876-96b2-2a1be984ec9e.png)

  ![image](https://user-images.githubusercontent.com/59719632/162243447-82bd6fd5-c4c3-476c-bc72-548eb18f9680.png)

  ![image](https://user-images.githubusercontent.com/59719632/162244385-c7da0c9d-569a-43ce-8f54-3fca2f627a11.png)

  - 파일 쓰기

  ![image](https://user-images.githubusercontent.com/59719632/162245310-9f17c96f-8c81-4ebb-a356-0caa4696f373.png)

  ![image](https://user-images.githubusercontent.com/59719632/162245971-660508c6-1170-44f5-824b-3eb3ed2ad7fb.png)
  
  ![image](https://user-images.githubusercontent.com/59719632/162246368-a18ae069-aa35-4ee8-bdb5-9bad1ba6a217.png)

  ![image](https://user-images.githubusercontent.com/59719632/162246749-36200f4e-9000-472a-bfa3-ea4b9d41dddc.png)

  - 파일 복사하기 : 파일 읽어서 새로운 파일에 쓰기
  
  ![image](https://user-images.githubusercontent.com/59719632/162247216-9acfaae7-ca30-47c5-9300-49f12748e5d3.png)

  - 이미지 파일 복사하기
    + 이진 파일은 데이터가 직접 저장되어 있는 파일
    + 이진 파일은 1024바이트씩 읽어서 출력 파일에 쓴다.

  ![image](https://user-images.githubusercontent.com/59719632/162247998-0378e5c9-7632-449a-b9e8-7dc86818ad2b.png)

## 5-2. Exceptions
* Exception
  - extraordinary errors
* Error Handling with Exceptions
  - Basic structure of handling exceptions
    + try : 에러가 생길 수 있는 statement
    + except : 대응 방안, except는 여러 개 쓸 수 있다.
    + else : 에러가 발생하지 않았을 때 
    + finally : 반드시 실행되는 부분

    ![image](https://user-images.githubusercontent.com/59719632/162249026-4f9a7e9a-7db6-4c04-ac0b-4748d01be02b.png)

    ![image](https://user-images.githubusercontent.com/59719632/162249460-6c114584-cbf5-42e7-900b-00ca3716b034.png)


* 예외의 종류와 예외 에러 메시지

  ![image](https://user-images.githubusercontent.com/59719632/162249719-0cabbfc1-f662-4138-8672-32e10ac5ef5d.png)

* Exception Handling: Keyboard input

![image](https://user-images.githubusercontent.com/59719632/162250151-8689c00a-48ac-476d-bcf1-d79d6adbab72.png)


* Try\-finally Block

![image](https://user-images.githubusercontent.com/59719632/162250465-5176c328-8b69-4f71-a55c-ac14b00dadc4.png)

![image](https://user-images.githubusercontent.com/59719632/162251021-158447d4-ed85-4a0c-b958-c88eb5d61171.png)


  
  
