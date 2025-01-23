## 모듈

### 모듈: 한 파일로 묶인 변수와 함수의 모음. 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

- math 내장 모듈
    
    : 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
    
    ```python
    import math
    import random # 난수 생성
    import datetime # 날짜, 시간 관련
    
    print(math.pi) # 3.141592653589793
    
    print(math.sqrt(4)) #2.0
    
    print(random.randint(1, 10)) # 1~10 중 랜덤한 정수 하나 반환
    
    now = datetime.datetime.now() # datetime 모듈의 datetime 클래스 .. 
    print(now) 
    ```
    

- 모듈을 가져오는 방법
    1. import문 사용 (스타일 가이드에선 얘를 좀 더 권장)
        
        ```python
        import math
        
        print(math.sqrt(4))
        ```
        
    2. from 절 사용
        
        ```python
        from math import sqrt
        
        print(sqrt(4))
        ```
        
        → from 절 사용 시 sqrt가 모듈에서 가져온 함순지, 아닌지 명확하지 않아서 import문 사용을 좀 더 권장하나, 필수는 x. 이름 충돌도 해결 가
        
    

- 모듈 사용하기
    - ‘. (dot)’ 연산자
    - “점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라”

- 모듈 주의사항
    - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
    
    ![마지막에 import된 이름으로 대체됨](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/86a04673-cf30-4e00-8d27-313f3453c342/image.png)
    
    마지막에 import된 이름으로 대체됨
    

- sol) ‘as’ 키워드
    - as 키워드를 사용하여 별칭(alias) 부여
    - 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
    
    ```python
    from math import sqrt
    from my_math import sqrt as my_sqrt
    
    sqrt(4)
    my_sqrt(4)
    ```
    

### 사용자 정의 모듈

![my_math.py를 모듈로 가져옴 
(같은 경로에 있어서 바로 가져올 수 o, 다른 경로면.. 경로로 가져와야됨)](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/b19d67f2-2c7c-4114-a849-af55673961e9/image.png)

my_math.py를 모듈로 가져옴 
(같은 경로에 있어서 바로 가져올 수 o, 다른 경로면.. 경로로 가져와야됨)

### 파이썬 표준 라이브러리 (PSL)

: 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

- 모듈, 패키지 보다 좀 더 큰게 라이브러리..
- 패키지: 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것

![모듈, 패키지, 라이브러리 포함 관계](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/83b6dd07-f675-4c32-8fb7-0523ed980233/image.png)

모듈, 패키지, 라이브러리 포함 관계

- 패키지 사용하기

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/d4d0a974-25d6-4ada-82df-20a5a39a17c4/6f0f2671-e39f-486d-a94d-c012f9239f89.png)

- 경로가 길어지면 from 절 써서 가져오는 게 좋음

```python
from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1, 2))
print(tools.mod(1,2))
```

- PSL 내부 패키지: 설치 없이 바로 import 하여 사용
- 외부 패키지: pip를 사용하여 설치 후 import 필요
    - pip(파이썬 패키지 관리자): 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
    - 패키지 설치
        
        ![삭제하려면 install 대신 uninstall](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/8260de80-7ff9-4961-8c16-f2dae36dc4a8/image.png)
        
        삭제하려면 install 대신 uninstall
        
    - requests 외부 패키지 설치 및 사용 예시
        
        ```python
        $ pip install requests # 외부 API 서버로 요청
        ```
        
        ```python
        import requests
        
        # 무작위 사용자 정보를 제공해주는 API의 URL
        url = 'https://random-data-api.com/api/v2/users'
        
        # requests.get(rul)을 통해 API에 요청을 보냄
        # 서버로부터 응답(Response)을 JSON 형태로 받아 Pyton 객체 (딕셔너리/리스트 등)로 반환
        response = requests.get(url).json()
        
        # 받은 응답 데이터(딕셔너리 형태)를 출력
        print(response)
        print(type(response)) # <clss 'dict'>
        ```
        
    - 패키지 사용 목적
        
        : 모듈들의 이름공간을 구분하여 충돌 방지. 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할
        

## 제어문

: 코드의 실행 흐름을 제어하는 데 사용되는 구문. 조건에 따라 코드블록을 실행하거나 반복적으로 코드 실행

- 반복문: for, while
- 반복문 제어: break, continue, pass

### 조건문

: 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀

- if, elif, else
    
    ```python
    # if statement의 기본 구조
    if 표현식:
    	코드 블록
    elif 표현식:
    	코드 블록
    else:
    	코드 블록
    ```
    
- 복수 조건문: 조건식을 동시에 검사하는 것이 아니라 “순차적”으로 비교
- 중첩 조건문: 조건문 안에 조건문

### 반복문

: 주어진 코드 블록을 여러 번 반복해서 실행하는 구문

