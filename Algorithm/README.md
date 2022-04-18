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

* Solving by Substitution (치환)
  - QuickSort Average Case
    
    ![image](https://user-images.githubusercontent.com/59719632/161710900-d033c6de-fa39-4348-9f9e-8e19e36e3212.png)

    + 적분을 사용한 값, 1/x, 샌드위치 정리
        
    ![image](https://user-images.githubusercontent.com/59719632/161711574-efc6a9b3-416d-4dff-b7d8-5400177a3be6.png)

    ![image](https://user-images.githubusercontent.com/59719632/161711980-89e67fd4-217c-4cd2-9a78-a36de16cd3e2.png)

## 2-5. Detrmining Thresholds
* MergeSort와 QuickSort를 Recursive로 구현할 때 발생하는 overhead
  - Mid를 분할하는 시간
  - Recursive calls를 할 때 시스템 내부적으로 stack에서 activation하는 연산
  - 두 subarray를 merge하는 시간
  - 위 경우들을 고려했을 때 n이 작으면 Exchange sort (O(n^2))같은 알고리즘이 더 빠를 수 있다.
  - threshold보다 작은 값에서는 exchange sort를 실행하고 threshold보다 큰 값에서는 mergesort를 실행
  
  ![image](https://user-images.githubusercontent.com/59719632/161713697-9765e661-7cd3-4a29-be57-9375f27949eb.png)

  - 내부적으로 Exchange sort를 하는 Modified MergeSort
    + threshold t 보다 작을 때는 exchange sort, t 보다 클 때는 Mergesort
   
    ![image](https://user-images.githubusercontent.com/59719632/161719008-0fab92b7-4991-4df6-a924-fa77d003b31a.png)

    ![image](https://user-images.githubusercontent.com/59719632/161719368-a2bd2ce5-0bc6-459a-86b1-dc3b73b99eb1.png)

## 2-8. Divide and Conquer 사용하면 안되는 경우
* Size가 n인 instance를 분할 할 때 분할된 instance 크기가 n과 거의 비슷하게 분할되는 경우
  - Recursive Fibonacci (linear로 구현한 것보다 훨씬 비효율적)
  
  ![image](https://user-images.githubusercontent.com/59719632/161720123-cd662b82-7723-4a92-9aae-842455e9765f.png)

  
* Size가 n인 instance를 분할 할 때 분할된 instance 크기가 n/c인데 n과 거의 비슷한 경우
  
  ![image](https://user-images.githubusercontent.com/59719632/161720768-732c48dc-38f1-4623-bc45-86af5de3fb36.png)

  - 이 경우 Divide and Conquer로 하면 비효율적인 알고리즘이 됨
  
  
# Chap 3. Dynamic Programming
## 3. Dynamic Programming
* Similar to Divide and Conquer
  - 작은 instances로 분할
* Different from Divide and Conquer
  - 작은 instances를 먼저 해결하고 나중에 필요할 때 꺼내서 씀
  - Iterative Fibonacci
* Dynamic Programming 은 Bottom\-Up 방식이다
  - Divide and Conquer은 Top\-Down 방식이다.

* Step
  - Step 1:
    + 문제 instance의 해가 큰 문제의 해에 어떻게 활용이 되는지 파악
    + 알고리즘을 작성하기 전에 먼저 수행되어야 한다.

  - Step 2:
    + 작은 문제에 대한 해를 구하고 이를 통해 큰 문제의 해를 구한다.
    + bottom up

## 3-1. The Binomial Coefficient (이항 계수)
* nCk

![image](https://user-images.githubusercontent.com/59719632/161737853-0548bb0e-e15b-4cf4-be4d-9b50061d1c8d.png)

* Divide and Conquer를 이용한 Binomial Coefficient (재귀 호출 과정에서 연산 수가 굉장히 많아짐)

![image](https://user-images.githubusercontent.com/59719632/161738228-6ef7da82-cc61-484b-b539-ce3bbecc254f.png)

* Dynamic Programming을 이용한 Binomial Coefficient
  - 필요한 값에 대한 부분만 채워져있으면 됌
  
  ![image](https://user-images.githubusercontent.com/59719632/161739136-55222466-1ea1-47ec-aebd-a7ad23111553.png)

  ![image](https://user-images.githubusercontent.com/59719632/161739535-d581f069-b9b6-4c41-98f9-bbcb48d12621.png)

  - i<=k 까지는 연산 횟수가 i+1이고 i>k이면 min(i,k)가 k로 고정되기 때문에 연산 횟수가 k+1로 고정된다.
  
  ![image](https://user-images.githubusercontent.com/59719632/161740100-984f1009-60e6-4a2e-8d18-0b7f377dddfd.png)

  - 연산 횟수를 모두 더함
  
  ![image](https://user-images.githubusercontent.com/59719632/161740585-c10eb270-3303-4ce9-bf9e-d2383d0471f7.png)

## 3-2. Floyd's Algorithm for Shortest Paths
* The Shortest Paths Problem
  - 그래프의 모든 vertices 사이의 Shortest Paths를 찾는 것
  - 최단 경로가 여러 개라면 이 중 하나를 찾는 것
  - An exhaustive algorithm (전수조사, 매우 비효율적)
    + 시간복잡도를 구해보면 최소한 O(n!) 이다.
    + P(n-2,k), k는 v_i, v_j 사이에 거치는 vertices 개수 
    
    ![image](https://user-images.githubusercontent.com/59719632/161742929-b371288a-9686-45fd-bdbe-a13d39e489e8.png)

* Floyd's Algorithm
  - 가중치 nxn table W 을 n nodes graph에 적용
  - edge가 없는 것은 infinite 값으로 적용해서 없는 값으로 표현
  
  ![image](https://user-images.githubusercontent.com/59719632/161743400-ff96a266-bbe2-4f57-9fac-8f9a72446ae5.png)

  - 관계식 수립
    + vertex를 하나 더 늘려줬을 때와 안 늘렸을 때의 관계
    + D^(k)[i]\[j] 의미는 v_i에서 v_j를 가는데 v_1,v_2,..,v_k 까지만 거쳐서 얻을 수 있는 최단 경로의 길이
    
    ![image](https://user-images.githubusercontent.com/59719632/161746749-710bdb11-b65c-4ff6-b38c-9ea3ef2f1b2e.png)

    + Case 1: v_i에서 v_j로 가는데 v_k를 사용하지 않고도 최단 경로 방법이 있는 경우

    ![image](https://user-images.githubusercontent.com/59719632/161747400-12dd77c0-9782-4836-84a9-37a67857d8b2.png)

    + Case 2: v_k를 반드시 포함해야 최단 경로가 되는 경우

    ![image](https://user-images.githubusercontent.com/59719632/161747695-e2152576-b536-4a26-8ac5-9fc97fec1221.png)

    + 사실 Case를 따로 구분할 필요가 없다. 어떠한 경우든 짧은 쪽을 선택하면 된다.

    ![image](https://user-images.githubusercontent.com/59719632/161748021-fb83098c-6e36-43d3-88a9-7d4cdfd45404.png)

    + 3차원 배열로 구현, 굳이 3차원을 사용할 필요는 없다. 바로 전 층만 기억하게 하면 됀다. => 2차원 배열로 표현 할 수 있음 (계속 업데이트 하는 방식)
    
    ![image](https://user-images.githubusercontent.com/59719632/161748513-cd46e6d8-fda1-448b-929e-049ddbce9c04.png)
  
    ![image](https://user-images.githubusercontent.com/59719632/161749166-c2c3f369-94d7-43b9-8af6-9fd97ff166c1.png)

    + 최단 경로의 길이를 통해 노드의 순서를 구하는 과정, 위의 min 부분을 if문으로 바꾼 다음 if문 안에 조건을 만족하는 가장 큰 k 값을 기억시켜줌 
    
    ![image](https://user-images.githubusercontent.com/59719632/161749763-20853edb-711a-4f19-85a3-6207aa8ed313.png)

    + 최단 경로를 출력하는 함수, P[q]\[r]이 0이면 중간에 거치는 vertex가 없다는 의미, V_P[q]\[r] 까지 출력 1번, V_P[q]\[r]에서 V_r 까지 출력 1번
    
    ![image](https://user-images.githubusercontent.com/59719632/161750164-c7be0e12-ae18-4789-8b56-157956624e7c.png)

## 3-3. Dynamic Programming and Optimization Problem
* Principle of Optimality
  - 어떤 Instance의 optimal solution을 찾았을 때 모든 subinstances의 optimal solutions를 포함하고 있어야한다.
  - Principle of Optimality가 성립해야 Dynamic Programming을 사용할 수 있다.
  - 반례: Longest Simple Path Problem
    + Principle of Optimality가 성립하지 않는다.
    + subinstance의 optimal solution을 포함하지 않기 때문
    
  <img width="656" alt="image" src="https://user-images.githubusercontent.com/59719632/162564372-e78577f5-6fbb-46e2-94b5-a1d9aed606fc.png">

## 3-5. Optimal Binary Search Trees
* Binary Search Tree
  - Definition:
    + 각 노드가 하나의 key를 가진다
    + 어떤 노드의 left subtree에 있는 keys는 그 노드의 key 값보다 작거나 같다
    + 어떤 노드의 right subtree에 있는 keys는 그 노드의 key 값보다 크거나 같다
    
    <img width="643" alt="image" src="https://user-images.githubusercontent.com/59719632/162564541-bfb917fb-e3dd-4ce6-bc41-f7f0f341d1fd.png">

    <img width="649" alt="image" src="https://user-images.githubusercontent.com/59719632/162564926-310546ac-efce-4cbd-a528-8fba6304f48b.png">

  - Binary Search Tree Algorithm
    + 평균 비교횟수를 최소화
    
    <img width="598" alt="image" src="https://user-images.githubusercontent.com/59719632/162565240-3953d702-0c50-4783-8d4d-9e5544912ac9.png">

    + 검색 key로 사용될 확률이 높은 key를 위에 두면 평균적인 비교 횟수를 줄일 수 있다.
    + 경우의 수가 많아지면 다 따져보지 않고 Dynamic Programming 방식을 사용한다.
  
    <img width="677" alt="image" src="https://user-images.githubusercontent.com/59719632/162565299-fc8a5f7b-b893-4759-b585-193d1279d363.png">


  - n개의 노드로 Binary Search tree를 만들 수 있는 방법은 최소한 n의 exponential이 된다
    + 깊이가 가장 깊은 tree는 n-1이 된다. 이러한 모양을 갖는 경우의 수는 2^(n-1)가지 이다. (노드당 왼쪽 오른쪽 선택) 이 방법은 2^(n-1) 보다 많은 연산을 해야하기 때문에 지양한다.
  - Dynamic Programming Approach
    + 비교 횟수의 최소값을 A[i]\[j]에 저장
    + 전체 n개의 key를 모두 저장할 수 있는 optimal binary search tree를 찾음
    + 루트 node를 뭐로 할거냐에 따라 optimal solution이 나오고 이를 최종 solution으로 택하면 된다.

    <img width="639" alt="image" src="https://user-images.githubusercontent.com/59719632/162566166-c809b318-e054-4b17-ab6a-cfc46027a387.png">

    + key_k가 루트 노드인 경우
    
    <img width="644" alt="스크린샷 2022-04-09 오후 6 36 33" src="https://user-images.githubusercontent.com/59719632/162566256-9392f7f5-19b7-4ae2-b59c-4d2d02860eea.png">

    <img width="663" alt="image" src="https://user-images.githubusercontent.com/59719632/162566316-32aa8046-35cc-4d94-ba4f-44e0d6893a6a.png">

    <img width="656" alt="image" src="https://user-images.githubusercontent.com/59719632/162566395-8b695832-d113-40f6-8ae0-03cf507f10e7.png">
 
    <img width="588" alt="image" src="https://user-images.githubusercontent.com/59719632/162568453-85f0a578-4b02-4c63-887e-20c24e5dc2e1.png">

    + 초기값 설정
    + 구하려는 위치의 값을 알기 위해선 먼저 알아야하는 값들이 있다.
    + 초기 설정한 값을 통해 알 수 있는 값을 먼저 계산하고 이를 통해 차례로 계산한다.
 
    <img width="649" alt="image" src="https://user-images.githubusercontent.com/59719632/162568675-027ebf43-028c-4188-b73c-aee98821e412.png">

    + R은 A의 값이 저장될 때마다 해당하는 루트에 어떤 key가 와야하는지 저장하는 배열
    + 나중에 분석할 때는 A[i]\[j]의 min 부분을 구하는 것도 일종의 Loop이기 때문에 고려를 해줘야 한다.
    

 
    <img width="660" alt="스크린샷 2022-04-09 오후 7 53 51" src="https://user-images.githubusercontent.com/59719632/162568875-674d4e66-3d79-4e6e-8c69-405d7bb42835.png">

  - Dynamic Programming Approach
    + Basic Operation: the instructions executed for each value of k (여기서는 min 함수)
    + Input Size: n, number of keys

  <img width="657" alt="image" src="https://user-images.githubusercontent.com/59719632/162568984-16d8aa96-12e0-41fa-82a8-43b60f932833.png">
  
  - Building an Optimal Bianry Search Tree
    
  <img width="651" alt="image" src="https://user-images.githubusercontent.com/59719632/162569056-69d16a52-434a-4988-95ee-4561dc06fd91.png">

    
## 3-6. Traveling SalesPerson Problem (외판원 문제)
* Dynamic Programming Approach
  - V1에서 시작한다고 가정
  - 노란색 노드를 다르게 하면서 남아있는 노드들을 최단으로 통과해서 v1으로 가는 방법을 재귀적으로 찾음
  - 파란색 edge들의 길이의 합 (v_i에서 v1까지 가는 edges) : D[v_i]\[A]에 저장
  
  <img width="648" alt="image" src="https://user-images.githubusercontent.com/59719632/162608991-e4080650-8702-4d60-b834-f09de60cb6a0.png">

  - Optimal tour의 길이
    + W[1]\[j] 값은 v1에서 vj로 가는 edge 길이 그대로 사용하면 됨
    + Vj에서 방문하지 않은 노드들을 한번 씩 방문해서 v1으로 가는 길이: D
    
    <img width="626" alt="image" src="https://user-images.githubusercontent.com/59719632/162610183-cf3e9ebe-47b7-477e-82d7-ff6603e1cba5.png">

    <img width="619" alt="image" src="https://user-images.githubusercontent.com/59719632/162610285-6c1ff923-cc31-4455-b9a4-fc6ff13ae529.png">

    <img width="627" alt="image" src="https://user-images.githubusercontent.com/59719632/162610441-3a6fd8bc-9208-45f1-84ee-0fb881533285.png">

    <img width="596" alt="image" src="https://user-images.githubusercontent.com/59719632/162610482-bbaa7aac-cfa3-4536-9a48-77f4360adeaa.png">

    <img width="595" alt="image" src="https://user-images.githubusercontent.com/59719632/162610555-5144589f-b051-4360-9b0f-4f58c9793085.png">

    <img width="604" alt="image" src="https://user-images.githubusercontent.com/59719632/162610568-d4f46569-dfdf-4546-91c9-b22fb1b7e594.png">
    
    <img width="603" alt="image" src="https://user-images.githubusercontent.com/59719632/162610632-b8430b30-fc9c-40fc-95a7-a0049ba2dd86.png">

    <img width="578" alt="image" src="https://user-images.githubusercontent.com/59719632/162610795-f77e1641-bad1-4dd0-8243-a88fbea662ef.png">

  - Time Complexity Analysis
    + Basic Operation: the instructions executed for each vertices (min 안의 더하기 연산)
    + Input Size: n, number of vetices

    <img width="649" alt="image" src="https://user-images.githubusercontent.com/59719632/162611032-8a957a91-7bd5-4f21-822d-ca2fc99cfa22.png">

    <img width="621" alt="image" src="https://user-images.githubusercontent.com/59719632/162611459-8a7c6a62-4313-4eca-acaf-160b6997f957.png">

    <img width="587" alt="image" src="https://user-images.githubusercontent.com/59719632/162611520-aacb62d7-ab95-4c91-a2b6-acb4b9829603.png">
 
    
  - Memory Complexity Analysis
  
  <img width="553" alt="image" src="https://user-images.githubusercontent.com/59719632/162611603-5eb52400-e405-4e59-8c6f-87111d8348bb.png">

  - 앞서 나온 Dynamic Programming 방식과는 조금 다르다.
    + n에대한 다항식의 Time complexity가 아님
    + 아직까지 n에 대한 다항식으로 TSP를 만든 사람이 없다.
    
# Chap 4. Greedy Algorithm
* 일련의 선택을 할때 그 순간에 가장 좋아보이는 것을 선택하는 방법
* solution set에 넣으면 끝까지 사용
* 항상 최적을 보장하진 않음

![image](https://user-images.githubusercontent.com/59719632/163523754-cdaa5588-c529-4e00-af2c-5cc3f84fece1.png)

![image](https://user-images.githubusercontent.com/59719632/163523918-f3db841e-ddff-44ec-bebb-c8517773ea30.png)

## 4-1. Minimum Spanning Trees
* Definitions
  - Unbdirected Graph
    + 그래프의 edges가 방향성이 없는 그래프
  - Connected Graph
    + 어떤 vertices pair를 고르더라도 그 둘 사이의 path가 존재하는 그래프
  - Acyclic Graph
    + cycle이 없는 graph => 자신에게 다시 돌아오는 경로가 존재하지 않는 그래프
  - Tree
    + acyclic, connected, undirected graph

  - Spanning Tree for undirected graph
    + 원래 있는 그래프의 모든 정점들을 가지고 있는 부분 그래프, tree 형태
  - Minimum Spanning Tree for undirected graph
    + spanning tree의 가중치의 합이 최소인 tree
    
  ![image](https://user-images.githubusercontent.com/59719632/163524243-3894cc8a-7cd4-47fb-bdca-11d5df66d251.png)

  ![image](https://user-images.githubusercontent.com/59719632/163524848-95b48147-1117-4ed8-98af-96c18930a33e.png)

* Prim's Algorithm
  - 시작 노드에서 가중치가 가장 짧은 것을 선택하면서 탐색
  
  ![image](https://user-images.githubusercontent.com/59719632/163525122-ad9be5f7-b7cc-4f5d-b085-629e0b2fb299.png)

  ![image](https://user-images.githubusercontent.com/59719632/163525162-bcc1f2d2-cecb-43ff-bdb1-532f792f6bd3.png)

  - 구현
    
  ![image](https://user-images.githubusercontent.com/59719632/163525569-88eee7ab-12d2-4777-9d16-83890e4fceee.png)
  
  ![image](https://user-images.githubusercontent.com/59719632/163525605-ec024544-fe13-4202-827f-1d6e2bcb4458.png)

  ![image](https://user-images.githubusercontent.com/59719632/163529155-75fefcf2-def6-4544-947a-11e25fdc40fd.png)

  ![image](https://user-images.githubusercontent.com/59719632/163529556-c60ec949-fa34-46f8-814a-29f105c0ee90.png)

  ![image](https://user-images.githubusercontent.com/59719632/163529868-c50d81cf-06d0-40fb-8667-d0f58857edc4.png)

  ![image](https://user-images.githubusercontent.com/59719632/163529799-772d3370-7f1a-43e3-a9a4-8e4c54cdfc9c.png)

  ![image](https://user-images.githubusercontent.com/59719632/163530306-d6b4e572-1777-4cc6-91de-a540949e88c2.png)

  ![image](https://user-images.githubusercontent.com/59719632/163530323-d8eacebb-3352-4b1c-832d-77580b396814.png)

  ![image](https://user-images.githubusercontent.com/59719632/163530351-c6d3550c-6acd-48ff-9a3f-622db232df98.png)

  ![image](https://user-images.githubusercontent.com/59719632/163530388-dbd69dfc-1175-43c2-9cdf-767a40f5303e.png)

  ![image](https://user-images.githubusercontent.com/59719632/163530421-0e79123c-dcb3-4591-8ccc-e56c9c30829f.png)

* Kruskal's Algorithm

![image](https://user-images.githubusercontent.com/59719632/163572012-2cf42f4d-9050-4290-8ed4-fa4a5dbba607.png)

![image](https://user-images.githubusercontent.com/59719632/163572049-da2f476d-1044-4c0a-a999-8ca2212d9f5b.png)

![image](https://user-images.githubusercontent.com/59719632/163572061-ffe44221-112e-414b-b571-590ce29678e8.png)

![image](https://user-images.githubusercontent.com/59719632/163572071-9af9c0aa-afe5-4801-80a7-5cfba0f45bbe.png)

* Disjoint sets as forest

![image](https://user-images.githubusercontent.com/59719632/163572133-e159bee9-f7c5-443b-9982-71c16e1d575d.png)

![image](https://user-images.githubusercontent.com/59719632/163572149-a047b975-7ebe-4654-ba47-7bdbce049669.png)

![image](https://user-images.githubusercontent.com/59719632/163572175-543d8649-93f0-4587-844d-2a23907107c1.png)

![image](https://user-images.githubusercontent.com/59719632/163572202-b10dfe9a-6754-45f1-b24a-4378e2ab560b.png)

![image](https://user-images.githubusercontent.com/59719632/163572243-2c282649-ca0f-461b-84a9-0d8974c95682.png)

![image](https://user-images.githubusercontent.com/59719632/163572261-8a5a8fa1-cdc7-40a4-8498-0991be441c92.png)

![image](https://user-images.githubusercontent.com/59719632/163572280-7cf69d14-4e1b-49d7-9b48-2c6622039074.png)

![image](https://user-images.githubusercontent.com/59719632/163572296-6b512274-eb48-4556-a58a-0d26d4d6bffa.png)

![image](https://user-images.githubusercontent.com/59719632/163572322-1f29598c-7c7b-42c2-9301-47dbc9aeb9be.png)

![image](https://user-images.githubusercontent.com/59719632/163572346-637cbe07-9ccb-4c33-98d2-e8fcf61121f7.png)

![image](https://user-images.githubusercontent.com/59719632/163572363-f80c83d4-7701-4a1a-8ae3-7859f8f38aa3.png)

![image](https://user-images.githubusercontent.com/59719632/163572384-155472b7-994c-404b-817c-b2869e952446.png)

![image](https://user-images.githubusercontent.com/59719632/163572409-41a1eefa-39e3-484c-a63b-85fcb817487d.png)

## 4-4. Huffman Code

* Huyffman Code

  ![image](https://user-images.githubusercontent.com/59719632/163572766-177b5c59-ff2e-4551-8a00-1167ccd53ed9.png)

  - 고정길이 vs 가변길이 이진 코드
    + 가변길이 이진코드 사용하면 전체 비트 수를 줄일 수 있다.
    + String에 자주 나타나는 character들에 대해 적은 비트 수의 코드를 부여하기 때문이다.
  
  ![image](https://user-images.githubusercontent.com/59719632/163856396-18fc7eed-89a5-4567-bbee-6122505b125c.png)

  - Prefix Code  
    + 어떠한 글자에 대한 코드도 다른 코드의 시작 부분이 되지 않는 Code
    + 루트 node로부터 해당 node 까지의 값을 이어서 쓰면 해당 node의 이진 코드가 된다.
    
  ![image](https://user-images.githubusercontent.com/59719632/163856656-f93b8e54-473b-4c7b-96fb-a3636f4abd67.png)


  - 총 비트 수 계산
  
  ![image](https://user-images.githubusercontent.com/59719632/163856916-5828be5f-4057-4ef0-9b68-f14922da4c61.png)

  ![image](https://user-images.githubusercontent.com/59719632/163857079-30ef87fd-f88b-42c0-9834-0042730dbd1a.png)

  - code 3가 허프만 코드
  
  ![image](https://user-images.githubusercontent.com/59719632/163857128-a4b911e7-51e0-4d18-9c5d-d7572097485f.png)

  - Huffman's Algorithm
    + n개의 single-node tree를 만든다.
    + 각각 글자의 빈도가 제일 작은 값을 tree들을 merge 반복\
    + 하나의 tree로 만들어질 때까지 반복
    
    ![image](https://user-images.githubusercontent.com/59719632/163858097-1ebff1f3-cf50-4158-b558-c13538880881.png)

    + priority는 frequency가 결정. priority가 높다는 것은 frequency가 낮은 것
    + frequency가 낮은 것부터 remove
    + priority queue를 주로 heap으로 구현한다. => 깊이가 log n 에 해당하는 일을 함
    
    ![image](https://user-images.githubusercontent.com/59719632/163858653-6f4a6ebb-1e8c-45cb-8d72-32dd4dd2c9a1.png)

    ![image](https://user-images.githubusercontent.com/59719632/163858692-6f240376-9e3d-4816-b0de-a8bb6e1de2ea.png)

  - Optimality of Huffman's Algorithm 증명 (수학적 귀납법)
  
    ![image](https://user-images.githubusercontent.com/59719632/163858875-7a352168-3958-4df5-93ba-c701e762c7cd.png)

    + optimal tree의 왼쪽과 오른쪽을 바꾸더라도 모양은 달라지지만 여전히 optimal tree 이다. (증명 없이 넘어감)
    + sibling 끼리 바꾸는 경우
    
    ![image](https://user-images.githubusercontent.com/59719632/163859810-d7e7ceb5-54b5-4b2d-9f54-56823175e0ad.png)

    + 같은 depth의 subtree의 위치를 바꿔도 여전히 optimal tree이다.
    
    ![image](https://user-images.githubusercontent.com/59719632/163860024-4e37c629-c16b-4c4b-9b53-fe4424a59873.png)

    + Frequency가 같은 subtree 끼리 위치를 바꿔도 optimal tree를 유지한다. (depth, sibling 등 위치 상관 없이)

    ![image](https://user-images.githubusercontent.com/59719632/163860422-99f75c1e-a6bf-495d-901a-21cb652cc87c.png)


  - Huffman Tree Construction
  
    ![image](https://user-images.githubusercontent.com/59719632/163860742-8a050ce0-734d-4c0e-a34b-22f57d1a00f8.png)

    + Case 1: Optimal Tree T 안에 u,v가 sibling으로 있는 경우
    + 계속 결합해서 나가면 Optimal한 Tree를 만들 수 있다.
    
    ![image](https://user-images.githubusercontent.com/59719632/163871287-0a61b6db-8091-4db1-ac25-8cc668d82e43.png)
    
    + Case 2: Optimal Tree T 안에 u,v의 parent가 다른 경우
    + u의 짝이 되는 w가 존재
    
    ![image](https://user-images.githubusercontent.com/59719632/163871954-3ecee131-5fc0-4baf-90c1-4fa6c1c0e3c9.png)

    ![image](https://user-images.githubusercontent.com/59719632/163872538-28097fe9-384f-4b78-b71a-9b14ef27e168.png)

    ![image](https://user-images.githubusercontent.com/59719632/163873792-d7823d8f-a38b-4f9e-b0c0-722e6c8b1d90.png)
    
## 4-5. KnapSack
* Greedy Approach가 적용이 잘 안되는 예로 Knapsack 소개
  - S의 부분집합 A를 찾는데, A의 item의 weight 합이 knapsack 용량보다 크면 안되고, 이 중 가장 큰 이득을 줄 수 있는 부분집합을 찾는 문제
  - 0\-1 Knapsack Problem: Item을 모두 담거나 모두 담지 않거나. 일부만 담는 것을 허용하지 않는 문제

  ![image](https://user-images.githubusercontent.com/59719632/163877006-dba6c3bc-231b-42fb-8a91-8b2eb93bd41a.png)

  - Brute\-Force Solution to The 0\-1 Knapsack Problem
    + n에 대한 exponential complexity

  - A Simple Greedy Approach
    + Idea: profit 기준 오름차순 정렬된 item => 가장 profit이 큰 item이 큰 weight를 가지면 optimal을 보장하지 않는다.

  - Another Simple Greedy Approach
    + Idea: Weight 기준 오름차순 정렬된 item에서 weight가 작은 것부터 넣어감 => weight가 작은 item이 small profit을 가질 때 optimal이 안됨
     
  - More Sophisticated Greedy Approach
    + Idea: 단위 무게 당 profit의 내림차순 => Optimal한 solution을 찾아주지만 모든 경우의 optimal을 찾아주진 않는다.
    
    ![image](https://user-images.githubusercontent.com/59719632/163884731-7ed5c1b1-fd82-4a57-b604-03a3be4969a8.png)

    ![image](https://user-images.githubusercontent.com/59719632/163884881-ddff58f8-df0a-4fc8-a300-da5f9ebd8537.png)

  - 아직까지 Greedy Approach로 0\-1 Knapsack Problem의 optimal solution을 찾는 방법이 발견되지 않았다.
  - A Greedy Approach to the fractional Knapsack Problem (Item 일부만 택해서 사용)
    + Item을 일부만 사용하고 Profit도 일부만 얻게 허용을 해주면 profit per unit weight으로 Optimal solution을 찾을 수 있다.
    + 증명 생략
* Dynamic Programming Approach to the 0\-1 Knapsack Problem
  - P[i]\[w] 를 i개의 item 사용, w는 남아있는 용량 => n개 중에 첫번째부터 i번째 item까지만 선택했을 때 total weight가 w를 넘지 않는 범위에서 얻을 수 있는 최대 profit
   
  ![image](https://user-images.githubusercontent.com/59719632/163886091-909b33dc-a64f-4e45-bc7e-c91bcdd9d725.png)

  ![image](https://user-images.githubusercontent.com/59719632/163886444-97dac349-27c4-4648-9dea-ec88a1db157a.png)

  ![image](https://user-images.githubusercontent.com/59719632/163886586-a85fa3e9-31d9-45dc-a0b3-f24481f8d899.png)

  - Dynamic Programming 방식으로 접근해도 효율적이진 않다.
  
# Chap 5. Backtracking
## 5-1. The Backtracking Technique
* N\-queens Problem
  - NxN chessboard에서 n개의 queen을 놓는데 서로 공격하지 않도록 놓는 방법을 찾는 문제
  - Sequence: n개의 position을 찾아나가는 것
  - Set: NxN의 chessboard cell
  - Criterion: queen들이 서로 공격하지 않는 것
  - 4 queens problem
    
    ![image](https://user-images.githubusercontent.com/59719632/163887425-b6be7810-e417-4a20-8569-649d9dc2041f.png)

    ![image](https://user-images.githubusercontent.com/59719632/163887446-e1577e76-65b6-4aa8-b2e3-385fd5983b66.png)

    ![image](https://user-images.githubusercontent.com/59719632/163888244-e6834881-4d86-4911-b4c3-9eff3ccfce1a.png)

  
    + Backtracking => Depth\-First\-Search 사용

    ![image](https://user-images.githubusercontent.com/59719632/163888469-6e6e4747-1e85-4416-95ff-471d94f7189d.png)

    ![image](https://user-images.githubusercontent.com/59719632/163888717-c9ece91c-7e4a-421b-94ac-3c0ea3609410.png)

    ![image](https://user-images.githubusercontent.com/59719632/163888868-dd63477f-48a2-4333-a3d9-e310853f10b1.png)

    ![image](https://user-images.githubusercontent.com/59719632/163888893-de9ff9a6-9076-447f-965d-f8215edf957f.png)

    ![image](https://user-images.githubusercontent.com/59719632/163888928-5d047aaa-78f8-400c-8aa8-902562d8e15e.png)
