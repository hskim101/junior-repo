응용소프트웨어실습
==============

# C# Basic
## 닷넷 (.NET)
* .NET Framwork
  - 베이스 클래스 라이브러리 (Base Class Library, BCL)
    + .NET Framework를 사용하는 모든 프로그래밍 언어가 사용할 수 있는 라이브러리
    + 파일 입출력, 그래픽 렌더링, 데이터베이스 조작 등의 공통된 기능을 해주는 클래스들을 제공함
  - 공통 언어 기반 (Common Language Infrastructure)
    + **.NET Framework의 가장 중요한 요소**
    + 공통 언어 런타임 (Common Language Runtime, CLR)이라고 부르기도 함
    + 다음의 주요 요소로 구성되어 있음
      - 공통 타입 시스템 (Common Type System, CTS)
      - 공통 언어 스펙 (Common Language Spec, CLS)
      - 저스트 인 타임 컴파일러 (Just\-In\-Time, JIT)
      - 가상 실행 시스템 (Virtual Execution System, VES)

## C\#
* 특징
  - 객체 지향
    + 네임스페이스
    + 클래스
  - 언어 간 상호 운용성
    + .NET 기반의 다른 프로그래밍 언어로 개발된 컴포넌트들과 호환이 가능
  - 적용 분야의 다양성
    + 콘솔 애플리케이션
    + GUI 애플리케이션
    + 웹 애플리케이션
    + ...
  - 가비지 콜렉션
  - 멀티스레딩 지원
  - 비동기 처리 지원

