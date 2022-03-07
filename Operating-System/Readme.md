Operating System
================
시험 정리 자료
-----------

# Chap 1. Introduction

## 1-1. Computer System의 4가지 계층
  - User
  - System Programs and Application Programs
    + compiler, assembler, 개발툴, Database, etc. 
  - Operating System
  - Hardware
    + CPU, I/O, Memory
   
 <img width="520" alt="스크린샷 2022-03-02 오후 12 17 05" src="https://user-images.githubusercontent.com/59719632/156288923-a5f5883a-d072-4532-990e-590404198090.png">
 
## 1-2. Operating System
  - 주요 기능
    + **사용자의 프로그램 실행**
    + **사용자가 Computer System을 쉽게 사용할 수 있게 함**
    + 라이브러리를 제공해서 개발자가 쉽게 OS에 접근할 수 있도록 함
    + Memory를 효율적으로 사용할 수 있게 함
    
  - Definition
    + 사용자와 하드웨어 사이에 존재하는 프로그램
    + 하드웨어를 제어 및 할당하는 기능을 포함하는 소프트웨어
    + **kernel** 이라고도 부름

## 1-3. Operating System Roles
  - 사용자 관점에서, 사용자가 편리하게 사용하게 함, 사용자의 작업을 빠르게 처리(고성능)
  - System 관점에서,
    + **resource allocator**
      * resource를 효율적이고 공평하게 할당하는 역할
    + **control program**
      * 강제 종료, 에러 메세지 등

## 1-4. Structure
  - System Call : OS와 App 사이에 존재하는 Interface 또는 Library
  - Kernel
    + **Process Management** : 여러 개의 프로세스가 공평하게 실행되도록 관리
    + **Memory Management**
      * Virtual Memory 제공
      * Memory를 효율적으로 관리
    + **File Management**
      * File 생성, 삭제
      * Directory 생성, 삭제
    + I/O Management
      * **Disk**
      * Keyboard
      * Monitor
      
<img width="535" alt="스크린샷 2022-03-02 오후 12 34 50" src="https://user-images.githubusercontent.com/59719632/156290899-693bb830-6438-43e6-8a67-3f38bf763f2c.png">

## 1-5. Dual\-mode Operation : OS를 보호하기 위함
  - User mode : 우리가 짠 code
  - kernel mode : system call 호출 시 CPU는 kernel mode로 들어가서 system call을 실행한다.
  - Exceptions/Interrupts : 일종의 event, CPU가 정상적으로 실행하는 프로세스를 정지 시키고 특정한 명령을 실행하는 프로세스를 실행시킴
    + Exceptions : CPU가 사용자가 구현한 code를 실행할 때 발생하는 event. 내부적으로 발생하는 event.
      * division by zero
      * segmentation fault
    + Interrupts : 외부에서 발생하는 event
      * I/O
      * keyboard
    + exception/interrupt 발생 시 OS 내부(device driver)에 event를 처리하기 위한 code가 정의되어 있다.
    
<img width="515" alt="스크린샷 2022-03-02 오후 12 46 51" src="https://user-images.githubusercontent.com/59719632/156291210-23514ca5-a8c8-46bd-ac2d-a811c31842fd.png">

## 1-6. **Transition from User to Kernel Mode**
  - **System Call** : fork(), read(), write() 등, 개발자가 합법적으로 kernel mode로 들어갈 수 있는 유일한 방법
  - looping 도중 interrupt 발생 시 user mode -> kernel mode로 변경
  - exception 발생 시 kernel mode로 변경 후 강제 종료
  - Multitasking에서 scheduler가 프로세스를 이동 할 때 

<img width="601" alt="스크린샷 2022-03-02 오후 1 06 02" src="https://user-images.githubusercontent.com/59719632/156293462-a70f26c7-1a86-45ab-a916-747b34ed58d1.png">

## 1-7. User to kernel
- Implementation
  + Mode bit : provided by hardware
    * user mode : 1
    * kernel mode : 0
    
<img width="588" alt="스크린샷 2022-03-02 오후 1 15 57" src="https://user-images.githubusercontent.com/59719632/156293999-f61803aa-3608-4e5b-ab72-927970ab6d4d.png">

# Chap 2. Structures

## 2-1. User Operating System Interface
* CLI (Command Line Interface)
  - terminal 기반의 명렬어를 받아서 처리하는 인터페이스
  - shell은 Multiple command interpreter이다.

* Metaphor interface (GUI)
  - mouse, keyboard, monitor를 통해 사용하는 interface
  - 마우스 기반의 윈도우 메뉴 시스템 interface를 desktop metaphor interface 라고도 한다.
  - Unix (Command Desktop Environment (CDE)), Linux (GNOME)

