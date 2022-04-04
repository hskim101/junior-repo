Algorithm
=========
전공 자료 정리
----------

# Chap 1. Algorithms: Efficiency, Analysis, and Order
* 챕터 1에서는 알고리즘의 효율성(efficiency)을 다룬다.
* "Order" 라는 개념은 알고리즘의 efficiency를 나타낸다.

## 1-1.Some Definitions
* Problem : a question to which we seek an answer.
* Problem Instance : 각각의 parameter가 값을 갖는 경우
  - ex) Determine whether the number 5 is in the list [10, 7, 11, 5, 13, 8] of 6 numbers.
* Algorithm : 각각의 problem instance를 해결하기 위한 단계별 절차.
  - ex) Sequential Search Algorithm(순차 탐색)

## 1-2. 효율적인 알고리즘 개발의 중요성
* Sequential Search Algorithm

```java
// Java
public static index SeqSearch(int n, keyType[] S, keyType x){
    index location = 1;
    while(location <= n && S[location] != x)
        location++;
    if(location>n)
        location = 0;
    return location;
}
```

```python3
# python3
def seq_search(n:int, lst:list, target:int):
    for i in range(n):
        if lst[i]==target:
            return i
    return -1
lst=[1,5,7,9,2,4,3]
print(seq_search(len(lst),lst,10))
```

* Binary Search Algorithm
  - list가 정렬되어 있는 상태

```java
// Java
public static index BinarySearch(int n, keyType[] S, keyType x){
    index location, low, high, mid;
    
    low = 1;
    high = n;
    location = 0;
    
    while(low <= high && location == 0){
        mid=(low+high)/2;
        if(x==S[mid])
            location = mid;
        else if(x < S[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return location;
}
```

```python3
# python3
def binary_search(lst,target): # Iterative
    start=0
    end=len(lst)-1

    while start<=end:
        mid=(start+end)//2

        if lst[mid]==target:
            return mid
        elif lst[mid]>target:
            end=mid-1
        else:
            start=mid+1

lst=[1,2,3,4,5,6]
print(binary_search(lst,4))    
```

```python3
# python3
def binary_search(lst,target,start,end): # Recursive
    while start<=end:
        mid=(start+end)//2

        if lst[mid]==target:
            return mid
        elif lst[mid]>target:
            return binary_search(lst,target,start,mid-1)
        else:
            return binary_search(lst,target,mid+1,end)

lst=[1,2,3,4,5,6]
print(binary_search(lst,4,0,len(lst)-1))
```

* Sequential Search vs Binary Search
  - worst case 비교
    + 가장 핵심적인 연산(basic operation)이 실행되는 횟수로 비교
    
<img width="547" alt="스크린샷 2022-02-28 오후 7 25 29" src="https://user-images.githubusercontent.com/59719632/155966908-5f7f6041-b5f6-441e-80d4-4dedae6edcf7.png">

* Fibonacci Sequence

<img width="645" alt="스크린샷 2022-02-28 오후 7 27 59" src="https://user-images.githubusercontent.com/59719632/155967348-c210d34b-5a70-43f0-8a52-bae93dfbe282.png">

  - Recursive Algorithm
    + 굉장히 비효율적
```java
// Java
public static int Fib(int n){
    if(n<=1)
        return n;
    else
        return Fib(n-1) + Fib(n-2);
}
```
```python3
# python3
def fib(n): # Recursive
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
```


<img width="597" alt="스크린샷 2022-02-28 오후 7 30 38" src="https://user-images.githubusercontent.com/59719632/155967711-755dd478-5ca6-4325-9996-8b233a2069b7.png">

  - Iterative Algorithm

```java
// Java
public static int Fib2(int n){
    index i;
    int[] f=new int[n+1]; // n번째 항 구하려면 배열 size가 n+1이여야 한다. 0번째 항부터 시작하므로.
    
    f[0] = 0;
    if(n > 0){
        f[1] = 1;
        for(i=2 ; i<=n ; i++)
            f[i]=f[i-1]+f[i-2];
    }
    return f[n];
}
```

```python3
# python3
def fib(n): # Iterative ( Dynamic-Programming)
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
```

<img width="268" alt="스크린샷 2022-02-28 오후 7 48 48" src="https://user-images.githubusercontent.com/59719632/155970310-26fa2123-3206-4c8f-bff9-7df25a98dfef.png">

<img width="583" alt="스크린샷 2022-02-28 오후 7 49 30" src="https://user-images.githubusercontent.com/59719632/155970401-6a2c4955-91c8-4f66-99ed-cb9b5bdd435a.png">

