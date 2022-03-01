Algorithm
=========
전공 자료 정리
----------

# Chap 1. Algorithms: Efficiency, Analysis, and Order
* 챕터 1에서는 알고리즘의 효율성(efficiency)을 다룬다.
* "order" 라는 개념은 알고리즘의 efficiency를 나타낸다.

## 1-1.Some Definitions
* Problem : a question to which we seek an answer.
* Problem Instance : a problem where each parameter is assigned a specific value.
  - ex) Determine whether the number 5 is in the list [10, 7, 11, 5, 13, 8] of 6 numbers.
* Algorithm : 각각의 problem instance을 해결하기 위한 단계별 절차.
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
<img width="547" alt="스크린샷 2022-02-28 오후 7 25 29" src="https://user-images.githubusercontent.com/59719632/155966908-5f7f6041-b5f6-441e-80d4-4dedae6edcf7.png">

* Fibonacci Sequence
<img width="645" alt="스크린샷 2022-02-28 오후 7 27 59" src="https://user-images.githubusercontent.com/59719632/155967348-c210d34b-5a70-43f0-8a52-bae93dfbe282.png">
  - Recursive Algorithm

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
        return 1
    else:
        return fib(n-1)+fib(n-2)
```


<img width="597" alt="스크린샷 2022-02-28 오후 7 30 38" src="https://user-images.githubusercontent.com/59719632/155967711-755dd478-5ca6-4325-9996-8b233a2069b7.png">

  - Iterative Algorithm

```java
// Java
public static int Fib2(int n){
    index i;
    int[] f=new int[n+1];
    
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
  - single number \- 
    + ex) **n**\-th Fibonacci Number
  - Graph에서는 vertices 수와 edges 수 둘 다 input size이다.

* Basic Operation
  - 알고리즘이 실행될 때 기본적으로 실행되는 연산
    + 정렬 또는 탐색 알고리즘의 비교 연산
    + 행렬 곱의 덧셈 연산
* Time Complexity (시간 복잡도)
  - The determination of how many times the basic operation is don for each value of the input size.
    + 순차 탐색 알고리즘의 worst case는 **n**번 비교하는 것이다.

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
  - Non-Every case
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

## 1-4. Order
* Complexity Function
  - any function from. the **non\-negative integers** to the **non\-negative real** numbers
  - ex) n, log n, n^2 + n/2
 
* Complextiy of an Algorithm
  - the complexity function indicating **how many times** the basic operation.

* Linear Time Algorithm
  - O(n)
  - ex) Worst case of Sequential Search with n items.
 
* Quadratic Time Algorithm
  - O(n^2)
  - ex) Average case of Bubble sort with n items.

Input Size가 충분히 클 때 알고리즘이 어떻게 수행되는지 관심이 있다.

<p align="center">
<img width="300" alt="스크린샷 2022-03-01 오후 3 42 45" src="https://user-images.githubusercontent.com/59719632/156118442-8690ad49-72b1-4cb0-b962-cdbeb83570de.png"> <img width="300" alt="스크린샷 2022-03-01 오후 3 42 52" src="https://user-images.githubusercontent.com/59719632/156118462-811714c3-06e9-439a-81ff-53be5f13f56e.png"></p>

<img width="400" alt="스크린샷 2022-03-01 오후 3 43 01" src="https://user-images.githubusercontent.com/59719632/156118639-ca8d14bd-7281-4931-9d2b-a7795f4cf3e5.png">

* **Big O**
  - O(f(n)) is the set of complexity functions g(n)
for which there exists some positive **real constant c** and **some non\-negative integer N**
  - dim g(n) <= dim f(n)

<img width="400" alt="스크린샷 2022-03-01 오후 4 02 14" src="https://user-images.githubusercontent.com/59719632/156120827-fdfd4ff0-ac0e-495a-af01-b4cf222f0d20.png">


* **Omega(Ω)**
  - dim g(n) >= dim f(n)
 
<img width="557" alt="스크린샷 2022-03-01 오후 4 07 00" src="https://user-images.githubusercontent.com/59719632/156121402-010927cc-b505-4fd5-8a12-ea0f7046e18f.png">

* **Theta(θ)**
  - Ω(f(n)) <= dim g(n) <= O(f(n))

<img width="564" alt="스크린샷 2022-03-01 오후 4 08 55" src="https://user-images.githubusercontent.com/59719632/156121659-209c88ed-74b0-432f-902e-306d88a03013.png">

* **small o**
  - O(f(n))과 거의 비슷하지만 small o는 n이 무한대로 커질 때만 사용
  - g(n)의 절대값에 어떤 작은 양의 숫자를 곱해도 f(n)보다는 크게되는 순간이 x를 키우다보면 언젠가는 나타난다.
  - small o가 성립하면 Big O도 성립한다.
 
<img width="161" alt="스크린샷 2022-03-01 오후 4 18 19" src="https://user-images.githubusercontent.com/59719632/156122844-7bd5576f-0d69-40c8-80ce-87cc4d507e5f.png">
  
   - Exponential이 Factorial보다 느리게 증가함 증명
  
<img width="586" alt="스크린샷 2022-03-01 오후 4 25 48" src="https://user-images.githubusercontent.com/59719632/156123933-49408f0e-6155-4486-a2a2-8b7447a960f0.png">

   - 로피탈 정리 이용한 **small o** 증명

<img width="493" alt="스크린샷 2022-03-01 오후 4 25 56" src="https://user-images.githubusercontent.com/59719632/156123950-7ec6d0bc-55ac-4116-bd85-684ee07bfff8.png">


* Properties of Order

<img width="400" alt="스크린샷 2022-03-01 오후 4 22 48" src="https://user-images.githubusercontent.com/59719632/156123481-39116389-d0a4-48bf-ba62-9de2d919f76f.png">

* Using a Limit to Determine Order

<img width="454" alt="스크린샷 2022-03-01 오후 4 23 32" src="https://user-images.githubusercontent.com/59719632/156123545-358a3bf5-21b1-4ca1-b608-a467cb8cb868.png">
