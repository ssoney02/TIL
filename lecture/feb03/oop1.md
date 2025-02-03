## 절차 지향 프로그래밍

:프로그램을 함수와 로직(절차) 중심으로 작성.

데이터를 함수에 전달하며 순차적으로 처리

- 절차지향 프로그래밍 특징
    - 입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태
    - 순차적인 명령어 실행
    - 데이터와 함수(절차)의 분리
    - 함수호출의 흐름이 중요
    
    ⇒데이터를 재사용하기보다는 처음부터 끝까지 실행되는 결과물이 중요
    
- 절차 지향적 프로그래밍의 한계
    1. 복잡성 증가
        - 프로그램 규모가 커질 수록 데이터와 함수의 관리가 어려움
        - 전역 변수의 증가로 인한 관리의 어려움
    2. 유지보수 문제
        - 코드 수정 시 영향 범위 파악이 어려움

## 객체 지향 프로그래밍

: 데이터와 함수를 하나의 단위(객체)로 묶어서 관리. 

객체들을 조합하고 재활용하는 방식으로 프로그램 구성

![image.png](attachment:4903fadd-aec5-4cc3-9ad1-fa10d3ad55cc:image.png)

→ person이라는 클래스로 무언가를 반환 → 메서드 사용(변수가 메서드 호출)

- 객체 지향 프로그래밍 특징
    - 프로그램을 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 조직적으로 관리
    - 데이터와 메서드의 결합
    
    ![공통의 목적이 있는걸 하나의 객체로 묶어버림](attachment:dd40cf92-4040-4eb9-ade1-623bb1dca688:image.png)
    
    공통의 목적이 있는걸 하나의 객체로 묶어버림
    

### 절차지향 & 객체지향

절차지향: 데이터와 해당 데이터를 처리하는 함수가 분리. 함수 호출의 흐름이 중요

→ “어떤 순서로 처리할까”

객체지향: 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체(클래스)로 묶음. 객체 간 상호작용과 메시지 전달이 중요

→ “어떤 객체가 이 문제를 해결할까” “이 객체는 어떤 속성과 기능을 가질까”

- 둘을 대립적인 관계로 보면 x

**객체지향**: 수동적인 데이터가 능동적인 객체로 변화한 것

데이터가 함수를 호출함.. 

- 절차지향 → 데이터가 함수의 매개변수로 전달되어 처리되는 수동적 존재
- 객체지향 → 데이터와 해당 데이터를 처리하는 메서드가 하나의 객체로 통합되어 스스로 기능을 수행하는 능동적 존재가 됨

⇒ 코드의 구조화, 재사용성 높임 & 실제 세계의 모델링 방식과 더 유사한 프로그래밍 가능하게 함.

(기존 절차 지향을 기반으로 두고 + 보완하기 위해 객체 개념을 도입! 상속, 코드 재사용성 ,유지보수성 등의 이점가짐 → 대조적 관계가x)

## 객체와 클래스

### 객체(Object)

:실제 존재하는 사물을 추상화한 것

- “속성”, “동작”을 가짐
    
    (속성 → 변수 / 동작 → 메서드)
    
- 객체 특징
    1. 속성: 객체의 상태/데이터
    2. 메서드: 객체의 행동/기능
    3. 고유성: 

### 클래스(Class)

: 객체를 만들기 위한 설계도

- 데이터와 기능을 함께 묶는 방법을 제공
- 파이썬에서 타입을 표현하는 방법

→ 클래스로부터 여러 개의 객체를 쉽게 찍어낼 수 있음

ex. 아이유, bts → 객체. 둘다 노래한다라는 공통 동작 → 가수라는 클래스안에 노래라는 메서드를 만들면됨

## 클래스 기초

### 클래스

: 데이터와 기능을 하나의 틀로 묶어 관리하는 방법. 사용자 정의 객체를 만드는 수단이자 속성과 메서드를 정의

### 클래스 정의

class 키워드

클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 작성

```python
class MyClass:
	pass
```

cf. 변수명 → 스네이크케이스 (언더바 사용)

- __init__ 메서드는 ‘생성자 메서드’로 불림. 새로운 객체를 만들 때 자동으로 호출되어 필요한 초기값을 설정
    
    → 개발자가 직접 호출을 진행하진 x
    

## 인스턴스

: 클래스를 통해 생성된 객체

(클래스 → 설계도, 인스턴스 → 그 설계도로부터 실제로 만든 ‘개별 물건’)

- Person(”Alice”, 25) 라고 하면 Person이라는 설계도로부터 이름이 Alice이고 나이가 25인 ‘사람 객체’가 탄생

