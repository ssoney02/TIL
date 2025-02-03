## 함수와 Scope

### 함수: 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음

- 함수 사용 이유
    - 코드의 중복 방지
    - 재사용성 높임, 코드의 가독성과 유지보수성 향상

### 함수 호출

: 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것

- function_name(arguments)

### 함수 구조

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/ab9a47dc-85cb-4ce7-9353-196cd4b08232/image.png)

- docstring: 이 함수가 어떤 함수인지, 사용법 설명 (설명서)

### 함수 정의와 호출

1. 함수 정의
    - 함수 정의는 def 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호 안에 매개변수 정의 가능
    - 매개변수(parameter)는 함수에 전달되는 값을 나타냄
2. 함수 body
    - 콜론 다음에 들여쓰기 된 코드 블록
    - 함수가 실행될 때 수행되는 코드를 정의
3. Docstirng: 함수 body 앞에 선택적으로 작성 가능한 함수 설명서
4. 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return 문은 함수의 실행 종료, 결과를 호출 부분으로 반환
    - 함수 내에 return 문이 없다면 None이 반환됨 (return None)
        - print함수가 반환값이 없는 대표적인 함수
            
            → 아무것도 return하지 않고 사용자가 입력한 것을 터미널에 출력
            
            ```python
            return_value = print(1)
            print(return_value) #None
            ```
            
            ```python
            def my_func():
            	print('hello')
            
            result = my_func() #hello
            print(result) #None
            ```
            
            → my_func()이 호출되긴 했으므로 hello가 출력됨
            
            ⭐ 화면의 출력과 반환은 아무 관련x
            
5. 함수 호출
    - 함수를 사용하기 위해서는 호출이 필요
    - 함수의 이름, 소괄호를 활용해 호출
    - 필요한 경우, 인자 (argument)전달 해야 됨
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨

### 매개변수와 인자

- 매개변수: 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
- 인자: 함수를 호출할 때, 실제로 전달되는 값

1. **Positional Arguments (위치인자)**
    
    : 함수 호출 시 인자의 위치에 따라 전달되는 인자
    
    ⭐ 위치인자는 함수 호출 시 반드시 값을 전달해야 함
    
    ![위치에 따라 출력되는 것이라 입력한 인자가 이름인지 숫자인지 함수는 모름, 그냥 위치대로 입력](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/e14340eb-70d7-41f6-b2e0-bf93659d5357/image.png)
    
    위치에 따라 출력되는 것이라 입력한 인자가 이름인지 숫자인지 함수는 모름, 그냥 위치대로 입력
    

1. **Default Argument Values(기본 인자 값)**
    
    : 함수 정의에서 매개변수에 기본 값을 할당
    
    - 함수 호출 시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당 됨
    
    ![image.png](
    

1. **Keyword Arguments (키워드 인자)**
    
    : 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    
    - 매개변수와 인자를 일치시키지x, 특정 매개변수에 값을 할당 가능
    - 인자의 순서는 중요x, 인자의 이름을 명시하여 전달
    
    ⭐ 단, 호출 시 키워드 인자는 위치인자 뒤에 위치해야 함
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/53e3d932-7b39-4e3f-871d-fa5ce818f2b9/image.png)
    

1. **Arbitrary Argument Lists(임의의 인자 목록)**
    
    : 정해지지 않은 개수의 인자를 처리하는 인자
    
    - 함수 정의 시 매개변수 앞에 ‘*’를 붙여 사용
    - 여러 개의 인자를 tuple로 처리
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/ccc5c718-432b-42f0-8631-97dd4e0e76cb/image.png)
    

1. **Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록)**
    
    : 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    
    - 함수 정의 시 매개변수 앞에 ‘**’를 붙여 사용
    - 여러 개의 인자를 dictionary로 묶어 처리
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/1e1367c6-930d-4099-88ae-5316a7eebf2a/image.png)
    

