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
 
  
  