* 많은 시스템에서 CLI와 GUI interfaces 둘다 제공

## 2-2. System Call and API
* Definition of system call
  - OS 서비스를 제공하는 프로그래밍 인터페이스

* Implementation of system calls
  - C or C++ 로 작성됨

* Definition of API (Application Programming Interface)
  - Application 프로그래머들이 사용할 수 있게 하는 functions
  - Middleware layers에서 제공한다. 
  - 대부분의 application들은 하이레벨 API를 사용하고 system call을 직접 쓰지는 않는다.

* Example
  - Win32 API for Windows
  - POSIX API for POSIX-based systems (Unix, Linux, Mac OS X)
  - Java API for Java virtual machine (JVM)

* API 사용하는 이유
  - Compatibility(호환성) : 같은 API를 여러 프로그램에서 compile, run을 할 수 있다.
  - cygwin : posix api로 만들어진 앱을 window에서 바로 구동할 수 있도록 해줌, 계층이 늘어나기 때문에 CPU부하가 늘어나서 앱의 성능이 느려질 수 있는 문제가 있다.
  - Information hiding : OS 내부의 구조를 모르더라도 앱 개발을 할 수 있게 해준다.
  - API가 제공하는 함수가 system call 보다 많다.
  
 <img width="400" alt="스크린샷 2022-03-07 오후 12 18 11" src="https://user-images.githubusercontent.com/59719632/156962008-9123d368-f953-44dd-9ff8-59c09dec6b4e.png">

* API \- System Call \- OS Relationship
  
<img width="400" alt="스크린샷 2022-03-07 오후 12 24 52" src="https://user-images.githubusercontent.com/59719632/156962549-7c068ba0-3706-4b64-8c68-312cd0847858.png">

* Example : Standard C Library
  - printf() library call, printf는 posix이다.
  - "**API는 내부적으로 System call을 사용하고 있다**" 만 알고 있으면 된다.    
  
<img width="400" alt="스크린샷 2022-03-07 오후 12 28 52" src="https://user-images.githubusercontent.com/59719632/156962973-b36cf2e4-9b17-485e-88da-d540a60d821b.png">

## 2-3. System Call Implementation

* 각각의 system call은 자신만의 번호를 가지고 있다.
  - 부팅을 하면 **sys_call_table** 테이블이 메모리에 만들어진다.
  - 함수의 이름은 함수 포인터이다. 
  
  <img width="500" alt="스크린샷 2022-03-07 오후 12 31 48" src="https://user-images.githubusercontent.com/59719632/156963405-6ffd487d-53e0-4ccb-9392-d7907c3e2a52.png">

* Case Study : Linux
  - system read
    + int read(int fd, void\* pBuf, int nBytes);
  - System call is defined as macro
    + #define __NR_read 3
    + _syscall3(int, \_\_NR\_read, int, fd, void\*, pBuf, int, nBytes)
  - read 함수 호출 과정
    + read 함수 호출 
    + system call 번호를 EAX라는 cpu register에 저장 
    + interrupt 0x80 실행하면 user mode 에서 kernel mode로 전환  
    + sys\_call\_table에서 read와 관련된 함수 포인터를 호출
    + 쭉 실행되다가 kernel mode에서 user mode로 return

  <img width="500" height="500" alt="스크린샷 2022-03-07 오후 12 43 10" src="https://user-images.githubusercontent.com/59719632/156964129-641a8d32-61ca-4da8-8247-b87ce8241b93.png">
  
  - "**TRAP**" 이라는 exception을 사용하게 되면 user mode에서 kernel 모드로 이동하게 된다.
    + interrupt 0x80
  - System call 번호는 EAX register에 저장된다.
  - 그 번호는 <am/unistd.h>에 정의된 함수 포인터를 호출하게 해준다.

## 2-4. System Call parameter Passing
* Parameters는 **block or in\-memory table**에 저장된다.
  - system call을 호출할 때 block을 메모리에 만들고, system call을 통과한 args를 block에 차곡차곡 쌓는다.
  - cpu register 하나만 사용해도 할 수 있다.
  - args가 아무리 많더라도 시작 위치만 던져 줄 수 있기 때문에 args에 대한 갯수, 길이 제한이 없다.
  - window에서는 stack 영역을 사용한다.


<img width="550" alt="스크린샷 2022-03-07 오후 12 59 42" src="https://user-images.githubusercontent.com/59719632/156965628-9bd171c1-9414-4106-97af-8972b9559bc8.png">





