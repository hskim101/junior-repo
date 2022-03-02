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
  - Systemp Call : OS와 App 사이에 존재하는 Interface 또는 Library
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