## 1-3. Analysis of Algorithms
* Input Size
  - size of array
    + ex) **n**\-tuple
  - single number
    + ex) **n**\-th Fibonacci Number
  - Graph에서는 vertices 수와 edges 수 둘 다 input size이다.

* Basic Operation
  - 알고리즘이 실행될 때 알고리즘 전체의 계산 양에 가장 많은 영향을 미치는 연산
    + 정렬 또는 탐색 알고리즘의 비교 연산
    + 행렬 곱의 덧셈 연산
* Time Complexity (시간 복잡도)
  - 입력 크기에 대한 basic operation 횟수
    + 순차 탐색 알고리즘의 worst case는 **n**번 비교하는 것이다.
    + 개발 환경과 독립이다.
* Types of Time Complexity Analysis
  - Sum of **n** numbers

```java
// java
int sum(int n, keyType[] S){
    int i=0;
    int total=0;
    while(++i<=n)
        total=total+S[i] # + 연산
    return total;
}
```

```python3
# python3
def sum(n:int, S:list):
    total=0
    for i in range(n):
        total+=S[i]
    return total
```

  - Sequential Search for **x**


```java
// java
int SeqSearch(int n, keyType[] S, keyType x){
    location = 1;
    while(location <= n && S[location] != x) # != 비교 연산
        location++;
    if(location>n)
        location = 0;
    return location;
```

```python3
# python3
def seq_search(n:int, S:list, x:int){
    for location in range(n):
        if S[location]==x:
            break
    if(location>=n)
        location = -1;
    return location;
```

  <img width="604" alt="스크린샷 2022-03-01 오후 3 12 24" src="https://user-images.githubusercontent.com/59719632/156114996-4eb033a5-7928-435f-952d-1718ca3508f2.png">

  - Every Case
    + Size가 **n**인 모든 인스턴스에 대해 **basic operation**이 동일한 횟수로 수행될 때 적용 가능
    + sum 연산
  - Non-Every case : 동일한 input size라도 basic operation 실행 횟수가 달라질 수 있다.
    + Best Case : the **minimum** of times
    + Worst Case : the **maximum** of times
    + Average Case : the **average** of times

  - Example: Sequential Search
    + Basic Operation : **Comparison**
    + Input Size : **n**, the array size
    + Best Case : 1
    + Worst Case : n
    + Average Case : **p**를 **target**이 배열에 있을 확률이라고 하면, p\*(k번째에서 찾을 확률) + (1-p)\*(끝까지 못 찾을 확률)

<img width="572" alt="스크린샷 2022-03-01 오후 3 24 06" src="https://user-images.githubusercontent.com/59719632/156116295-fb17545d-d1a3-4418-bfc0-c329841b10d5.png">

  - Considering Overhead Instructions
    + T(n)=n\*(1000\*t)
    + T2(n)=n^2\*(1\*t)
      * T2(n) 알고리즘이 T(n) 보다 n<1000 일 때 더 낫다. n의 값이 클 경우 T(n)이 더 낫다.
      * 일반적으로 복잡도가 n^k인 함수에서 k가 작을수록 효율적이다.
      * n이 작은 경우 차수가 높은 알고리즘이 더 좋을 수 있다.

## 1-4. Order
* Complexity Function
  - any function from. the **non\-negative integers** to the **non\-negative real** numbers
  - ex) n, log n, n^2 + n/2
 
* Complextiy of an Algorithm
  - 입력 크기에 따라 basic operation이 몇 회나 실행되는지 나타내는 함수.

* Linear Time Algorithm
  - O(n)
  - ex) Worst case of Sequential Search with n items.
 
* Quadratic Time Algorithm
  - O(n^2)
  - ex) Average case of Bubble sort with n items.

**Input Size가 충분히 클 때 알고리즘이 어떻게 수행되는지 관심이 있다.**

<p align="center">
<img width="300" alt="스크린샷 2022-03-01 오후 3 42 45" src="https://user-images.githubusercontent.com/59719632/156118442-8690ad49-72b1-4cb0-b962-cdbeb83570de.png"> <img width="300" alt="스크린샷 2022-03-01 오후 3 42 52" src="https://user-images.githubusercontent.com/59719632/156118462-811714c3-06e9-439a-81ff-53be5f13f56e.png"></p>

<img width="400" alt="스크린샷 2022-03-01 오후 3 43 01" src="https://user-images.githubusercontent.com/59719632/156118639-ca8d14bd-7281-4931-9d2b-a7795f4cf3e5.png">