## 클래스와 인스턴스

![image.png](attachment:7bfc6a38-d70a-4da3-8d9c-e2502dcc95c1:image.png)

**클래스를 만든다 == 타입을 만든다**

- 변수 name의 타입은 str 클래스다
- 변수 name은 str클래스의 인스턴스이다.
- 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.

```python
name = 'Alice'
print(type(name)) # <class 'str>
```

![image.png](attachment:97e00ef4-edcb-46de-9f8a-479374f5fb97:image.png)

list_1.append() → 리스트 클래스 안에 작성된 메서드 (내부적으로 이렇게 동작함)

- 하나의 객체는 특정 클래스의 인스턴스이다.

### 클래스 구조

- 생성자 메서드
    - 인스턴스 생성 시 자동 호출되는 특별한 메서드
    - __init__ 이라는 이름의 메서드로 정의
    - 인스턴스 변수의 초기화 담당
- 인스턴스 변수(속성)
    - 각 인스턴스 별 고유한 속성
    - self.변수명 형태로 정의
    - 인스턴스마다 독립적인 값 유지→ 찍어낼 때 마다 다른……
- 클래스 변수(속성)
    - 모든 인스턴스가 공유하는 속성
    - 클래스 내부에서 직접 정의
    
    ```python
    class Circle:
    	# 클래스 변수(속성)
    	pi = 3.14
    	
    	def __init__(self, radius):
    		self.radius = radius
    	
    c1 = Circle(5)
    
    print(c1.pi) # 3.14
    	
    ```
    
    ```python
    class Circle:
    	# 클래스 변수(속성)
    	pi = 3.14
    	
    	def __init__(self, radius):
    		self.radius = radius
    	
    c1 = Circle(5)
    c2 = Circle(10)
    c1.pi = 100
    print(c1.pi) # 100
    print(Circle.pi) # 3.14
    
    print(c2.pi) # 3.14
    ```
    

- 클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조하게 됨
- class.class_variable로 클래스 변수 참조 가능

## 메서드

: 클래스 내부에 정의된 함수. 해당 객체가 어떻게 동작할지를 정의

### 메서드 종류

1. 인스턴스 메서드 → 인스턴스.메서드()
2. 클래스 메서드
3. 스태틱 메서드

![image.png](attachment:06aa20f3-bdf1-4779-bbcb-b6d6056d9122:image.png)

### 인스턴스 메서드

: 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드

→ 인스턴스의 상태를 조작하거나 동작을 수행

- 인스턴스 메서드 구조
    - 클래스 내부에 정의되는 메서드의 기본
    - 반드시 첫 번쨰 인자로 인스턴스 자신(self)을 받음
    - 인스턴스의 속성에 접근하거나 변경 가능
    
    ```python
    class MyClass:
    	def instance_method(self, arg1, ...):
    		pass
    ```
    
- self 동작 원리
    - upper 메서드를 사용해 문자열 ‘hello’를 대문자로 변경하기
        
        ```python
        'hello'.upper()
        ```
        
    - 하지만 실제 파이썬 내부 동작은 다음과 같이 진행됨
        
        ```python
        str.upper('hello')
        ```
        
    - str 클래스가 upper메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간것
    
    ⇒ 인스턴스 메서드의 첫 번쨰 인자가 자기자신인 이유
    
    ```python
    'hello'.upper()은 str.upper('hello')를 객체지향 방식의 메서드로 호출하는 표현
    ```
    
    ![자기자신의 변수값을 할당하면서 시작 가능](attachment:df7a5e11-936b-4203-b2a5-57436397c057:image.png)
    
    자기자신의 변수값을 할당하면서 시작 가능
    
    ```python
    class Counter:
        def __init__(self):
            self.count = 0
    
        def increment(self):
            self.count += 1
    
    c = Counter()
    print(c.count) # 0
    c.increment() # 호출
    print(c.count) # 1
    
    c2 = Counter()
    print(c2.count) # 0 
    # 인스턴스는 서로 독립적임 c.increment()랑은 아무상관x
    ```
    
- 생성자 메서드 활용
    
    ![다른 변수 이름인데 헷갈리니까 일반적으로 맞춤.. but 같은 건 아님!!!!](attachment:3792cdfd-ff0f-460c-a994-c740a40f43c3:image.png)
    
    다른 변수 이름인데 헷갈리니까 일반적으로 맞춤.. but 같은 건 아님!!!!
    
    ```python
    class Person:
        def __init__(self, name):
            # 왼쪽 name : 인스턴스 변수 name
            # 오른쪽 name : 생성자 메서드의 매개변수 이름
            self.name = name
            print('인스턴스가 생성되었습니다.')
    
        def greeting(self):
            # name이라는 변수는 정의된 적 x
            print(f'안녕하세요 {name}입니다.') # 에러 발생생
            # 정의된건 인스턴스 name
            print(f'안녕하세요 {self.name} 입니다.')
    
    person1 = Person('지민')  # 인스턴스가 생성되었습니다.
    person1.greeting()  # 안녕하세요. 지민입니다.
    # Person.greeting(person1) # 실제 내부 동작형태
    ```
    

