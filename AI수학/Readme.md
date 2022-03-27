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

# Chap 2. 다양한 행렬 및 행렬식
## 2-1. 전치행렬
* 기존 행렬의 행과 열을 바꾼 행렬

 ![스크린샷 2022-03-10 오후 4 50 55](https://user-images.githubusercontent.com/59719632/157613848-9893f077-2b7a-4edb-96ee-a5688ec11fdb.png)

* 전치 행렬의 성질
 
  ![스크린샷 2022-03-10 오후 4 53 20](https://user-images.githubusercontent.com/59719632/157614230-c5578cae-d628-46b0-b1c2-d0916f11196e.png)

## 2-2. 대칭행렬 (Symemetric matrix)
* 기존 행렬과 전치 행렬이 동일한 **정사각행렬** : A = A^T
* 대칭 행렬의 성질
  - 대칭행렬(A,B) 간 덧셈, 뺄셈 결과 : 대칭행렬
  - 대칭행렬(A,B) 간 행렬 곱 : 대칭행렬이 아님
  - 대칭행렬(A)의 거듭제곱(A^n) : 대칭행렬
  - \*\*\* **AA^T, A^TA : 대칭행렬 (A는 대칭행렬일 필요가 없음)**

  ![스크린샷 2022-03-10 오후 5 00 02](https://user-images.githubusercontent.com/59719632/157615276-9915373b-94f8-47a3-9818-488f32349b47.png)

## 2-3. 대각행렬(diagonal matrix, D)
  - 정사각행렬에서 주대각원소를 제외한 나머지 원소가 0인 행렬
  - 대각행렬의 역행렬 및 거듭제곱

  ![스크린샷 2022-03-10 오후 5 01 23](https://user-images.githubusercontent.com/59719632/157615466-0c770577-5464-43a7-adf3-c56221593d71.png)
  
  - 대각행렬의 성질
    + 행렬 A와 대각행렬 D의 행렬곱 AD : 행렬 A의 열이 대각 원소의 배수만큼 변환
    + DA는 행렬 A의 행이 대각 원소의 배수만큼 변환된다.

  <p align="center"><img width="700" alt="스크린샷 2022-03-10 오후 5 03 53" src="https://user-images.githubusercontent.com/59719632/157615895-ffaf2ccf-a4ff-4aba-bf02-ef07791c2ece.png"> <img width="700" alt="스크린샷 2022-03-10 오후 5 04 06" src="https://user-images.githubusercontent.com/59719632/157615900-94e859a5-f961-43be-8104-bd0470527258.png"></p>

## 2-4. 단위행렬(identity matrix, I)
  - 주대각원소가 1인 대각행렬
  - 항등행렬이라고도 한다.

  <img width="500" alt="스크린샷 2022-03-10 오후 5 06 43" src="https://user-images.githubusercontent.com/59719632/157616300-f5826a31-2a86-4fc6-adb0-d0fa33f72b74.png">
  
## 2-5. 영행렬(zero matrix, 0)
  - 모든 행렬 구성 원소가 0인 행렬
 
  <img width="241" alt="스크린샷 2022-03-10 오후 5 08 25" src="https://user-images.githubusercontent.com/59719632/157616535-1585e4a3-8d77-4423-be6d-643922d06ba3.png">

## 2-6. 삼각행렬(triangular matrix)
  - 상삼각행렬(U), 하삼각행렬(L)로 구성
  - 상삼각행렬(U) : 주대각원소 아래쪽에 있는 모든 원소가 0인 정사각행렬
  - 하삼각행렬(L) : 주대각원소 위쪽에 있는 모든 원소가 0인 정사각행렬

  ![스크린샷 2022-03-10 오후 5 10 05](https://user-images.githubusercontent.com/59719632/157616779-d40731c5-e853-4584-895b-04ebed8b3f0a.png)

  - 삼각행렬 간 덧셈, 뺄셈, 행렬 곱의 결과 : 삼각행렬
  - 상삼각행렬과 하삼각행렬은 전치행렬 관계이다.

  ![스크린샷 2022-03-10 오후 5 11 45](https://user-images.githubusercontent.com/59719632/157617077-4db85e63-f9d5-4bd8-b302-d207950c0e2a.png)
  
## 2-7. 특이행렬(singular matrix)
  - 특이행렬 A란 A의 역행렬이 존재하지 않는 행렬 => det(A) = 0 이 되는 행렬

## 2-8. 정칙행렬(non\-singular\-matrix)
  - 정칙행렬 A란 A의 역행렬이 존재하는 행렬 => det(A) != 0 이 되는 행렬

## 2-9. 행렬식
* 행렬식(determinant, det(A) or |A|)
  - 행렬의 특성을 하나의 숫자로 표현하는 방법
* 행렬이 단위 공간을 얼마나 늘렸는지 혹은 줄였는지를 나타냄
  - 행렬식=1 : 해당 행렬이 단위 공간의 부피와 같음
  - 행렬식=0 : 해당 행렬이 나타내는 부피가 0
  - 행렬식=10 : 해당 행렬이 단위 공간 부피의 10배에 해당함

  ![스크린샷 2022-03-10 오후 5 17 55](https://user-images.githubusercontent.com/59719632/157618107-817a0e23-8300-4565-9776-e39a4ae4d8f3.png)
  
  ![스크린샷 2022-03-10 오후 5 27 30](https://user-images.githubusercontent.com/59719632/157619728-b0c50544-942c-4d00-bf17-50d464b3578f.png)

* 소행렬식 (minor of entry a_ij) M_ij
  + 행렬의 i행과 j열을 제외하고 구성된 부분 행렬의 행렬식

* 여인수(cofactor of entry a_ij) C_ij = (-1)^(i+j) \* M_ij
  
  ![스크린샷 2022-03-10 오후 5 29 54](https://user-images.githubusercontent.com/59719632/157620182-1d9dcf32-4f5a-477b-ae12-b2c68fe1073f.png)

  - 여인수를 이용해 행렬식을 구하는 방법
 
  ![스크린샷 2022-03-10 오후 5 31 59](https://user-images.githubusercontent.com/59719632/157620574-bdced6a5-8c5d-4272-b3bf-da07e8289224.png)

  ![스크린샷 2022-03-10 오후 5 33 09](https://user-images.githubusercontent.com/59719632/157620775-221b2b34-8425-46b1-97ae-f7515959b4fe.png)  

* 삼각행렬의 행렬식
![스크린샷 2022-03-10 오후 5 35 35](https://user-images.githubusercontent.com/59719632/157621168-a84987a7-eff4-4a6f-95f4-b9c8543d57db.png)

* 대각행렬의 행렬식
![스크린샷 2022-03-10 오후 5 35 39](https://user-images.githubusercontent.com/59719632/157621196-8b22e2a9-8c47-4ca5-a44e-e03cf234b7e7.png)

* 전치행렬의 행렬식 : det(A) = det(A^T)

* 특정 행과 열의 원소가 모두 0일 때 행렬식 = 0

* 행렬곱과 행렬식
  - det(AB) = det(A) \* det(B)

```python3
import numpy as np

# Transpose matrix
A=np.array([[1,5],[3,4],[6,2]])
At=np.transpose(A)
At=A.T

# Symmetric matrix
B=np.array([[1,0,2],
            [0,2,1],
            [2,1,1]])
B==B.T            
# B^n 도 대칭행렬
Bn=B
for i in range(4):
  Bn=np.matmul(Bn,B)
  
# A*A^T => A^T*A  

# Diagonal matrix (D)
diag_B=np.diag(B)

# Identity matrix (I)
I=np.identity(3)

# Zero matrix(0)
Z=np.zeros((3,2))

# Triangular matrix (L,U)
U=np.triu(B) # upper tri
L=np.tril(B) # lower tri

# Singular matrix (S)
detB=np.linalg.det(B) # linear algebra function
```

## 2-10. 역행렬
* 역행렬
  - 행렬 A의 역행렬이란 AB = I를 만족하는 행렬 B
* 가역행렬
  - 행렬식이 0이 아니라는 조건이 필요
  - 가역행렬의 역행렬은 유일하다.
  - 역행렬이 존재하지 않는다면 행렬 A를 특이행렬이라 한다.
* 2x2 행렬의 역행렬 연산

<p align="center">
<img width="400" alt="스크린샷 2022-03-20 오전 9 18 50" src="https://user-images.githubusercontent.com/59719632/159142777-45696f4b-dab3-444b-8b10-ff7bd0eaa2af.png"> <img width="504" alt="스크린샷 2022-03-20 오전 9 20 07" src="https://user-images.githubusercontent.com/59719632/159142818-49747c85-4d56-4bf9-9ad5-af8b8c35f078.png">
</p>

* mxn 행렬의 역행렬 연산
  - 수반행렬(여인수행렬의 전치 행렬)을 통해 역행렬 연산이 가능

<p align="center">
<img width="350" alt="스크린샷 2022-03-20 오전 9 22 12" src="https://user-images.githubusercontent.com/59719632/159142890-644d6e91-e325-40d1-bdbd-f4f80844856c.png">
<img width="350" alt="스크린샷 2022-03-20 오전 9 22 54" src="https://user-images.githubusercontent.com/59719632/159142898-996f1601-4a3c-49eb-962f-dc8bce636512.png">
<img width="350" alt="스크린샷 2022-03-20 오전 9 23 26" src="https://user-images.githubusercontent.com/59719632/159142899-dcfceba6-5979-4cef-9e5d-48f3678fccb2.png">
</p>

* 역행렬의 성질
  - 정사각행렬(A)의 거듭 제곱
  - 역행렬의 거듭 제곱  
  - 역행렬과 전치행렬
    + 행렬 A가 가역행렬이면 A의 전치행렬도 가역행렬이다
    + 행렬 A가 가역행렬이면 A(A^T), (A^T)A도 가역행렬이다
    + A의 역행렬의 행렬식은 A의 행렬식의 역수이다. 

<p align="center">
<img width="400" alt="스크린샷 2022-03-20 오전 9 26 06" src="https://user-images.githubusercontent.com/59719632/159142985-a8bdb012-bedf-4f21-bd0e-172badcf1d65.png">
<img width="400" alt="스크린샷 2022-03-20 오전 9 27 44" src="https://user-images.githubusercontent.com/59719632/159142986-4b0ef86d-fbd7-4af9-9451-e6c516bfff46.png">
</p>

Chap 3. 선형시스템 Linear Systems
## 3-1. 선형방정식
* 선형방정식의 정의
  - 변수(x1,x2,...,xn)에 대한 1차 방정식
  - 최고차항의 차수가 1임
  - 선형방정식이 아닌 경우
    
<img width="400" alt="스크린샷 2022-03-20 오전 9 35 06" src="https://user-images.githubusercontent.com/59719632/159143110-c6f8fa18-015f-47e6-a98e-6490d9c9bf15.png">

* 선형시스템의 정의
  - 선형방정식의 집합
  - 연립1차방정식 (system of linear equation)

  <p align="center">
  <img width="400" alt="스크린샷 2022-03-20 오전 9 37 59" src="https://user-images.githubusercontent.com/59719632/159143163-e3f2af16-80f5-42c9-95c7-77ab522a559e.png"> <img width="400" alt="스크린샷 2022-03-20 오전 9 39 24" src="https://user-images.githubusercontent.com/59719632/159143189-86faf090-b782-4a85-959c-6d44d72c26d3.png">
</p>

* 기본행 연산(elementary row operation)
  - 한 행에 영이 아닌 상수를 모두 곱함
  - 두 행을 교환
  - 한 행의 배수를 다른 행에 더함

* 가우스 조르단 소거법
  - 선형 시스템의 해를 구하는 방법
  - 첨사 행렬을 기본행 연산을 이용해 가우스 행렬 혹은 기약가우스행렬 형태로 변환
  - 가우스 행렬 : 각 행의 0이 아닌 첫 원소는 1이고 1아래에 위치하는 원소는 모두 0인 행렬
  - 기약가우스행렬 : 가장 첫 원소가 1인 열에 대해 1을 제외한 나머지 행 원소가 모두 0인 행렬
  <p align="center">
  <img width="400" alt="스크린샷 2022-03-20 오전 9 44 14" src="https://user-images.githubusercontent.com/59719632/159143313-e07d35d3-c1ab-43f0-8ee6-eb27a6964a26.png">
  <img width="400" alt="스크린샷 2022-03-20 오전 9 45 47" src="https://user-images.githubusercontent.com/59719632/159143317-b06e6f1f-ba22-43b8-834f-5d333d2c5c46.png">
  </p>

  - 첨가행렬 형태로 정리
  - 기본행연산 수행
  
  <img width="448" alt="스크린샷 2022-03-20 오전 9 48 02" src="https://user-images.githubusercontent.com/59719632/159143374-55bfac79-7b7b-490e-936a-a366bd652a71.png">

  - 가우스 소거법
    + 가우스 행렬로 변환 후 첨가 행렬을 선형시스템으로 표현해서 해 찾기
  <img width="498" alt="스크린샷 2022-03-20 오전 9 49 41" src="https://user-images.githubusercontent.com/59719632/159143406-8b044bf7-b225-45eb-aa32-0e29dc966cc4.png">

* 동차선형시스템 (homogeneous linear system)
  - 우변이 0인 선형시스템
  - 오직 하나의 해 또는 무한개의 해

  <img width="437" alt="스크린샷 2022-03-20 오전 9 51 02" src="https://user-images.githubusercontent.com/59719632/159143421-75bc914f-a177-44bb-b3de-711c235951b4.png">

```python3
import numpy as py
invA=np.linalg.inv(A)
sol=np.linalg.solve(A,y) # A는 행렬, y는 값 => Ax=y
```

## 3-2. 벡터공간
* 벡터공간
  - 벡터의 덧셈과 스칼라 곱이 정의된 공간
  - 선형공간
  - 차원의 개념
    + 1차원 : 숫자 하나로 표현
    + 2차원 : 각 벡터의 원소가 2개로 구성
    + 3차원 : 각 벡터의 원소가 3개로 구성
  - 유닛벡터 (unit vector)
    + 어떤 공간의 좌표 축의 기본 벡터
    + ex) 3차원 공간에서 i,j,k
    + n차원 벡터는 유닛벡터의 선형결합으로 나타낼 수 있다.
* 부분공간 (subspace)
  - 공간 R^n의 부분집합 V가 아래의 2가지 조건을 만족하면 V를 부분공간이라 함
    + 부분공간 V에 속하는 벡터 u,v에 대해 두 벡터의 합인 u+v도 공간 V에 속한다
    + a가 임의의 스칼라이고 벡터 u가 공간 V에 속할 때, a\*u도 공간 V에 속한다.
## 3-3. 선형결합 (Linear Combinations)
  
  <p align="center">
  <img width="400" alt="스크린샷 2022-03-20 오전 10 08 09" src="https://user-images.githubusercontent.com/59719632/159143723-68bf4823-9f39-4842-987a-cfe577ec3640.png">
  <img width="409" alt="스크린샷 2022-03-20 오전 10 10 32" src="https://user-images.githubusercontent.com/59719632/159143772-b645982e-be36-4033-8d2f-c73bc24e3cf4.png">
  </p>

  <img width="480" alt="스크린샷 2022-03-20 오전 10 11 14" src="https://user-images.githubusercontent.com/59719632/159143783-1d94e59c-be32-4f66-9c78-43d059bfdaf8.png">

* 선형결합의 의미
     
  <img width="539" alt="스크린샷 2022-03-20 오전 10 17 09" src="https://user-images.githubusercontent.com/59719632/159143877-34236ff9-222a-497a-a6dc-d486c593ae7b.png">

## 3-4. Span 
* Span{v1,...,vn}
  - 주어진 v1,...,vn에 대하여 이 벡터들의 모든 선형 결합에 대한 집합
  - 2개의 벡터(2차원) : 두 벡터가 포함되어 있는 평면
  - 1개의 벡터(1차원) : 직선
  - 3개의 벡터(3차원) : 3차원에 해당하는 모든 공간의 점
* 선형시스템 (Ax=b)의 해가 존재하는 경우
  - Span 안에 b 벡터가 포함되어 있을 때
  
  <img width="509" alt="스크린샷 2022-03-20 오전 10 29 23" src="https://user-images.githubusercontent.com/59719632/159144215-8c25ad4f-be28-4400-9a00-f62d962d1275.png">

## 3-5. 선형독립

![image](https://user-images.githubusercontent.com/59719632/160266157-5ebd866f-3ea4-4cdb-9b19-c47dc34a41c3.png)

* 선형독립
  - span 안의 한 벡터가 다른 벡터들의 선형 결합으로 표현이 되지 않는 경우
  - 표현이 된다면 선형종속이다.
  - 특정한 벡터가 추가되었을 때, 새로운 Span을 생성할 수 있어야 함
  
  ![image](https://user-images.githubusercontent.com/59719632/160266209-cf53e343-d5c6-4cd6-aca5-e33099e056d4.png)
  
  ![image](https://user-images.githubusercontent.com/59719632/160266302-c369c898-3a17-4dd2-b037-b1c7a2a0aa44.png)

  - 선형독립 판정
    + 행렬식 != 0
    * n차원 벡터공간에 n개 보다 많은 벡터가 있는 경우 선형 종속이다.
    * n차원 벡터공간에 n개보다 적은 벡터가 있는 경우 독립 일수도 종속일 수도 있다.
    
    ![image](https://user-images.githubusercontent.com/59719632/160268098-4476bed9-0588-422b-984d-077e6a40aa5c.png)

    ![image](https://user-images.githubusercontent.com/59719632/160268147-29cc1c53-2361-459a-bce6-9917b348e467.png)


* 선형종속
  - 특정한 벡터를 다른 벡터의 선형결합으로 표현 가능
  
  
  
## 3-6. 기저
* 부분공간 (Subspace)
  - 두 개의 벡터에 대해 어떠한 스칼라 곱 및 벡터 덧셈을 하더라도 부분공간 안에 존재해야 함
  - 닫힌 선형결합 조건을 만족하는 벡터의 subset으로 정의
  - Span은 항상 부분공간이다.

* 기저벡터 (Basis)
  - 부분 집합 S가 주어질 때 아래 두 조건을 만족하면 S를 R^n의 기저벡터라 한다.
    + S가 선형독립
    + Span(S) = R^n
  - 선형독립으로만 이루어진 벡터

  ![image](https://user-images.githubusercontent.com/59719632/160268243-3abc397e-1afa-4d56-a570-0ff18c3aea82.png)
  
  - 하나의 subspace에 관한 기저 벡터는 유일한가? NO!

  - 벡터 공간의 성질
    + n개가 넘는 벡터가 만드는 집합은 선형종속
    + n개 미만의 벡터가 만드는 집합은 벡터공간 S를 생성할 수 없음
    + 벡터 공간의 모든 기저벡터의 개수는 동일

  ![image](https://user-images.githubusercontent.com/59719632/160268328-86e7fe19-18fd-4a37-9732-c3d1be7b2612.png)

## 3-7. 차원
* 차원 (Dimension)
  - 해당 공간을 구성하는 기저 벡터의 개수
    + 1차원 : 1개
    + 2차원 : 2개
    + 3차원 : 3개

* 행공간 / 열공간 / 영공간
  - 행공간: 행벡터로 Span할 수 있는 공간
  - 열공간 (rank): 열벡터로 Span할 수 있는 공간
  - 영공간 (null space): 행렬 A가 주어질 때 Ax=0을 만족하는 모든 x의 집합
  - 행공간과 열공간의 차원은 항상 같다.
  
    ![image](https://user-images.githubusercontent.com/59719632/160268422-49fef584-c319-4513-ae3b-b3220b7549c4.png)
 
 
## 3-8. 선형변환 (Linear Transformation)
* 변환
  - 입력과 출력이 모두 벡터인 함수
   
  ![image](https://user-images.githubusercontent.com/59719632/160277622-f4166956-aeed-48e4-886b-50eb159195c2.png)
  
  - 행렬변환
  
  ![image](https://user-images.githubusercontent.com/59719632/160277691-db8d0f83-3355-431e-90a2-e12f2011e9be.png)

  - 선형변환
    + T(x+y) = T(x) + T(y), T(ax)= aT(x) 를 만족
    
    ![image](https://user-images.githubusercontent.com/59719632/160277738-29c63dc9-54de-4c73-b0d9-96bf7c51be28.png)

    ![image](https://user-images.githubusercontent.com/59719632/160277870-51cfdb87-0218-445e-9fe6-cc23267227a3.png)
     
    ![image](https://user-images.githubusercontent.com/59719632/160277877-41094c0b-a6ae-496a-b5df-0d710a6cabb9.png)
 
    ![image](https://user-images.githubusercontent.com/59719632/160278007-ea911efd-4dd2-4b59-8995-656c7544f686.png)

    ![image](https://user-images.githubusercontent.com/59719632/160278074-ac0cf7d6-af8a-4119-8502-4d5f17b5650c.png)

    ![image](https://user-images.githubusercontent.com/59719632/160278094-1d17ddf7-d3a4-4ccd-8307-81604c15fd56.png)

    ![image](https://user-images.githubusercontent.com/59719632/160278150-9bae2c8e-b5d1-49a4-9379-090408cd58e9.png)

* 선형변환의 기하학적 의미
  - 축을 움직이면서 자연스럽게 input 벡터가 바뀌는 것 
 
  ![image](https://user-images.githubusercontent.com/59719632/160278281-da1d743e-7a95-46ad-b9ec-f00667b5a2b5.png)
  
* 선형변환
  - 변환 중에서도 선형성을 가지는 변환
    + 직선 형태를 띄던 벡터가 변환 이후에도 직선형태여야 함
    + 원점이 고정된 채로 유지
    
  ![image](https://user-images.githubusercontent.com/59719632/160278617-5dfd4435-efe4-40e7-93ea-e04f9cde5a8d.png)

 
