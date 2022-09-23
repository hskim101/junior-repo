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
        
  
  
  
  
  


