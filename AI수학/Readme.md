AI 수학
======
시험 자료 정리
----------

# Chap 1. 선형대수의 기본 요소
## 1-1. Scalar
* 스칼라
  - 크기만으로 나타낼 수 있는 물리량
  - 길이, 넓이, 질량, 온도
  - 데이터 분석 할 때 column을 feature, row를 record라고 한다.
  - 변수에 스칼라 정의(수식)
    + x=3, x=2
  - 기하학적 정의
    + 한 점
  ![스크린샷 2022-03-09 오후 1 00 37](https://user-images.githubusercontent.com/59719632/157370314-1ad00d5b-5a2c-48c5-bbbb-7d254307feea.png)
  
  - 기본 연산
  
<img width="726" alt="스크린샷 2022-03-09 오후 1 02 04" src="https://user-images.githubusercontent.com/59719632/157370426-5dbe298e-afed-433b-8ab1-622c9f2badb6.png">

## 1-2. Vector
* 스칼라의 집합이며, 행렬을 구성하는 기본 단위
  - 모든 n차원 벡터 전체의 집합을 n\-공간 R^n으로 나타낸다.
    + R^n={(x1,x2,...,xn)}
* 크기와 방향을 모두 나타내는 개념
* 열 벡터 (column vector) : 열 방향으로 나열한 벡터 (기본 값), 가로로 나열된 벡터는 기본적으로 열 벡터로 생각한다.
* 행 벡터 (row vector) : 행 방향으로 나열한 벡터
* 영 벡터 (zero vector) : 크기가 0인 벡터, 벡터의 시작 지점과 종료 지점이 동일
* 마이너스 부호가 붙은 벡터 : 방향이 정반대인 벡터
* 기본 연산
  - 벡터의 덧셈과 뺄셈 : 두 벡터의 차원이 동일할 때만 가능
  - 벡터의 스칼라 곱 : 벡터의 길이와 방향을 바꿀 수 있는 방법
    + 스칼라 부호 : 방향
    + 1보다 작은 양수 : 크기 감소
    + 1보다 큰 양수 : 크기 확대
  - 기본 연산의 성질

![스크린샷 2022-03-09 오후 1 40 42](https://user-images.githubusercontent.com/59719632/157374057-dd85410d-5903-4e34-92a0-5ceec78acf1f.png)

## 1-3. Matrix
* 행과 열로 구성
  - 행렬 : 행 벡터의 집합 또는 열 벡터의 집합
  - 사각형 형태로 숫자를 나열 (**A** mxn 행렬), m은 행 벡터 입장에서 본 행 벡터의 갯수, n은 열 벡터 입장에서 본 열 벡터의 갯수
 
![스크린샷 2022-03-09 오후 1 48 14](https://user-images.githubusercontent.com/59719632/157374830-240abd30-7ead-46b5-880b-fee17f6f1e90.png)

* 행렬을 구성하는 스칼라 값 : 원소(element)
  - 데이터 분석 시 데이터 셋을 구성하는 숫자의 집합

![스크린샷 2022-03-09 오후 1 50 03](https://user-images.githubusercontent.com/59719632/157375019-18a09393-52e3-4d94-9d00-d5a387c2d5dd.png)

* 행 벡터 : 열 벡터의 Transpose

![스크린샷 2022-03-09 오후 1 51 01](https://user-images.githubusercontent.com/59719632/157375106-3ed6a22b-5729-46f3-b2ce-5f80e9de038f.png)

* 행렬의 기본 연산
  - 행렬의 덧셈과 뺄셈 : 행렬의 크기가 동일한 경우 연산이 가능
  - 행렬의 스칼라 곱 : 벡터의 스칼라 곱과 동일
  - 행렬의 원소 곱 (matrix element multiplication) : 크기가 동일한 두 행렬에서 동일한 위치의 원소 곱

  ![스크린샷 2022-03-09 오후 1 54 30](https://user-images.githubusercontent.com/59719632/157375478-d148e344-4451-45b0-a1ea-27c52e6f881b.png)

  - 행렬의 곱 (matrix multiplication) : 곱하는 행렬의 열 크기와 곱해지는 행렬의 행 크기가 일치하여야 함 
    + 행렬 곱의 교환법칙은 성립하지 않는다.
   
  ![스크린샷 2022-03-09 오후 1 57 16](https://user-images.githubusercontent.com/59719632/157375763-f4fbc18c-4400-4fab-b2a0-6266af8349e7.png)

  <img width="687" alt="스크린샷 2022-03-09 오후 2 00 31" src="https://user-images.githubusercontent.com/59719632/157376108-b34b2d3d-5375-4713-a4d5-f5ceefe30d6a.png">
  
  - 행렬의 대각합 (trace) : 행렬 A가 정사각행렬일 때, 주대각원소를 모두 더한 값
  
  <img width="321" alt="스크린샷 2022-03-09 오후 2 04 37" src="https://user-images.githubusercontent.com/59719632/157376460-352bcf70-2f02-414c-bcea-21406226c9d5.png">

  - 행렬 연산의 성질

<p align="center">
<img width="380" alt="스크린샷 2022-03-09 오후 2 05 49" src="https://user-images.githubusercontent.com/59719632/157376615-d07f5a54-34f7-4786-a870-96542c9a30f0.png">
<img width="380" alt="스크린샷 2022-03-09 오후 2 05 54" src="https://user-images.githubusercontent.com/59719632/157376627-d2d42eb7-ce1b-4032-bf11-44a80e83cea7.png">
</p>


## Python (numpy)

```python3
import numpy as np

# 스칼라 정의 
x=4 
y=2
# 스칼라 연산 
add_xy = x + y 
subt_xy = x - y 
mul_xy = x * y 
div_xy = x / y

print(add_xy)
print(subt_xy)
print(mul_xy)
print(int(div_xy))

# 벡터 정의
u = np.array([1,2,4]) 
v = np.array([7,3,2]) 
k = 3
print(u, v)
print(u.shape)

# 벡터 연산 
add_uv = u + v 
subt_uv = u - v 
mul_ku = k * u 
mul_uv = u * v 
div_uv = u / v

print(add_uv)
print(subt_uv)
print(mul_ku)
print(mul_uv)
print(div_uv)
```

```python3
import numpy as np

# 행렬 정의
A = np.array([[2,7], [3,4], [6,1]])
B = np.array([[1,4], [4,-1], [2,5]])
C = np.array([[3,-3,5], [-1,2,-1]])
k=3

print(A)
print(B)
print(C)
print(A.shape)

# 행렬 연산
add_AB = A + B
subt_AB = A - B
mul_kA = k * A
mul_AB = np.multiply(A, B) # 원소 곱
matmul_AC = np.matmul(A, C)

print(add_AB)
print(subt_AB)
print(mul_kA)
print(mul_AB)
print(matmul_AC)
```