**➕ 함수 인자 권장 작성 순서**

: 위치 → 기본 → 가변 → 가변 키워드

- 단 , 모든 상황에 적용되는 절대적인 규칙은 x, 상황에 따라 유연하게 조정될 수 o

### 재귀 함수

: 함수 내부에서 자기 자신을 호출하는 함수

- 재귀함수 예시 - 팩토리얼
    
    ```python
    def factorial(n):
    	#종료 조건: n이 0이면 1을 반환
    	if n == 0:
    		return 1
    	else:
    		#재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    		return n * factorial(n-1)
    
    print(factorial(5)) #120
    ```
    
- base case로 수렴해야됨 (안그러면 무한하게 반복됨..)
- 재귀함수 특징
    - 특정 알고리즘 식을 표현할 때 변수 사용 감소, 코드 가독성 높아짐
    - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
    
    ⭐ 종료 조건 명확히, 반복되는 호출이 종료 조건을 향하도록
    

### 내장 함수

:  파이썬이 기본적으로 제공하는 함수

(별도의 import 없이 바로 사용 가능)

ex. print(), len(),max, min, sum, sorted..

**<유용한 내장 함수>**

- **map(function, iterable)**
    
    : 순회(반복) 가능한 데이터구조 (iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
    
    - map의 function 부분에 다른 함수가 들어갈 수도 있음!!!
        
        → ex)
        
    
    ```python
    def get_double_number(a):
    	return a * 2
    
    b = [1,2,3,4]
    
    result = list(map(get_double_number, b))
    print(result)
    ```
    
    ```python
    numbers = [1,2,3]
    result = map(str, numbers)
    
    print(result) # <map object at 0x0000~~~
    print(list(result)) #['1','2','3']
    ```
    
- **zip(*iterables)**
    
    : 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/d9cc13b4-c0ed-4281-b88a-56d00ff691be/image.png)
    
    1. 여러 개의 리스트를 동시에 조회할 때 많이 사용
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/30aa8be4-8b27-4a20-821b-090ba1416349/image.png)
    
    1. 2차원 리스트의 같은 컬럼(열) 요소를 동시에 조회할 때
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/9e4aacd0-b5b2-431b-a2d3-75109723f4e6/image.png)
    

### python의 범위(scope)

1. scope
    - global scope: 코드 어디에서든 참조할 수 있는 공간
    - local scope: 함수가 만든 scope (함수 내부에서만 참조 가능)
    
    local scope에 존재하는 변수는 global scope에서 사용 불가
    
    - 변수의 수명주기
        
        변수의 수명주기는 변수가 선언되는 위치와 scope에 따라 결정됨
        
        1. built-in scope :파이썬이 실행된 이후부터 영원히 유지
        2. global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
        3. local scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    - 이름 검색 규칙(Name Resolution)
        
        LEGB Rule
        
        - 함수 안에 함수가 있는 경우, enclosed scope라고 함 (ex. 재귀 함수)
        - 역순은 x, 함수 내에서는 바깥 scope의 변수에 접근 가능하나, 수정은 x
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/6c90e9ed-1f19-473b-8066-6517514e9119/image.png)
        
        - LEGB Rule 예시
            - sum은 원래 내장함수 (built-in)인데 내장함수의 이름(sum)을 변수로 지정(global)
                
                → global을 먼저 찾아서 built-in의 sum을 사용x
                
            
            ![del sum을 쓰기 보단,, 애초에 내장함수 이름을 변수로 쓰면 안됨!!!!](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/4ba1b246-1324-4cee-a475-b3baa84d121c/image.png)
            
            del sum을 쓰기 보단,, 애초에 내장함수 이름을 변수로 쓰면 안됨!!!!
            
            ⭐
            
            ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/6f18dc33-616f-4305-862b-14731dc7fa94/image.png)
            
            → **함수는 호출될 때 실행됨**
            
            마지막 enclosed()에서 호출되어 실행됨
            
            def local(c)부분은 정의
            
            local(500)에서 local 함수가 호출되어 실행 → c = 500
            