### 클래스 메서드

: 클래스가 호출하는 메서드

→ 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

→ 인스턴스의 상태에 의존하지 않는 기능을 정의

- 클래스 메서드 구조
    - @classmethod 데코레이터를 사용하여 정의
    - 호출 시, 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
    - 클래스를 인자로 받아 클래스 속성을 변경하거나 읽는데 사용
        
        ```python
        class MyClass:
        
        	@classmethod
        	def class_method(cls, arg1, ...):
        		pass
        	# 인스턴스로 클래스 사용
        ```
        
- 클래스 메서드 활용
    
    ```python
    class Person:
        population = 0
    
        def __init__(self, name):
            self.name = name
            Person.increase_population()
    
        @classmethod
        def increase_population(cls):
            cls.population += 1  # Person.population 값이 호출될떄마다 +1 됨
    
    # 인스턴스 각각 생성
    person1 = Person('Alice')  #alice라는 이름을 가진 person1이라는 인스턴스 생성
    person2 = Person('Bob') # bob이라는 이름을 가진 person2라는 인스턴스 생성
    print(Person.population)  # 2
    
    Person.increase_population()
    print(Person.population) # 3
    ```
    

### 스태틱 메서드

(정적 메서드)

→ 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

- 스태틱 메서드 구조
    - @staicmethod 데코레이터를 사용하여 정의
    - 호출 시 자동으로 전달 받는 인자가 없음(self, cls를 받지 않음)
    - 인스턴스나 클래스 속성에 직접 접근하지 않는, ‘도우미 함수’와 비슷한 역할
    - 예시
        
        ```python
        class MathUtils:
        	@staticmethod
        	# 두 개의 값 받아서 덧셈 기능만 하면 되는 단독적인 함수(인스턴스나 클래스랑 아무상관x)
        	def add(a,b):
        		return a+b
        		
        # 엄연히 메서드이기때문에 클래스가 호출함)
        print(MathUtils.add(2,3)) # 5
        ```
        

### 입출금이 가능한 은행계좌 클래스 만들기

```python
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현

# BackAccount 호출 하자마자 owner랑 balance 두 개의 인스턴스가 생성됨
class BankAccount:
    interest_rate = 0.02  # 이자율: 모두 동일해야됨됨

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다!')

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0

# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner) # Alice
print(alice_acc.balance) # 1000

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500) 
print(alice_acc.balance) # 1500

alice_acc.withdraw(3000)
print(alice_acc.balance) # 1200
# 잔액 확인 (인스턴스 변수 참조)

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03) 
print(BankAccount.interest_rate) # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
print(BankAccount.is_positive(alice_acc.balance)) # True
```

클래스 → 모든 메서드를 호출할 수 있긴하나, 클래스 메서드랑 스태틱 메서드만 사용해야됨!!

인스턴스 → 모든 메서드를 호출할 수 있긴하나, 인스턴스 메서드만 사용해야됨!!

### 클래스와 인스턴스 간의 이름공간

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름공간 생성
- 인스턴스에서 특정 속성에 접근하면 : 인스턴스 → 클래스 순으로 탐색

![image.png](attachment:575a2626-a105-4aac-b568-ced07edbbe78:image.png)

- 독립적인 이름 공간을 가지는 이점
    - 각 인스턴스는 독립적인 메모리 공간을 가짐 → 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근 불가능
    - 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
    - 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
    
    ⇒ 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌
    

### 매직메서드

: double underscore(’__’가 있는 메서드는 특수한 동작을 위해 만들어진 메서드

- 인스턴트 메서드
- 특정 상황에 자동으로 호출됨
- = 스페셜 메서

ex. 

![image.png](attachment:98b61172-ccf3-4c29-963c-cfd9441826a9:image.png)

__str__(self) : 내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경

![image.png](attachment:c84d8fd5-efec-4b1f-bcd1-93b10fc81763:image.png)

### 데코레이터

: 다른 함수의 코드를 유지한 채로(원본은 유지!!) 수정하거나 확장하기 위해 사용되는 함수

![image.png](attachment:8cd29491-d8c5-49e4-a680-6b22b2581b65:image.png)