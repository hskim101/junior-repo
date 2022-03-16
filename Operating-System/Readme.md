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

## 2-5. System Programs
* System program : OS system call로 구현된 프로그램.
* File management
  - command line 상에서 호출하는 대부분의 실행 파일
* Status information
  - 어떤 시스템의 상태를 확인할 수 있는 프로그램

## 2-6. Layered Approach
* Layered Approach : 상위 레이어가 하위 레이어의 개체를 호출해 나가는 접근. 
  - 레이어를 건너 뛰어서 호출하면 안되고 순차적으로 호출해야한다. (down call)
  - up call은 사용하면 안된다.
  - 같은 레이어는 양방향 호출해도 무방하다.
* Advantages : 만들기 쉽고 디버깅하기 쉽다.
* Disadvantages : layer의 적절한 배분이 쉽지 않다, 부하가 심해질 수 있다.

![스크린샷 2022-03-10 오전 12 05 13](https://user-images.githubusercontent.com/59719632/157468906-94b0806d-129a-4723-aa28-b4b58f25112b.png)

## 2-7. Monolithic Structure of Simple Structure
* MS\-DOS : 적은 공간에 만들어서 한 레이어가 잘 분리되지 못했다.


![스크린샷 2022-03-10 오전 12 13 09](https://user-images.githubusercontent.com/59719632/157470470-d37cb117-1e6b-4e94-b759-fe29485c44ce.png)

## 2-8. System Structure
* 각각 layered 형태로 구성되어 있다. 
  ![스크린샷 2022-03-10 오전 12 14 14](https://user-images.githubusercontent.com/59719632/157470679-3536d3a0-ea98-4b4a-84d0-e5676bf7bd24.png)

* 문제점 : 새로운 함수를 새로운 레이어들에 확장하는 것이 어렵다. 안정화된 코드를 수정하면 버그들이 생길 수 있다.
 
![스크린샷 2022-03-10 오전 12 17 27](https://user-images.githubusercontent.com/59719632/157471324-eeb5618f-69b5-46d6-a189-d2527b81eb5c.png)

* Microkernel System Structure : 위의 문제점을 보완하기 위해 나온 구조 
  - kernel 안에 최소한의 기능만 집어넣고 나머지 기능들은 모두 user mode로 올림(독립적인 프로세스 서버로 돌아감)

  ![스크린샷 2022-03-10 오전 12 20 36](https://user-images.githubusercontent.com/59719632/157472005-a7e44df9-621b-4508-8fd5-da0f6c3c2bf2.png)

  - 장점 : 버그가 생기면 user mode에서 프로세스가 죽기 때문에 시스템이 다운되지 않는다.

## 2-9. Modules
* 필요한 module만 동적으로 loading 해서 사용한다.
* 장점 : 사용할 필요가 없는 device를 기본적으로 탑재할 필요가 없다.


![스크린샷 2022-03-10 오전 12 26 56](https://user-images.githubusercontent.com/59719632/157473279-fddc84de-f680-4336-8ce9-281ec2f4669a.png)

## 2-10. Virtual Machine
* OS와 hardware를 새로운 hardware 처럼 보이게한다.
* virtual machine은 하나의 hardware라고 볼 수 있다.

![스크린샷 2022-03-10 오전 12 30 58](https://user-images.githubusercontent.com/59719632/157474084-754bc89c-43eb-450b-b957-a49febcbf66b.png)

* VMware Architecture

![스크린샷 2022-03-10 오전 12 32 12](https://user-images.githubusercontent.com/59719632/157474363-4ac350f5-b068-439a-9fda-c7cbe5ec6d95.png)

* Java Virtual Machine
  - class loader : 개발자가 만든 java class file을 load, 개발자가 reference 하고 있는 java API를 load 하는 역할

  ![스크린샷 2022-03-10 오전 12 35 27](https://user-images.githubusercontent.com/59719632/157474928-97c53488-1cfb-4ec0-9b76-57abb31842c3.png)
  
## 2-11. System Boot
* Booting : 컴퓨터를 시작홰서 kernel을 loading하는 과정
* Bootstrap program (or boot loader, BIOS) \- One\-step process
  - Step 1 : 문제가 있는지 검사
  - Step 2 : kernel을 main memory에 load한 후 시작

* Two\-step booting process (Linux, Unix, and Window OS)
  - Step 1 : bootstrap program, 
    + 1) 문제가 있는지 검사
    + 2) Load boot block (Mast Boot Record, MBR)
    + 3) boot block 코드 실행
  - Step 2 : boot block 코드가 kernel을 main memory로 load한다.

![스크린샷 2022-03-10 오전 12 40 51](https://user-images.githubusercontent.com/59719632/157475980-5ec0e70e-18f7-45e7-a1dc-5bf36e0d2e5c.png)

* boot block 안에 OS를 선택할 수 있는 기능이 있다. (멀티 부팅)

![스크린샷 2022-03-10 오전 12 44 31](https://user-images.githubusercontent.com/59719632/157476663-2a7244b0-0040-458b-8788-abf159a06565.png)

# Chap 3. Process
## 3-1. Process Concept
* What exactly is an UNIX process
  - 실행되는 프로그램
  - 자신만의 resource, program count를 가진다.
  - 자신만의 메모리 공간, control information을 가진다.

![스크린샷 2022-03-14 오후 5 28 32](https://user-images.githubusercontent.com/59719632/158133611-19a711a9-ae89-4ede-aa8e-8d9fa95ac711.png)

* Process in Memory
  - 초기화된 전역변수 : initialized data 영역에 저장된다.
  - 초기화되지 않은 전역변수 : uninitialized data 영역에 저장된다.
  - 전체적인 코드는 text 영역에 저장된다. 
  - header 영역에는 실행파일의 정보를 담고 있다.
  - 로딩이 되면 text, initialized data, bss 영역이 메모리에 올라온다. 
  - malloc (동적할당)의 메모리 공간은 heap 영역에 올라온다.
  - 호출된 함수는 user stack 영역에 잡힌다.
  - 스택은 위에서 밑으로 주소가 감소하는 방향, heap은 밑에서 위로 주소가 증가하는 방향으로 잡힌다.
  - process 하나별로 메모리 공간이 잡힌다.

![image](https://user-images.githubusercontent.com/59719632/158584371-4d8de53f-37e9-4b4e-a1a7-07caf086402d.png)

* Process state
  - new : 프로세스가 만들어지기 전 단계
  - running : ready 상태의 프로세스를 CPU에 올린 상태, 자신의 time slice를 모두 소비하면 ready 상태로 이동한다.(cpu 독점을 막기 위함)
  - waiting : sleep(10) 또는 read(fd, pBuf) 같은 함수를 호출하면 다른 event가 생기는 것을 기다리는 상태가 된다. disk에서 파일을 모두 읽어오면 ready상태로 간다.
    + waiting에서 ready로 이동하는 이유는 waiting 상태에서 깨어난 프로세스가 갑자기 running 상태로 올라오게 되면 현재 실행되고 있는 프로세스가 자신에게 할당된 time slice를 소비할 수 없는 상황이 발생된다. 이를 막기 위해 ready 상태로 이동한다.
    + waiting 상태의 process를 CPU에 올려도 실행되지는 않는다. 조건(I/O, sleep, read)이 만족될 때까지 실행되지 않는다.
  - ready : 프로세스가 만들어진 단계, 자신의 실행 순서가 올 때까지 기다린다. ready 상태의 process를 CPU에 올리면 실행된다.
  - terminated : return 또는 exit(0) 을 하게되면 terminated 상태가 된다.
    + Zombie 상태라고도 한다.
    + 자기가 사용하고 있는 resouce들을 깨끗하게 없앤다.
    + 몇 가지 찌꺼기가 남는데 청소(crop)를 하지 않으면 시스템 상에서 문제가 발생할 수 있다.
    + waitpid(), wait() 함수를 사용하면 zombie 상태의 프로세스를 깨끗하게 청소할 수 있다.

  ![image](https://user-images.githubusercontent.com/59719632/158587549-f1e9b43c-97fd-4b90-b314-c8f860c7bbb4.png)
  
* Process Control Block (PCB) : 프로세스의 정보를 담아두고 있는 일종의 구조체
  - Process state
  - Program Counter : 다음에 실행할 명령어를 가리킴
  - CPU registers
  - CPU scheduling information 
  - Memory\-management information
  - Accounting information
  - I/O status information : 대표적으로 file descriptor table

* Process Scheduling
  - Multiprogramming : 프로세스를 동시에 실행하는 동작, CPU 효율을 최대화함
  - Time\-Sharing : 여러 사용자가 컴퓨터를 동시에 사용하게 하는 동작, 각 사용자가 해당하는 컴퓨터를 자신만의 컴퓨터로 느끼게 해주는 기능
  - Process scheduler : Multiprogramming과 Time\-Sharing을 지원해주는 역할
  
* CPU Switch

![image](https://user-images.githubusercontent.com/59719632/158590816-719d5eff-f366-4601-85bd-e12e6a31eb01.png)

* Process Scheduling Queues
  - Job queue : 모든 프로세스를 관리하는 queue
  - Ready queue : ready 상태의 프로세스를 관리하는 queue
  - Waiting queue
    + Device queue : I/O device
    + Waiting queue per resorce (message queue, socket, semaphore)

![image](https://user-images.githubusercontent.com/59719632/158592149-7e8ae003-be1c-4e0b-a479-d7561031410b.png)

* Schedulers
  - Short\-term scheduler : process scheduler

* Context Switch
  - context : CPU registers, process state를 가리킴, PCB 안에 저장된다.
p0 가 실행 중인데 p1로 context swtich 한다고 가정.   
context switch가 발생하면 cpu는 p0를 정지시킴, cpu 안에 들어있는 register 값들과 state를 메모리(PCB) 상에 저장함(각 프로세스마다 메모리 공간이 있음)   
p0의 context가 p0의 PCB 안으로 저장된다. 정지했다가 다시 시작할 p1의 context를 cpu 상으로 로드한다. 로드가 완료되면 p1은 이전에 정지된 시점부터 다시 실행된다.   
p1 \-> p0 context swtich 발생 시, p0의 context가 다시 cpu로 로드, p0가 이전에 정지된 시점부터 자동으로 다시 실행된다.

![image](https://user-images.githubusercontent.com/59719632/158593772-f944a14d-ac37-4553-86a4-781ffc7c4213.png)

* Process Creation
  - Parent process가 children process를 생성하는 과정
  - 프로세스는 자신만의 고유한 pid를 가지고 있다.
  - fork() 함수로 프로세스 생성 가능
  - pageout, fsflush 프로세스는 kernel 프로세스이다.
  - **child와 parent간에 서로 변경한 데이터 내용은 서로 볼 수 없다.**
  - 변경된 데이터는 각 프로세스만 볼 수 있다.
  - child를 생성할 때 parent의 resource가 child에게 그대로 물려받는다.
![image](https://user-images.githubusercontent.com/59719632/158595873-19aae371-2e73-4cbb-a7c2-e67fa60beb5a.png)


