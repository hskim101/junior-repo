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

## WinFormsProgramming #1
* Winform의 대표적인 구성 요소
  - Form
    + 프로그램이 표시되는 창
    + Form 클래스를 이용하여 구현
  - Control
    + Button이나 Text Box 등 Form에 추가되는 구성 요소들
  - Event
    + 버튼을 클릭하거나 스크롤 바를 움직이는 등 컨트롤에 변화가 생길 때 발생하는 상황
    + 이벤트가 발생했을 때, 그 이벤트에 맞는 처리를 해주는 것이 WinForms의 핵심

* Form 클래스
  - Form 클래스는 상속 관계를 통해 이루어짐
  
  ![image](https://user-images.githubusercontent.com/59719632/160334062-4f45af3f-026c-41f8-a4fe-17a241e897e5.png)

  - Form 클래스 메소드
    + Activate() : 주어진 Form을 활성화시키고, 그 포커스를 Form에 맞춤
    + Close() : Form을 닫음
    + CenterToScreen() : Form을 스크린 부동 중심점에 위치시킴 (화면의 정 중앙에 위치 시킴)
    + LayoutMdi() : 부모 Form 안의 자식 Form들을 모두 정렬함
    + OnResize() : Resize 이벤트에 반응함
    + ShowDialog() : Form을 Modal 대화상자로 나타냄

  ![image](https://user-images.githubusercontent.com/59719632/160335610-006676b6-c0e9-4665-835f-e83393820cad.png)

* Control 클래스
  - 대부분의 Control은 System.Windows.Forms.Control 클래스로부터 파생
  - Control 클래스 속성
    + Anchor : Control이 그려지는 위치를 폼의 어느 가장자리에 고정 시킬 것인지 결정함, 거의 사용하지 않음
    + Dock : Control을 Form의 크기와 상관없이 Form의 지정된 부분을 모두 차지함
    + Label : 텍스트 또는 이미지를 표시할 수 있는 Control, 사용자에게 제목이나 짧은 힌트, 설명을 표시하는 용도로 쓰임
    + TextBox : 사용자로부터 값을 입력 받을 수 있는 Control, 텍스트 선택, 잘라내기, 복사, 붙여넣기 등의 다양한 이벤트 기능을 제공
    + TextBox 사용 예시 : Multiline (여러 줄 입력), WordWrap (자동 줄바꿈 여부), 등
    
    ![image](https://user-images.githubusercontent.com/59719632/160336431-13a11704-edfc-4790-93f7-6a6c1093a0f5.png)

* Button 클래스
  - 이벤트 (Event)
    + 키를 누르거나 마우스로 클릭하는 등의 사용자가 프로그램에 하는 행동
  - 이벤트 핸들러
    + 이벤트가 발생했을 때 호출되는 일종의 함수
  - Button
    + 생성된 Button을 더블 클릭하여 Click 이벤트 핸들러를 만들거나, 속성 뷰에 표시된 이벤트들 중 하나를 명시하면 자동으로 관련 코드가 생성됨
   
  ![image](https://user-images.githubusercontent.com/59719632/160336903-d2cec2ab-2839-4907-847e-9751ecb2e8a4.png)

* RadioButton 클래스와 CheckBox 클래스
  - RadioButton
    + 하나의 label 왼쪽에 작은 원이 나타나 있는 형태
    + 여러 개의 button 중 하나만 선택할 수있음
  - CheckBox
    + 그룹으로 묶이지 않으며, 여러 개의 선택사항을 동시에 선택할 수 있음
    
    ![image](https://user-images.githubusercontent.com/59719632/160348136-bd4e5ee8-f5d0-45f2-98e9-8215e018201d.png)

    ![image](https://user-images.githubusercontent.com/59719632/160351383-881f29a6-72e0-4982-903a-51a9a51e4790.png)

* ListBox 클래스와 CheckedListBox 클래스
  - ListBox
    + 항목의 목록을 나열하는 클래스
    + 목록이 많을 경우, 스크롤바를 사용할 수 있음
  - CheckedListBox
    + 목록에 체크를 할 수 있음
    + 선택할 항목이 많을 경우에, CheckBox 클래스를 사용하는 것보다 유용함
    
    ![image](https://user-images.githubusercontent.com/59719632/160352761-2f584607-b45b-47cf-8e31-3e69cce11cc0.png)

    ![image](https://user-images.githubusercontent.com/59719632/160352706-717708fa-25fd-4bff-8067-d6449dd00110.png)

* ComboBox 클래스
  - ComboBox
    + 많은 아이템 중에서 하나의 아이템을 선택할 경우에 사용함
    
    ![image](https://user-images.githubusercontent.com/59719632/160353244-39cb9fad-5cda-4f09-b502-5522e47d1d7c.png)

* ListView 클래스
  - ListView
    + Windows 탐색기에서 폴더와 파일들을 보여주는 뷰와 유사함
    + 사용자가 표시 방식을 여러가지로 바꿀 수 있는 기능을 제공함
    + View 속성 : LargeIcon, Details, SmallIcon, Lisk, Tile

  ![image](https://user-images.githubusercontent.com/59719632/160353444-7fad9287-ab38-44e9-afaa-575d1d654fc1.png)

  ![image](https://user-images.githubusercontent.com/59719632/160353493-9e51edf9-bffe-406a-a78a-8f040b929a7f.png)

  ![image](https://user-images.githubusercontent.com/59719632/160353984-fb4e5be8-ba72-4467-a73b-54d3cea57936.png)

* Timer 클래스
  - 어떤 주어진 시간마다 이벤트를 실행시키고 싶을 때 사용함
  - 0.1초에 한번씩 1을 증가시키고 화면에 출력, interval을 1000으로 하면 1초에 1번
  
  ![image](https://user-images.githubusercontent.com/59719632/160354083-d587eadd-3541-4b9a-834f-1626f7c1af8f.png)
  
  
* Form 클래스
  - 폼의 외형을 설정하는 속성
  - 폼의 동작을 정의하는 메소드
  - Component 클래스
    + 화면에 표시되지 않는 요소도 Component로 표현함
  - Control 클래스
  - ScrollableControl
    + 스크롤 개념이 필요한 Control을 정의하기 위해서 사용되는 Base 클래스
  - ContainerControl
    + Control, Component를 포함할 수 잇는 포커스를 관리하기 위한 Base 클래스
  - 주요 이벤트
    + Closing 먼저 발생 후 Closed 발생함
* 이벤트
  - 프로그램에 의해 감지되고, 처리될 수 있는 동작이나 사건
  - 메시지 루프
    + 메시지 큐에서 발생하는 메시지를 메시지 핸들러로 전달하여 처리함
    ![image](https://user-images.githubusercontent.com/59719632/161455603-9c43ffec-631b-4f81-8b36-7bcf500fab01.png)
  - 주요 이벤트
    + 키보드 이벤트
    + 마우스 이벤트
* Control 클래스
  - 주요 이벤트


  ![image](https://user-images.githubusercontent.com/59719632/161455673-b066ae91-6820-4d49-898c-f81207a6650d.png)

  - GroupBox 클래스
    + 다른 Control을 포함하는 Container로 사용함
    + 사용자에 대한 이해를 쉽게 함

  - CheckBox 클래스와 RadioButton 클래스
  - PictureBox 클래스

```c#
private void rdoOption_CheckedChanged(object sender, EventArgs e)
        {
            var rdoOption = sender as RadioButton;

            if (null != rdoOption)
            {
                PictureBoxSizeMode SizeMode;

                if (rdoOption == rdoNormal)
                    SizeMode = PictureBoxSizeMode.Normal;
                else if (rdoOption == rdoStretchImage)
                    SizeMode = PictureBoxSizeMode.StretchImage;
                else if (rdoOption == rdoAutoSize)
                    SizeMode = PictureBoxSizeMode.AutoSize;
                else if (rdoOption == rdoCenterImage)
                    SizeMode = PictureBoxSizeMode.CenterImage;
                else
                    SizeMode=PictureBoxSizeMode.Zoom;

                picProfile.SizeMode = SizeMode;
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            picProfile.Visible = !checkBox1.Checked;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            picProfile.ImageLocation = textBox1.Text;
        }
```
* 이벤트 핸들러의 통합과 재사용
  - 동일한 이벤트 핸들러를 사용하면, 작성해야 하는 코드의 양이 줄어듦
  - 기존 동작 이벤트에서 CheckedChanged 속성의 함수를 지우고 새로 작성한 통합 함수를 넣어줌
 
 ```c#
 private void txtNumber_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar) || e.KeyChar == Convert.ToChar(Keys.Back))
                return;
            e.Handled = true;
        }

        private void btnSummit_Click(object sender, EventArgs e)
        {
            string messageString = string.Format("사과 {0}개, 바나나 {1}개",
                txtApple.Text, txtBanana.Text);
            MessageBox.Show(messageString + " 입력받았습니다.");
            var result = MessageBox.Show(
                messageString + " 입력받았습니다.\r\n계속 하시겠습니까?",
                "Caption",
                MessageBoxButtons.OKCancel,
                MessageBoxIcon.Question);

            if (result == DialogResult.OK)
                MessageBox.Show("OK를 눌렀습니다.");
        }
 ```

* 메뉴
  - MenuStrip 클래스
    + 메뉴를 포함하는 메뉴바로 구성되어 있음
    + 각 메뉴는 메뉴 항목을 Drop\-down 형식으로 표시됨
    + 메소드를 활성화 하기 위해, 버튼의 추가기능 또는 버튼 대신에 메뉴 항목을 사용할 수 있음
  - ToolStripMenuItem 클래스
    + MenuStrip이나 ContextMenuStrip에 표시되는 선택 가능한 을 나타냄

* 아이템 컬렉션
  - 아이템을 관리하기 위해 사용함
  
  ![image](https://user-images.githubusercontent.com/59719632/163008121-58530131-72b6-4071-a435-e768dd102017.png)

  ![image](https://user-images.githubusercontent.com/59719632/163008363-72b69242-e691-47e3-ba75-2d421db68f7e.png)

  ![image](https://user-images.githubusercontent.com/59719632/163008663-5e262c76-9f30-4045-99dc-e015046656c7.png)

* 공통 대화상자
  - 모든 windows 응용 프로그램에서 공통적으로 사용되는 대화상자
  
  
  
  
## Chap. Windows Form 4
* 파일 입출력
  - StreamReader 클래스
  - StreamWriter 클래스
  - File 클래스
    + File 클래스
    + FileInfo 클래스
  - Directory 클래스
    + Directory 클래스: 디렉토리 전반의 일을 함
    + DirectoryInfo: 특정 경로에 대해 그 경로의 정보를 나타냄

```c#
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void testFileBtn_Click_Click(object sender, EventArgs e)
        {
            string file_path = "testFile.txt";
            if (File.Exists(file_path))
            {
                File.Delete(file_path);
                MessageBox.Show("파일을 삭제합니다.");
            }
            else
            {
                MessageBox.Show("파일이 존재하지 않습니다.");
            }
        }

        private void testDirBtn_Click_Click(object sender, EventArgs e)
        {
            string directory_path = "testDirectory.txt";
            if (Directory.Exists(directory_path))
            {
                Directory.Delete(directory_path);
                MessageBox.Show("디렉터리를 삭제합니다.");
            }
            else
            {
                MessageBox.Show("디렉터리이 존재하지 않습니다.");
            }
        }
    }
```

* MDI (Multiple Document Interface)
  - 하나의 폼 안에 여러 폼을 포함하여, 개별 폼마다 다른 문서를 동시에 작업할 수 있는 형태의 인터페이스

```c#

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace WindowsFormsApp2
{
    public partial class Parent : Form
    {
        Child child;
        int nChild =0;
        public Parent()
        {
            InitializeComponent();
        }

        private void 새파일ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child = new Child();
            child.MdiParent = this;
            child.Text = "NONAME" + nChild++;
            child.Show();
        }

        private void 열기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (openFDlg.ShowDialog() == DialogResult.OK)
            {
                Stream str = openFDlg.OpenFile();
                StreamReader reader = new StreamReader(str);

                child = new Child();
                child.MdiParent = this;
                child.Text = "NONAME" + nChild++;
                child.Show();

                child.getTextBox().Text = reader.ReadToEnd();
                reader.Close();
                str.Close();
            }
        }

        private void 저장ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveFDlg.ShowDialog() == DialogResult.OK)
            {
                child = (Child)(this.ActiveMdiChild);
                string fName = child.Text;
                StreamWriter write = new StreamWriter(fName);
                write.Write(child.getTextBox().Text);
                write.Close();
           
            }
        }

        private void 다른이름으로저장ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (saveFDlg.ShowDialog() == DialogResult.OK)
            {
                child = (Child)(this.ActiveMdiChild);
                string fName = saveFDlg.FileName;
                StreamWriter write = new StreamWriter(fName);
                write.Write(child.getTextBox().Text);
                write.Close();
                child.Text = fName;
            }
        }

        private void 실행취소ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child=(Child)(this.ActiveMdiChild);
            child.getTextBox().Cut();
        }

        private void 오려내기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child = (Child)(this.ActiveMdiChild);
            child.getTextBox().Cut();
        }

        private void 복사하기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child = (Child)(this.ActiveMdiChild);
            child.getTextBox().Copy();
        }

        private void 붙여넣기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child = (Child)(this.ActiveMdiChild);
            child.getTextBox().Paste();
        }

        private void 지우기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            child = (Child)(this.ActiveMdiChild);
            child.getTextBox().Text = "";
        }

        private void 자동줄바꿈ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (child.getTextBox().WordWrap)
            {
                child.getTextBox().WordWrap = false;
                자동줄바꿈ToolStripMenuItem.Checked = false;
            }
            else
            {
                child.getTextBox().WordWrap = true;
                자동줄바꿈ToolStripMenuItem.Checked = true;
            }
        }

        private void 글꼴ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (fontDlg.ShowDialog() == DialogResult.OK)
            {
                child.getTextBox().Font = fontDlg.Font;
            }
        }

        private void 글자색바꾸기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDlg.ShowDialog() == DialogResult.OK)
                child.getTextBox().ForeColor = colorDlg.Color;
        }

        private void 바탕색바꾸기ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDlg.ShowDialog() == DialogResult.OK)
                child.getTextBox().BackColor = colorDlg.Color;
        }

        private void 바둑판배열세로ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileVertical);
        }

        private void 바둑판배열가로ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileHorizontal);
        }

        private void 계단식배열ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.Cascade);
        }
    }
}
```

```c#
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Child : Form
    {
        public Child()
        {
            InitializeComponent();
        }
        public TextBox getTextBox()
        {
            return this.textBox;
        }
    }

}

```

* 대화상자
  - Modal: 현재 활성화된 창을 닫기 전에는 다른 작업을 할 수 없음
  - Modaless: 현재 활성화된 폼 이외에 다른 폼을 활성화 할 수 있음
  - Owner 속성: Owner 속성으로 지정된 폼이 닫히거나 최소화 되면, 현재의 폼도 함께 닫히거나 최소화 됨