1. for: 특정 작업을 반복적으로 수행
    
    : 임의의 ~~시퀀스 항목~~들(비시퀀스도 가능)을 그 시퀀스에 들어있는 순서대로 반복
    
    - **반복 횟수가 명확하게 정해져 있는 경우에 유용**
        
        **ex.  리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때**
        
    
    ```python
    for 변수 in 반복 가능한 객체:
    	코드 블록
    ```
    
    - 반복 가능한 객체 iterable
        
        : 반복문에서 순회할 수 있는 객체
        
        (시퀀스 객체 뿐만 아니라 dict, set 등도 포함) 
        
        → (dict, set는 순서가 없으나,, 출력되는 순서는 보장을 해줘서 반복 가능)
        
    - for문 작동 원리 (작업량이 정해진 상태로 진행)
        - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록이 실행
        - 다음으로 반복 변수에 리스트의 2번쨰 항목이 할당되고 코드블록이 다시 실행
        - … 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드 블록이 실행
            
            ```python
            items = ['apple', 'banana', 'coconut']
            
            for item in items: # items의 길이만큼 반복
            	print(item)
            ```
            
            ```python
            for i in range(5): # range(5): 0~4 총 5번
            	print(i)
            ```
            
            ```python
            # 딕셔너리 순회. key를 반복
            my_dict = {
            	'x' : 10,
            	'y' : 20,
            	'z' : 30,
            }
            
            for key in my_dict:
            	print(key)
            	print(my_dict[key])
            ```
            
            - 추가,,)
            
            ```python
            items = ['apple', 'banana', 'coconut']
            
            for item in items:
            	print(item)
            
            print(item) #coconut이 출력될 것.... item은 전역 scope에 종속이 됨..
            ```
            
            - 중첩 반복문
                
                ```python
                outers = ['A', 'B']
                inners = ['c', 'd']
                
                # 총 4번 반복 (2*2)
                for outer in outers:
                	for inner in inners:
                		print(outer, inner)
                		
                		
                elements = [['A','B'], ['c','d']]
                
                for elem in elements:
                	print(elem)  
                """
                ['A', 'B'] 
                ['c', 'd']
                """
                for elem in elements:
                	for item in elem:
                		print(item)
                """
                A
                B
                c
                d
                """
                
                ```
                

1. while: 주어진 조건이 참인 동안 반복해서 실행
    
    주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
    
    == 조건식이 거짓(False)가 될 때까지 반복
    
    - **반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용**
        
        **ex.  사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우**
        
    
    ❗ while문은 반드시 종료 조건이 필요!!
    

### 반복 제어

:for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

- 반복문 제어 키워드
    1. break: 반복을 즉시 중지
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/def99abd-2217-4431-b027-b007a8de4b52/image.png)
        
        이 때 break는 if를 탈출하는게 아니라 for문을 탈출하는 것!!
        
    2. continue:  현재 반복문의 남은 코드를 건너 뛰고 다음 반복으로 넘어감
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/94b4ecf8-129e-4b0a-9547-ab2b2e8f2317/image.png)
        
    3. pass: 아무런 동작도 수행하지 않고 넘어감
        
        a. 코드 작성 중 미완성 부분
        
        - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음
        
        b. 조건문에서 아무런 동작을 수행하지 않아야 할 때
        
        ```python
        if condition:
        	pass #아무런 동작도 수행하지 않음
        else:
        	# 다른 동작 수행
        ```
        
        c. 무한루프에서 조건이  충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
        
        ```python
        while True:
        	if condition:
        		break
        	elif condition:
        		pass # 루프 계속 진행
        	else:
        		print('..')
        		
        ```
        

➕ 어떠한 값을 찾고 나서 True/False를 바꾸는 변수 → ‘플래그 변수’ 

(현재 우리 코드의 상태를 나타내는 변수)

### List Comprehension: 간결하고 효율적인 리스트 생성 방법

but, 가독성은 떨어짐. 너무 남용하진 x

- List Comprehension 구조
    
    ```python
    [expression for 변수 in iterable]
    
    list(expression for 변수 in iterable)
    ```
    
    ```python
    [expression for 변수 in iterable if 조건식]
    
    list(expession for 변수 in  iterable if 조건식)
    ```
    
- 예시
    
    ```python
    # append 사용
    num = [1,2,3,4,5]
    suqared_numbers = []
    
    for num in numbers:
    	squared_numbers.append(num**2)
    
    print(squared_numbers) #1,4,9,16,25
    
    # 리스트 컴프리헨션 사용
    [num**2 for num in numbers] # 1,4,9,16,25
    list(num**2 for num in numbers) # 1,4,9,16,25
    ```
    
    ```python
    
    # 리스트 컴프리헨션 with 조건문
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens) # [0,2,4,6,8]
    ```
    
    ```python
    # 2차원 배열 생성 시 (인접행렬 생성 시)
    data1 = [[0] * (5) for _ in range(5)]
    
    # 또는
    data2 = [[0 for _ in range(5)] for _ in range(5)]
    ```
    
    ```python
    # map 사용
    result3 = list(map(lambda i: i, range(10)))
    ```
    

➕ 모듈 내부 살펴보기

- 내장 함수 help를 토해 모듈에 무엇이 들어있는지 확인가능
- help(math)
- 파이썬 공식문서에서 보는게 좋음..

➕ enumerate(iterable, start = 0)

: iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
	print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits,3):
	print(index, fruit)
"""
3 apple
4 banana
5 cherry
"""
```

---

### ➕ for else

```python
for i in range(10):
	if i == 5:
		print("5번째에서 멈췄습니다. ")
		break
else:
	# 중간에 for문이 break로 인해서 탈출하지 않고, 끝까지 돌았을 떄 이쪽 else로 옴
	# 중간에 break가 걸리면 else도 실행 안됨
	print("전부 돌았습니다.")
# 만약 조건문에 들어가지 않고, break하지 않고 끝까지 for loop을 돌면
# 전부 돌았습니다. 를 출력하세요.
```

- flag로 구현

```python
flag = False #break 한 적 있는지 판단 가능
for i in range(10):
	if i == 5:
		print("5번째에서 멈췄습니다.")
		flag = True
		break

if not flag: #flag가 False라는 건 break에 걸린 적이 없다는 것..!
	print("전부 돌았습니다.")
```