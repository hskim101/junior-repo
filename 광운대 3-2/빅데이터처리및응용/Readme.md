# 빅데이터처리및응용

## Chap 1. Mining Massive Data Sets

### 1-1. Intro

### 1-2. MapReduce

### 1-3. Spark
* Problems with MapReduce
    - MapReduce를 할 때마다 Disk에서 data를 읽는 작업을 계속 해줘야함 => Overhead 발생
    - 많은 프로그램들이 MapReduce로 변환이 잘 안된다.
    - bottleneck 가능성
    - large application에 적합하지 않음
* Data\-Flow Systems
    - Data\-Flow 관점에서 MapReduce는 2개의 rank를 가짐
    - 하나는 Map, 나머지는 Reduce
    - Data\-Flow Systems에서는 task 또는 rank의 제한이 없다. (MapReduce는 2개)
    - Map and Reduce 외에 다른 함수도 허용한다.
    - 망가진 시점 근처에서 그 이후에 수행된 작업만 복구하면 된다.
    - Data가 one way로 흐르는 것이 복구하기에 용이하다.
* Spark
    - Map\-reduce model에 국한되지 않은 시스템
    - 중간 결과를 disk에 가급적 쓰지 않으려고 함
    - caching을 통해 빠른 작업을 수행
    - 다양한 함수 사용
    - Directed Acycllic Graph 사용
    - 하둡과 호환 가능
    - RDD (Resilient Distributed Dataset)
        + key, value pair 강제 하지 않음
        + Caching dataset in memory
        + RDD를 다른 RDD로 transform해서 겨로가를 낼 수 있음
        + Transformations: RDD를 변환해서 다른 RDD를 만들어냄
        + Lazy evaluation: 사용자가 어떠한 action을 요구하기 전까지 아무런 action을 취하지 않음 (사용자 명령어를 최적화할 수 있는 장점)
        + Actions: return value or export data
    - DataFrame, Dataset 지원
        + Pandas DataFrame과 동일
        + 둘 다 RDD로 변환 가능
    - Spark SQL
    - Spark Streaming
    - MLlib
    - GraphX
    - Spark vs Hadoop
        + 성능상에서는 Spark가 더 빠르다.
        + Memory에서 작업을 하면 할 수록 Spark이 빠르다.
        + Memory가 크지 않을 때 disk를 사용하게 되므로 spark의 성능이 떨어진다.
        + MapReduce는 성능 저하가 크게 없이 다른 서비스들과 잘 동작하지만 Spark는 잘못 쓰면 Memory를 왕창 쓰게 된다.
        + Spark이 프로그래머 입장에서는 훨씬 쉽다.
        + 일반적으로 Spark이 좋다.
         
### 1-4. Problems Suited for MapReduce  
* 
  
  