![스크린샷 2022-03-14 오후 2 34 49](https://user-images.githubusercontent.com/59719632/158111215-d4ede109-ed05-4a9a-9c01-2307c26a9bfd.png)

* 클래스 도움말
  - https://docs.microsoft.com/ko-kr/

## C\# 프로그래밍
* C\# 코드의 구조

  ![스크린샷 2022-03-14 오후 2 38 00](https://user-images.githubusercontent.com/59719632/158111531-f8fdccf2-e74d-4601-bc8f-71f20e792b81.png)
  
  - 클래스
    + 하나의 C\# 코드 파일 내에 하나 이상의 클래스가 존재할 수 있음
    + partial 키워드를 사용하여 하나의 클래스를 여러 개의 코드 파일에 걸쳐 정의할 수 있음
    
  ```c#
  class 클래스명{
    /* 멤버 변수와 메소드 등 */
  }
  ```
  - Main() 함수
    + 프로그램의 시작점이 되는 함수
    + public static void로 선언해야 함
    + main()이 아닌 Main()임을 반드시 확인
  - Prolog
    + using Statements와 namespace 부분을 포함
    + namespace
      - 하나 이상의 클래스를 그룹화 한 단위를 namespace라고 함
    + 다른 namespace의 클래스에 접근하고자 하면, using을 사용하여 해당 namespace에 접근함
    + Console.WriteLine()은 System namespace를 using System으로 접근함으로써 사용 가능함 (System.Console)

* 에러
  - 구문 에러 (Syntax error)
    + 기본 문법에 대한 규칙을 위반
  - 런타임 에러 (Runtime error)
    + 프로그램을 실행하는 도중에 발생
  - 로직 에러 (Logic error)
    + 실행 결과가 의도한 결과가 아닌 잘못된 결과가 나온 경우

* 디버그 (Debug)
  - 프로그램의 다양한 오류를 찾고, 이를 수정하는 것
  - 구문 오류는 Visual Studio 내의 코드 편집기에서 확인할 수 있음
  - 런타임 오류는 Visual Studio 내의 코드 편집기에서 확인할 수 있음
  - 로직 오류는 개발자 스스로 원인을 찾고 해결해야함
    + Visual Studio 내의 디버그 기능을 활용하면 변수의 현재 값, 함수의 반환 값 등을 확인할 수 있음

* 명명 규칙 (Naming Rule)
  - 변수, 함수, 객체 등의 명명 조건과 규칙
    + 반드시 영문자 또는 밑줄(_)로 시작해야 함
    + 영문자, 숫자, 밑줄을 포함할 수 있음
    + 공백() 또는 구두점(.)은 포함할 수 없음
    + 예약어는 사용할 수 없음
  - 보편적인 명명 규칙
    + **CamelCase** : 주로 사용
    + Snake_Case
    + Hungarian
      - bFlag
      - iNum
  - MS coding conventions https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions
  
  <img width="700" alt="스크린샷 2022-03-14 오후 2 49 22" src="https://user-images.githubusercontent.com/59719632/158112677-9d313741-09ae-49d2-9ea9-aec3f64aee33.png">


  <img width="700" alt="스크린샷 2022-03-14 오후 2 50 07" src="https://user-images.githubusercontent.com/59719632/158112763-8c4932a3-f76e-4276-9fb9-1b6a3bc5f7dc.png">
  
* 자료형 (Data Type)
  - System이라는 namespace에 정의되어 있음
  - System.object에서 파생된 System.Type을 상속함

  <img width="900" alt="스크린샷 2022-03-14 오후 2 52 16" src="https://user-images.githubusercontent.com/59719632/158112982-14b25091-58af-47a7-917f-e59ca2fbd427.png">
  
  
  <img width="900" alt="스크린샷 2022-03-14 오후 2 53 07" src="https://user-images.githubusercontent.com/59719632/158113091-74661e39-cd4d-4401-a10d-3f07619ccd69.png">  

```c#
using System;

namespace Example1 {
    class Program{
        static void Main(string[] args){
            char chVar1 = 'A';
            char chVar2 = '\x0041'; // 16진수
            char chVar3 = (char)65; 
            char chVar4 = '\u0041'; // 유니코드
            
            Console.WriteLine("문자 표현: {0}", chVar1); // python의 format과 비슷
            Console.WriteLine("16진수 표현: {0}", chVar2); 
            Console.WriteLine("ASCII 표현: {0}", chVar3); 
            Console.WriteLine("Unicode 표현: {0}", chVar4);
        } 
    }
}
```

<img width="154" alt="스크린샷 2022-03-14 오후 2 55 23" src="https://user-images.githubusercontent.com/59719632/158113327-84911845-b64d-4820-9f07-e55e42c38013.png">

```c#
using System;

namespace Example2{
    class Program{
        static void Main(string[] args){
            string strText1 = " Hello ";
            string strText2 = " C# ";
            string strText3 = " World! ";
            string strText4 = strText1 + strText2 + strText3; // concat
            
            Console.WriteLine("전체 문자열: {0}", strText4);
            Console.WriteLine("전체 문자열의 길이: {0}", strText4.Length); 
            Console.WriteLine("문자열 시작과 끝의 공백 제거: {0}", strText4.Trim()); // .Trim()으로 공백 제거
            Console.WriteLine("C# 제거: {0}", strText4.Remove(8, 2)); // 인덱스로 접근해서 원하는 문자열 제거, 인덱스 8부터 2개 삭제
            Console.WriteLine("Hello를 안녕으로 변경: {0}", strText4.Replace("Hello", "안녕")); // 문자열 대체
            Console.WriteLine("모두 대문자로 변경: {0}", strText4.ToUpper()); 
            Console.WriteLine("모두 소문자로 변경: {0}", strText4.ToLower());
        } 
    }
}
```
 <img width="291" alt="스크린샷 2022-03-14 오후 3 00 18" src="https://user-images.githubusercontent.com/59719632/158113882-cdba3e85-6f09-4d4d-86f7-56a553dc8987.png">

* 변수 (Variable)
  - 변수
    + 데이터의 저장에 관련된 것
    + 데이터를 읽거나 쓰는 것이 가능하고, 참조만 하는 것도 가능
  - 변수의 선언 방법
    + [modifiers] datatype indentifier;

  <img width="200" alt="스크린샷 2022-03-14 오후 3 02 03" src="https://user-images.githubusercontent.com/59719632/158114071-b4b3fe29-cb60-4fe5-91a5-23ee8884b3af.png">
  
  - 변수의 기본값

  <img width="700" alt="스크린샷 2022-03-14 오후 3 03 10" src="https://user-images.githubusercontent.com/59719632/158114195-b2230c6a-de63-43e5-9bb8-ae57cbbfb6c8.png">

* 연산자 (Operator)
  - 산술 연산자
    + 계산식을 처리하는 연산자

  <img width="700" alt="스크린샷 2022-03-14 오후 3 08 30" src="https://user-images.githubusercontent.com/59719632/158114715-9bbe0d1b-5398-4b25-822e-42f7b3552587.png">
  
  - 증가, 감소 연산자
  
  <img width="700" alt="스크린샷 2022-03-14 오후 3 09 15" src="https://user-images.githubusercontent.com/59719632/158114850-c2c10885-2935-4119-a827-c0348e6c5cfc.png">

  - 배정 연산자
  
  <img width="700" alt="스크린샷 2022-03-14 오후 3 09 28" src="https://user-images.githubusercontent.com/59719632/158114861-f0bd0897-8939-4676-87c2-3bc9366c2d3c.png">

  - 논리 연산자
    + &, | 와 &&, || 가 조금 다름
  
  <img width="700" alt="스크린샷 2022-03-14 오후 3 10 44" src="https://user-images.githubusercontent.com/59719632/158114940-82cc1db6-02e9-442a-a9d5-bf0e6d2ab727.png">
  
  - 비교 연산자

  <img width="700" alt="스크린샷 2022-03-14 오후 3 12 16" src="https://user-images.githubusercontent.com/59719632/158115099-84713436-d24e-4144-a32b-9d7b892d2f91.png">
  
* 연산자의 우선순위
  - 연산자가 동등한 우선순위에 있는 경우
    + 대입 연산자는 오른쪽에서 왼쪽으로 연산 순서를 갖음
    + 대입 연산자를 제외한 모든 연산자는 왼쪽에서 오른쪽으로 연산 순서를 갖음
    + 산술 연산자는 대수학(algebra)의 규칙을 따름
  - 연산자가 낮은 우선순위에 있는 경우
    + 우선순위가 낮은 연산자를 먼저 처리하기 위해서는, ()를 사용해야함

```c#
using System;
namespace Example5 {
    class Program{
        static void Main(string[] args){
            int iNum1 = 3;
            int iNum2 = 3;
            Console.WriteLine("전위 연산자");
            Console.WriteLine("iNum1 = {0}, iNum2 = {1}", iNum1, iNum2); 
            Console.WriteLine("++iNum1 = {0}, --iNum2 = {1}", ++iNum1, --iNum2); 
            Console.WriteLine("iNum1 = {0}, iNum2 = {1}", iNum1, iNum2);
            
            iNum1 = 3;
            iNum2 = 3;
            Console.WriteLine("\n");
            Console.WriteLine("후위 연산자");
            Console.WriteLine("iNum1 = {0}, iNum2 = {1}", iNum1, iNum2); 
            Console.WriteLine("iNum1++ = {0}, iNum2-- = {1}", iNum1++, iNum2--); 
            Console.WriteLine("iNum1 = {0}, iNum2 = {1}", iNum1, iNum2);
        } 
    }
}
```

<img width="185" alt="스크린샷 2022-03-14 오후 3 16 59" src="https://user-images.githubusercontent.com/59719632/158115670-20dd7668-3706-4032-9556-68250ac74a2c.png">

* 표준 입출력

```c#
using System;
namespace Example6 {
    class Program{
        static void Main(string[] args){
            string strName;
            
            Console.Write("<< 이름을 입력하세요: ");
            strName = Console.ReadLine(); // 입력 함수
            Console.WriteLine(">> {0} 님, 안녕하세요!", strName); // writeline은 \n까지 포함해서 자동으로 개행함
        } 
    }
}
```

* 사용자 정의 클래스, 배열, 연산자 예시

```c#
using System;
namespace Example7 {
    public class Student{
        private int mINumber;
        private int mIScore;
        
        public Student(int iNumber, int iScore) {
            mINumber = iNumber;
            mIScore = iScore;
        }
        public int getNumber(){ 
            return mINumber; 
        }
        public int getScore(){ 
            return mIScore;
        }
    }
    
    class Program{
        static void Main(string[] args) {
            const int NUM_STUDENTS = 5;
            Array arrStudents = Array.CreateInstance(typeof(Student), NUM_STUDENTS);
            int iScoreSum = 0;
            double dScoreMean = 0.0;
            Console.WriteLine("<< {0} 명의 학생의 점수를 입력하세요.", NUM_STUDENTS); 
            for (int i = 0; i < NUM_STUDENTS; i++){
                    int iNumber = i + 1;
                    string strScore = Console.ReadLine();
                    int iScore = Convert.ToInt32(strScore);
                    Student student = new Student(iNumber, iScore);
                    arrStudents.SetValue(student, i);
            }
            for (int i = 0; i < arrStudents.Length; i++){
                int iNumber = ((Student)arrStudents.GetValue(i)).getNumber(); 
                int iScore = ((Student)arrStudents.GetValue(i)).getScore();

                string strGrade = "F";
                if (iScore >= 90) { 
                    strGrade = "A"; 
                }
                else if (iScore >= 80) { 
                    strGrade = "B"; 
                } 
                else if (iScore >= 70) { 
                    strGrade = "C"; 
                } 
                else if (iScore >= 60) { 
                    strGrade = "D"; 
                }
                Console.WriteLine(">> {0} 번 학생의 점수: {1}, 등급: {2}", iNumber, iScore, strGrade);
                iScoreSum += iScore;
            }
            dScoreMean = (double)iScoreSum / NUM_STUDENTS;
            Console.WriteLine("평균 점수: {0}", dScoreMean); 
        }
    } 
}
```

<img width="284" alt="스크린샷 2022-03-14 오후 3 29 40" src="https://user-images.githubusercontent.com/59719632/158117114-afc22092-db57-467f-a0d8-b29fe4c2cd7e.png">

## C\#프로그래밍 2

* 반복문
  - foreach
    + 배열이나 collection 객체를 위한 반복문
    + 파이썬 for와 유사
    + for 보다 연산속도가 느리다.
    + for 사용을 더 지향한다.
    
    ![image](https://user-images.githubusercontent.com/59719632/159192220-e286a68e-502f-48c8-82cf-d1505c59f401.png)
    
    ```c#
    using System;
    using System.Collections;
    namespace Example1
    {
        class Program
        {
            static void Main(string[] args)
            {
                ArrayList myAL = new ArrayList(); // 배열 객체 생성
                myAL.Add("Hello"); // 배열에 문자열 append
                myAL.Add("World");
                myAL.Add("!");
                Console.Write("Values : ");
                PrintValues(myAL);
            }
            public static void PrintValues(ArrayList myList)
            {
                foreach(string text in myList)
                {
                    Console.Write("\t{0}", text);
                }
                Console.WriteLine();
            }
        }
    }
    ```
    
    ![image](https://user-images.githubusercontent.com/59719632/159192421-8af6b60b-504a-4e61-8498-dde6286844fc.png)

* 예외 및 예외처리
  - 예외: 프로그램 실행 중 발생하는 오류
    + 컴파일 오류 (Compile error): 오타, 문법에 맞지 않는 코드로 인한 오류
    + 실행 중 오류 (Run\-Time error): 디버깅 모드를 통해 해결, 프로그램의 비정상적인 동작
    + 로직 에러
  - 예외 처리
    + try, catch, throw, finally 키워드를 규칙에 따라 조합하여 사용
    + try와 catch는 반드시 함께 사용
    + try: 예외가 발생할 가능성이 있는 코드의 영역을 지정, 예외를 감시하는 부분
    + catch: try에서 발생한 예외나 throw 명령으로 전달한 예외를 처리
    + throw: 예외를 저낟ㄹ하는 키워드
    + finally: 예외 발생과 상관없이 실행하는 부분
    
    
    ```c#
    using System;
    namespace NullError
    {
        class Program
        {
            static void Main(string[] args)
            {
                String str = null;
                try
                {
                Console.WriteLine(str.ToString());
                Console.WriteLine("Program Terminated");
                }
                catch(NullReferenceException e)
                {
                    Console.WriteLine(e.ToString());
                }
            }
        }
    }
    ```
  - 다중 catch: try 부분에서 하나 이상의 예외가 발생하는 경우 여러 개의 catch를 이용하여 예외를 처리함
  - 다중 catch 규칙:
    + 각각의 catch는 반드시 서로 다른 종류의 예외를 처리함
    + 상속관계에 있는 여러 예외객체를 처리하는 경우 세부적인 예외 처리부를 앞에 두고 일반적인 객체를 나중에 처리함
  ```c#
  using System;
  
  namespace Example3
  {
    class Program
    {
      static void Main(string[] args)
      {
        int[] arr1={1,11,22,33};
        int[] arr2={0,1,2};
        for(int i=0; i<arr1.Length;i++)
        {
          try{
            Console.WriteLine(arr1[i]+"/"+arr2[i]+"="+arr1[i]/arr2[i]);
          } catch(DivideByZeroException e){
            Console.WriteLine("Can't divide");
          } catch(Exception e){
            Console.WriteLine(e.Message);
          }
        }
      }
    }
  }
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/159192866-efcb1c15-82f7-4ed0-8b72-bd02bb2a97df.png)

  - try ~ catch ~ finally
    + try 블록에서 예외가 발생한 코드의 다음 코드부터는 실행하지 않음
    + finally: 예외 발생 여부에 관계없이 실행할 코드를 입력, finally 부분은 생략할 수 있음
    
* 배열
  - 배열
    + 형식이 같은 변수들의 집합
    + 인덱스를 통해 접근
  - C\#에서 배열 선언 시 주의사항
    + 배열 크기를 지정할 수 없음 == 정적 배열을 사용할 수 없음
  - 다차원배열
    + 2차원 이상의 배열을 의미
    + 정사각형이 아닌 가변 배열을 생성할 수 있음  (Jagged Array)
    
  ![image](https://user-images.githubusercontent.com/59719632/159193047-b023c232-016c-4a39-ba1d-4145172120cc.png)

  ![image](https://user-images.githubusercontent.com/59719632/159193073-dcdfe174-2fc3-4809-89b4-065608ddbc6a.png)

  - 배열의 주요 메소드 및 속성
  
  ![image](https://user-images.githubusercontent.com/59719632/159193134-01fe4009-3ec7-4188-ba98-197f68d2bbbb.png)

  ```c#
  using System;

  namespace Example4 {
      class Program {
          static void Main(string[] args) {
              int[] arr1 = new int[5] { 3, 5, 7, 4, 1 };
              int[] arr2 = (int[])arr1.Clone();
              foreach (int item in arr2) {
                  Console.WriteLine("{0}", item);
              }
          }
      }
  }
  ```
  
  ```c#
  using System;

  namespace Example5 {
      class Program {
          static void Main(string[] args) {
              int[] arr1 = new int[5] { 3, 5, 7, 4, 1 };
              int[] arr2 = new int[5] { 9, 3, 6, 5, 2 };
              int[] arr3 = new int[10];

              arr1.CopyTo(arr3, 0);
              arr2.CopyTo(arr3, 5);

              foreach (int item in arr3) {
                  Console.Write("{0} ", item);
              }
          }
      }
  }
  ```
  
  ```c#
  using System;

  namespace Example6 {
      class Program {
          static void Main(string[] args) {
              int[,] arr1 = new int[2, 5] { { 3, 5, 7, 4, 1 }, { 4, 5, 7, 8, 9 } };

              Console.WriteLine("{0}", arr1.GetLength(0));
              Console.WriteLine("{0}", arr1.GetLength(1));
              Console.WriteLine("{0}", arr1.Length);
              Console.WriteLine("{0}" + "차원", arr1.Rank);
          }
      }
  }
  ```
* Class
  - 객체 지향 프로그래밍의 핵심
  - 객체의 변수와 메소드 등을 정의하는 일종의 틀
  - 클래스 멤버
    + 멤버의 순서는 의믜가 없지만 같은 종류 별로 모으는 것이 관리하기 쉬움
    + 같은 이름의 멤버 여러 개를 사용할 수 없음
    + 멤버의 종류
      - 필드 (Field): 클래스의 멤버 변수, staic redonly const 등 사용
      - 메소드 (Method): 일련의 문장을 포함하는 코드 블록
      - 상수 (Constant): 값을 바꿀 수 없는 정적 필드, const, readonly(초기화 필요없음, 초기값 한 번 입력 가능)
      - 생성자 (Constructor): 클래스의 인스턴스를 초기화 하는 함수
     
  ![image](https://user-images.githubusercontent.com/59719632/159194463-127a8aa0-8451-4995-8af4-32754b6d4cb9.png)

  - this 키워드
    + 객체 자신을 참조하는 변수
    + 복잡한 코드에서 멤버 변수와 지역 변수를 구분할 때 유용함
  - 상속
    + 부모 클래스의 모든 멤버와 메소드를 파생 클래스가 가짐
  - 추상 클래스 (Abstract Class)
    + 미완성 설계도
    + 미완성 메소드 포함할 수 있음
    + 추상 클래스는 인스턴스 생성할 수 없음
    + 상속을 통한 파생 클래스에 의해 완성됨
    + 추상 메소드는 반드시 오버라이드 (override) 해서 사용해야 함
    + 클래스 앞에 abstract 키워드를 붙여서 만듦
  - 인터페이스
    + 클래스에 대한 설계도
    + 상속 받을 클래스가 구현해야 할 기능을 나열함
    + 인스턴스로써 사용할 수 없음
    + interface 키워드를 사용함
  - 추상 클래스와 인터페이스
    + 공통점
      - 스스로 인스턴스를 생성할 수없음
      - 업캐스팅이 가능함
      - 상속 받은 클래스는 모든 메소드를 구현해야 함
  - 봉인 클래스 (Sealed Class)
    + 클래스를 봉인해서 어떤 클래스도 상속을 받을 수 없게 함
    + 클래스 정의 앞에 sealed 키워드를 붙여 선언
    + 자신이 만든 클래스가 더 이상 상속받아서 변경되어 사용되는 것을 방지하기 위함
  - 정적 클래스 (Static Class)
    + 비정적 클래스와 동일하지만, 인스턴스화 할 수 없다는 한 가지 차이점이 있음
    + 인스턴스 변수가 없기 때문에, 클래스 이름 자체를 사용하여 정적 클래스의 멤버에 접근함
    + 정적 멤버만 포함함
    + 봉인되어있음
    + 인스턴스 생성자를 포함할 수 없음

* 속성
  - 속성 (Property)
    + 필드처럼 보이지만 실제로는 메소드임
    + get, set 접근자에 의해 표현
    + 메소드이므로 virtual, static, abstract, override 키워드를 사용할 수 있음
  ```c#
  using System;
  
  namespace Example8{
    public class Date{
      private int month=7;
      public int Month{
        get{ 
          return month; 
        }
        set { 
          if ((value > 0) && (value<13)) 
            month=value;
        }
      }
    }
    
    class Program{
      static void Main(string[] args){
        Date d1=new Date();
        Console.WriteLine("Default month: {0}\n", d1.Month);
        
        while (true){
          Console.Write("Enter month: ");
          int inputMonth=int.Parse((Console.ReadLine()));
          
          if (inputMonth==-1){
            break;
          }
          d1.Month=inputMonth;
          
          Console.WriteLine("Now month: {0}\n",d1.Month);
        }
      }
    }
  }
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/159195554-e60f9967-17e1-449c-9cbe-e2f5e17f86fe.png)

  ```c#
  using System;
  
  abstract class Shape{
    public abstract double Area{
      get;
      set;
    }
  }
  
  class Square : Shape{
    public double side;
    
    public Square(double s){
      side=s;
    }
    
    public override double Area{
      get{
        return side*side;
      }
      set{
        side=Math.Sqrt(value);
      }
    }
  }  
  class Cube : Shape{
    public double side;
    
    public Cube(double s){
      side=s;
    }
    public override double Area{
      get{
        return 6*side*side;
      }
      set{
        side=Math.Sqrt(value/6);
      }
      
    }
  }
  
  class Program{
    static void Main(string[] args){
      // Input the side:
      Console.Write("Enter the side : ");
      double side = double.Parse(Console.ReadLine());
      // Compute the areas:
      Square s = new Square(side);
      Cube c = new Cube(side);
      // Display the results:
      Console.WriteLine("Area of the square = {0:F2}", s.Area);
      Console.WriteLine("Area of the cube = {0:F2}", c.Area);
      // Input the area:
      Console.Write("Enter the area: ");
      double area = double.Parse(Console.ReadLine());
      // Compute the sides:
      s.Area = area;
      c.Area = area;
      
      Console.WriteLine("Side of the square = {0:F2}", s.side);
      Console.WriteLine("Side of the cube = {0:F2}", c.side);
    }
  }
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/159195521-be4eada8-a097-485c-830d-5bb89b35ea8d.png)

* 인덱서
  - 인덱서 (Indexer)
    + 클래스나 구조체의 인스턴스를 배열처럼 인덱스를 써서 접근할 수 있게 함
  - 인덱서의 특징
    + get, set 접근자로 표현
    + this 키워드를 사용
    + 배열에 접근하는 방식처럼 사용