* **Big O**
  - O(f(n)) is the set of complexity functions g(n)
for which there exists some positive **real constant c** and **some non\-negative integer N**
  - f(n) (i.e log n, n, nlog n, n^2, n^3, 2^n, n!, ...)
  - g(n) <= c\*f(n) 일 때 O(g(n)) = O(f(n))

<img width="400" alt="스크린샷 2022-03-01 오후 4 02 14" src="https://user-images.githubusercontent.com/59719632/156120827-fdfd4ff0-ac0e-495a-af01-b4cf222f0d20.png">

  - 증명 과정 (정의 이용), 상수 c와 N 찾음

<img width="600" alt="스크린샷 2022-03-07 오후 11 18 08" src="https://user-images.githubusercontent.com/59719632/157051909-94b39bea-c7ac-4d68-a41e-eb430f98dc22.png">

  - 반례 이용
  
  <img width="600" alt="스크린샷 2022-03-07 오후 11 35 34" src="https://user-images.githubusercontent.com/59719632/157054540-a0d7526a-c71c-48e2-b51e-1bac5121d6d2.png">

* **Omega(Ω)**
  - g(n) >= c\*f(n), for all n>=N (Big O와 부등호 방향 반대)
  - 차수가 높거나 같은 것
 
<img width="600" alt="스크린샷 2022-03-01 오후 4 07 00" src="https://user-images.githubusercontent.com/59719632/156121402-010927cc-b505-4fd5-8a12-ea0f7046e18f.png">

  - 중명 과정 
  
  <img width="600" alt="스크린샷 2022-03-07 오후 11 39 43" src="https://user-images.githubusercontent.com/59719632/157055305-e26cd76f-b650-4292-b58a-c579b3a3337c.png">

<img width="600" alt="스크린샷 2022-03-07 오후 11 44 48" src="https://user-images.githubusercontent.com/59719632/157056249-c457627c-a526-40e7-b79d-af867c417c3c.png">

* **Theta(θ)**
  - Omega와 Big O의 교집합
  - θ(f(n))은 f(n)의 최고 차수
  - c\*f(n) <= g(n) <= d\*f(n), for all n>=N
  - 상수배 관계

<img width="600" alt="스크린샷 2022-03-01 오후 4 08 55" src="https://user-images.githubusercontent.com/59719632/156121659-209c88ed-74b0-432f-902e-306d88a03013.png">