2. variable
    - global variable: global scope에 정의된 변수
    - local variable: local scope에 정의된 변수

➕ ‘global’ 키워드

- 변수의 scope를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/37030194-b4c8-4a78-887f-8d70b06f41de/image.png)
    

⚠️ global 키워드 선언 전에 참조 불가

→ 예시) global 선언 전에 print(num)을 해버림

⚠️ 매개변수에는 global 키워드 사용 불가

## 함수 스타일 가이드

### 함수 이름 작성 규칙

1. 소문자와 언더스코어(_) 사용
2. 동사로 시작하여 함수의 동작 설명
3. 약어 사용 지양
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/93fe9f30-3b8e-4b7f-a5b9-161ae2087ea3/image.png)
    

### 함수 이름 구성 요소

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/8dd6c940-f004-4ee7-bf31-69f197d971c5/image.png)

### 단일 책임 원칙

: 모든 객체는 하나의 명확한 목적과 책임만을 가져야 함

(함수도 객체)

## Packing & Unpacking

### Packing: 여러 개의 값을 하나의 변수에 묶어서 담는 것

- 한 변수에 콤마(,)로 구분된 값을 넣으면 자동으로 튜플로 처리 (튜플의 본체는 콤마,,,,)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/7ff21b57-a19b-4014-b5f3-e964c9b49831/image.png)

- ‘*’을 활용한 패킹 (변수 할당 시)
    1.  ‘*변수명’을 사용하면 ‘나머지 모든 값’을 리스트로 묶어서 받을 수 있음
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/4fc103b0-fd08-4a56-bc38-08b73c71c87e/image.png)
        
    2. ‘*매개변수’를 사용하면 호출 시 여러 개의 인자를 한 변수에 묶어서 받을 수 있음
        - 이때 함수 내부에서 해당 매개변수는 튜플 형태로 취급
    

### Unpacking: 패킹된 변수를 풀어서 개별 변수나 함수 인자로 전달

- 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
    
    → 수가 일치해야하는 듯
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/92f89b6e-a365-47d3-8660-ca07dd6e0b4d/image.png)
    
- 시퀀스(리스트, 튜플 등)를 함수에 전달할 때, 각 요소를 ‘풀어서’ 개별 인자로 넘겨 줄 수 o
    
    ![*names가 아니라 그냥 names를 넣으면 인자 하나만 들어간 상태라 에러남
     my_function(x,y,z)이므로..](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/1745c979-879f-4bb8-8ae6-c46380720d86/image.png)
    
    *names가 아니라 그냥 names를 넣으면 인자 하나만 들어간 상태라 에러남
     my_function(x,y,z)이므로..
    
- 딕셔너리 키-값 쌍을 분리해, 함수의 키워드 인자로 전달할 때 사용
    - 딕셔너리의 값을 활용하는 구조임. key값은 매개변수를 나타내기 위해 사용한거라,,
        
        들어갈땐 key 매칭해서 값만 들어간다고 생각하면 됨
        
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/a8109383-3b5d-42a9-b501-86149adc5059/image.png)
    

### *, ** 패킹/언패킹 연산자 정리

1. ‘*’
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 리스트나 튜플로 묶음
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
2. ‘**’
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 개별 키워드 인자로 전

## 람다 표현식

: 익명 함수를 만드는 데 사용되는 표현식 ⇒ 한 줄로 간단하게 함수를 정의

- 구조
    
    lamda 매개변수: 표현식
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/48c5feeb-1f4e-4388-acfa-78580b3af165/image.png)
    
- 활용 경우
    1. 간단한 연산이나 함수를 한 줄로 표현할 때
    2. 함수를 매개변수로 전달하는 경우에 유용하게 사용