* **small o**
  - O(f(n))과 거의 비슷하지만 small o는 n이 무한대로 커질 때만 사용
  - g(n)의 절대값에 어떤 작은 양의 숫자를 곱해도 f(n)보다는 크게되는 순간이 x를 키우다보면 언젠가는 나타난다.
  - small o가 성립하면 Big O도 성립한다.
  - f(n)의 차수 이하인 것들
  - g(n) <= c\*f(n), for all n>=N, 모든 c에 대해 성립
  - Big O는 어떤 c, small o는 모든 c에 대해 성립
 

  <img width="161" alt="스크린샷 2022-03-01 오후 4 18 19" src="https://user-images.githubusercontent.com/59719632/156122844-7bd5576f-0d69-40c8-80ce-87cc4d507e5f.png">
  
  ![스크린샷 2022-03-10 오전 11 39 01](https://user-images.githubusercontent.com/59719632/157577546-afb1421a-1b5f-4768-8c12-ce5b37a428c9.png)

  - by contradiction을 이용한 반례 증명

  ![스크린샷 2022-03-10 오전 11 42 04](https://user-images.githubusercontent.com/59719632/157577846-745bbe82-c190-4cea-b780-17cdd2423564.png)
  
  - 배수인 경우 상수를 1 이하로 만드는 c로 반례 증명
  
  ![스크린샷 2022-03-10 오전 11 44 25](https://user-images.githubusercontent.com/59719632/157578106-80591ae3-23fc-46c5-a0e5-d24b096db6d5.png)


* Properties of Order

<img width="400" alt="스크린샷 2022-03-01 오후 4 22 48" src="https://user-images.githubusercontent.com/59719632/156123481-39116389-d0a4-48bf-ba62-9de2d919f76f.png">

* Using a Limit to Determine Order

  <img width="454" alt="스크린샷 2022-03-01 오후 4 23 32" src="https://user-images.githubusercontent.com/59719632/156123545-358a3bf5-21b1-4ca1-b608-a467cb8cb868.png">

  - **Exponential이 Factorial보다 느리게 증가함 증명**
  
  <img width="586" alt="스크린샷 2022-03-01 오후 4 25 48" src="https://user-images.githubusercontent.com/59719632/156123933-49408f0e-6155-4486-a2a2-8b7447a960f0.png">

   - 로피탈 정리 이용한 **small o** 증명

  <img width="493" alt="스크린샷 2022-03-01 오후 4 25 56" src="https://user-images.githubusercontent.com/59719632/156123950-7ec6d0bc-55ac-4116-bd85-684ee07bfff8.png">

# Chap 2. Divide and Conquer
* Divide and Conquer
  - Step 1: Divide
    + 원래 문제의 instance를 작은 instance로 분할
  - Step 2: Conquer
    + 작아진 instance를 풀 수 있으면 풀거나 재귀적으로 더 작게 분할
  - Step 3: (If necessary) Combine
    + 작은 문제들의 해를 얻고 이 해들을 큰 문제의 해로 결합해주는 과정

## 2-1. Binary Search
* Step
  - step 0: If x=S[mid], quit
  - step 1: Divide
    + If x>S[mid], 오른쪽 서브배열에서 찾음
    + If x<S[mid], 왼쪽 서브배열에서 찾음
  - step 2: Conquer
    + 서브 배열에서 x를 찾았는지 검사
  - Worst\-Case Time Complexity of Binary Search
    + Basic Operation : x와 S[mid]의 비교 연산
    + Input Size : 배열의 item 수
    + Assumption : n=2^k, 어떤 입력을 반 분을 했을 때 정수로 나옴
    + W(n) = W(n/2) + 1 for n>1, W(1)=1
    
   <img width="500" alt="스크린샷 2022-03-20 오전 10 48 52" src="https://user-images.githubusercontent.com/59719632/159144591-9cf1c6cb-992a-4636-8f7f-7b58b1c26882.png">

  ```java
    // Java
    public static index BinarySearch(int n, keyType[] S, keyType x){
        index location, low, high, mid;

      low = 1;
      high = n;
      location = 0;

      while(low <= high && location == 0){
          mid=(low+high)/2;
          if(x==S[mid])
              location = mid;
          else if(x < S[mid])
              high = mid - 1;
          else
              low = mid + 1;
      }
      return location;
  }
  ```

  ```python3
  # python3
  def binary_search(lst,target): # Iterative
      start=0
      end=len(lst)-1

      while start<=end:
          mid=(start+end)//2

          if lst[mid]==target:
              return mid
          elif lst[mid]>target:
              end=mid-1
          else:
              start=mid+1

  lst=[1,2,3,4,5,6]
  print(binary_search(lst,4))    
  ```

  ```python3
  # python3
  def binary_search(lst,target,start,end): # Recursive
      while start<=end:
          mid=(start+end)//2

          if lst[mid]==target:
              return mid
          elif lst[mid]>target:
              return binary_search(lst,target,start,mid-1)
          else:
              return binary_search(lst,target,mid+1,end)

  lst=[1,2,3,4,5,6]
  print(binary_search(lst,4,0,len(lst)-1))
  ```
## 2-2. Merge Sort
* Step
  - Step 1: Divide
    + 두 개의 서브배열로 반 분한다.
  - Step 2: Conquer
    + 서브배열이 충분히 작으면 정렬한다
    + 더 분할이 가능하면 재귀적으로 분할한다.
  - Step 3: Combine
    + 정렬된 서브배열을 Merge한다.
  - Best Case Time Complexity of Merge
    + Basic Operation : U[i] 와 V[j]의 비교연산
    + Input size : 각 서브 배열의 길이
    + U 와 V가 모두 오름차순 정렬되어있고, len(U) < len(V) 이고, V의 최소값이 U의 최대값보다 큰 경우가 Best Case이다.
    + B(h,m) = min(h,m)
  - Worst Case Time Complexity of Merge
    + 제일 마지막 cell을 제외하고 나머지 값들이 모두 비교를 한 후 채워지는 경우
    + W(h,m) = h+m-1
    + W(n) = W(h) + W(m) + W(h,m) = W(h) + W(m) + h + m - 1

  <img width="622" alt="스크린샷 2022-03-20 오후 1 52 38" src="https://user-images.githubusercontent.com/59719632/159148768-19ccbe30-5062-4632-bb78-3903fcc666a7.png">


```python3  
def merge(U, V):
    S = []
    i = j = 0
    while (i < len(U) and j < len(V)):
        if (U[i] < V[j]):
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1
    # 카피되지 않고 남아있는 나머지 배열을 뒤에 concat
    if (i < len(U)):
        S = S + U[i : len(U)]
    else:
        S = S + V[j : len(V)]
    return S

def mergesort (S):
    n = len(S)
    if (n <= 1):
        return S
    else:
        mid = n // 2
        U = mergesort(S[0 : mid])
        V = mergesort(S[mid : n])
        print("U =", U, end=" ")
        print("V =", V)
        return merge(U, V)

S = [27, 10, 12, 20, 25, 13, 15, 22]
print('Before: ', S)
X = mergesort(S)
print(' After: ', X)
```
```python3
def merge2 (S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while (i <= mid and j <= high):
        if (S[i] < S[j]):
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1
    if (i <= mid):
        U += S[i : mid + 1]
    else:
        U += S[j : high + 1]
    for k in range(low, high + 1):
        S[k] = U[k - low]
    
def mergesort2 (S, low, high):
    if (low < high):
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        mergesort2(S, mid + 1, high)
        print(S[low:high + 1])
        merge2(S, low, mid, high)

S = [27, 10, 12, 20, 25, 13, 15, 22]
print('Before: ', S)
mergesort2(S, 0, len(S) - 1)
print(' After: ', S)
```

## 2-3. Quick Sort (Partition Exchange Sort)
* Similar to MergeSort
  - dividing the array into two partitions
  - sorting each partition recursively
* Different from MergeSort
  - Pivot item을 선택해서 pivot 보다 작은 것들을 왼쪽, 큰 것들을 오른쪽에 오도록 분할
  - Combine 단계가 필요없다.

* 과정
  - Array에 있는 첫 번째 아이템을 pivot으로 정한다
  - pivot 보다 작은 것들을 왼쪽, 큰 것들을 오른쪽에 오도록 partition 한다.
  - 각각의 partition을 재귀적으로 정렬한다.
  
  ```java
  // low: partition의 가작 작은 index
  // high: partition의 가장 큰 index
  publicv static void quickSort(index low, index high){
      index pivotPoint;
      
      if(high > low){
          pivotPoint=partition(low,high);
          quickSort(low,pivotPoint-1); // 왼쪽 partition 정렬
          quickSort(pivotPoint+1,high); // 오른쪽 partition 정렬
      }
  }
  
  // Partition Algorithm 
  // 1. local array를 하나 사용하는 방식
  //    i: S의 loop index
  //    j: pivot보다 작은 값부터 시작하는 index, 왼쪽부터 채운다.(j++)
  //    k: pivot보다 큰 값부터 시작하는 index, 오른쪽부터 채운다.(k--)
  //    j==k 일때 더 이상 비교할 값이 없으므로 pivot을 이 위치에 넣어준다.
  //    이 방식의 단점은 local array 만큼의 메모리가 더 필요하다. local array의 값을 S에 다시 copy해야 한다.
  
  // 2. In-Place Partition
  //    i: S의 loop index
  //    j: 현재까지 저장한 pivot보다 작은 값 위치
  //    pivot보다 작은 값을 찾으면 j 다음 인덱스 값과 자리 바꿈
  //    마지막까지 search 끝나면 j 위치 값과 pivot을 자리 바꿈
  //    1번 방식보다 공간 메모리적인 관점에서 효율적인 방식이다.
  
  public static index partition(index low, index high){
      index i,j,pivotPoint;
      keytype pivotItem;
      
      pivotItem=S[low];
      j=low;
      // pivot보다 작은 값을 찾으면 j 다음 인덱스 값과 자리 바꿈
      for(i=low+1; i<=high; i++){
          if(S[i]<pivotItem)
              exchange S[i] and S[++j];
      }
      // 마지막까지 search 끝나면 j 위치 값과 pivot을 자리 바꿈
      pivotPoint=j;
      exchange S[low] and S[pivotPoint];
      
      // pivot의 현 위치
      return pivotPoint;
  }
  ```
  
  ![image](https://user-images.githubusercontent.com/59719632/160317070-bd14af04-9026-49de-9069-dacc1f32cd0b.png)

  - Every Case Time Complexity of Partition
    + Basic Operation: pivot과 다른 값의 비교 연산
    + Input Size: high-low+1 => subarray의 item 갯수
  - Worst Case Time Complexity of QuickSort
    + Basic Operation: 동일한 입력 크기를 받아도 비교 횟수가 다를 수 있다. partition의 비교 연산
    + Input Size: 정렬해야하는 전체 array의 크기
    + Worst case는 우리가 원하는 정렬로 이미 정렬되어 있을 때 발생한다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160325585-5820d5fd-07e1-4323-b532-fc2985833a06.png)

    ![image](https://user-images.githubusercontent.com/59719632/160325934-66bde161-1971-467e-8eff-f9a22c4ec2cc.png)

  - 오름차순이 최악이라는 것에 대한 엄밀한 증명 (수학적 귀납법) W(n) <= n(n-1)/2
    + Induction Base: n=0 일때, W(0) = 0 <= 0(0-1)/2    
    + Induction Hypothesis: W(k) <= k(k-1)/2, 0<=k\<n 이라 가정
    + Induction Step: From the algorithm, W(n)=W(p-1)+W(n-p)+n-1, p가 pivotPoint
    + Induction Hypothesis로부터 W(n) <= (p-1)(p-2)/2 + (n-p)(n-p-1)/2 + n - 1
    + n(n-1)/2 - (p-1)(p-2)/2 + (n-p)(n-p-1)/2 + n - 1 = (n-p)(p-1) >= 0
    + 따라서 W(n) <= n(n-1)/2
    
  - Average Case Time Complexity of QuickSort
    + Basic Operation: 비교 연산
    + Input Size: Array의 크기
    + pivotPoint의 위치 i의 확률 p_i (1<=i<=n)
    + p_i = 1/n
    
    ![image](https://user-images.githubusercontent.com/59719632/160326983-cf56bf07-d7e4-4060-a85a-8d6d4ea0e653.png)

    ![image](https://user-images.githubusercontent.com/59719632/160328091-7e56f4cd-f54e-4302-a49c-82c75c03e5a7.png)

    ![image](https://user-images.githubusercontent.com/59719632/160329201-571e6b1c-51d3-401b-83ed-af64f87d48c0.png)

    ![image](https://user-images.githubusercontent.com/59719632/160329464-50893669-f9e1-4078-8adc-fff05ca196dc.png)

## 2-4. Solving Recurrence Relations

* Homogeneous Linear Recurrence Relations
  - 각 벡테의 계수를 r^k 꼴로 표현
  - 먼저 선형 식에 대한 characteristic equation을 만든다.
  - k개의 서로 다른 근이 있는 경우
    + 일반 식에 대한 일반항 t_n은 r_i에 상수 곱한 꼴로 표현된다.
    + 조합론에서 이미 보여진 결과를 우리는 가져다 사용한다.

    ![image](https://user-images.githubusercontent.com/59719632/161502993-c2451d96-a241-4a1f-a919-79d817996d1f.png)

    ![image](https://user-images.githubusercontent.com/59719632/161503613-58c9e8b2-3629-40d7-9ec6-d42e061b3fb2.png)



  - 중근이 몇개 있는 경우
    + k개의 근이 모두가 서로 다르지는 않은 경우
    + t_n은 위 식과 같이 표현되는데 중간에 빨간색으로 중근에 대한 표현이 추가된다.
    + 중복 개수에 따라 앞에 n을 곱해준다.

    ![image](https://user-images.githubusercontent.com/59719632/161503115-d8990cf5-5f76-4fe0-831c-a6314cde4148.png)

    ![image](https://user-images.githubusercontent.com/59719632/161505168-67beaba6-60b5-4ac8-b51c-ad3252b37120.png)

* Nonhomogeneous Linear Recurrence Relations
  - 특정한 모양일 때 푸는 방법
  
    ![image](https://user-images.githubusercontent.com/59719632/161505521-344b14c5-c03f-4acb-9386-b66ccd7028af.png)

    + 여기서 d는 p(n)이 n에 대한 다항식인데 n의 최고차항의 차수 (degree)이다.
    
    ![image](https://user-images.githubusercontent.com/59719632/161506040-073daf51-13fa-479c-8c9a-7eba27c7637e.png)

    + b와 c가 서로 다르다고 가정
    + 특성 방정식을 먼저 구한다.
    + t3는 c로부터 얻을 수 있는 일반해이다.

  - MergeSort Worst Case
    
    ![image](https://user-images.githubusercontent.com/59719632/161509318-62b3e623-526a-44c5-b0cb-67a4c8593f7f.png)
    
    + T_k의 일반항을 구한 후 n에 1부터 대입하면서 연립 방정식을 풀어준다.

    ![image](https://user-images.githubusercontent.com/59719632/161510291-daeb4bca-2e46-4c6b-be13-9ee485395a0d.png)
