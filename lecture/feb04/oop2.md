## 상속

한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려 받는 것

- 상속이 필요한 이유
    1. 코드 재사용
        - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
        - 기존 클래스를 수정하지 않고도 기능 확장 가능
    2. 계층 구조
        - 상속을 통해 클래스들 간의 계층구조를 형성할 수 있음
        - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
    3. 유지 보수의 용이성
        - 상속을 통해 기존 클래스의 수정이 필요한 겨우, 해당 클래스만 수정하면 되므로 유지보수가 용이해짐
        - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

```python
class Animal:
	def eat(self):
		print('먹는 중')

class Dog(Animal): # 상속
	def bark(Self):
		print('멍멍')
		
my_dog = Dog()

my_dog.bark() #멍멍

# 부모 클래스(Animal)에서도 메서드 사용 가능
my_dog.eat()

```

자식 클래스의 메소드를 부모클래스에서 사용할수는 x!!

```python
my_cat = Animal()
my_cat.bark() # AttributeError: 'Animal' object has no attribute 'bark'
```

```python
# 상속 없는 경우 - 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.

# 상속 없는 경우 - 2
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

# 상속을 사용한 계층구조 변경
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

# 인스턴스 생성

# 부모 Person 클래스의 talk 메서드를 활용

# 부모 Person 클래스의 talk 메서드를 활용
```

### 메서드 오버라이딩

: 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것

- 메서드 오버라이딩 예시
    
    자식 클래스가 부모 클래스의 메서드를 덮어써서 새로운 동작 구현 가능
    
    ```python
    class Animal:
    	def eat(self):
    		print('Animal이 먹는 중')
    
    class Dog(Animal):
    	# 부모 클래스(Animal)의 eat 메서드를 재정의(오버라이딩)
    	def eat(self):
    		print('Dog가 먹는 중')
    	
    my_dog = Dog()
    my_dog.eat() # Dog가 먹는 중
    ```
    

### [참고] 오버로딩(Overloading)

- 같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것( 파이썬은 미지원)
- 파이썬은 실제로 하나의 메서드만 인식. 인자의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않음 (마지막으로 선언된 메서드만 인식)

![image.png](attachment:1f7c5cec-5e6a-4dfa-9db5-8a31de0cee37:image.png)

## 다중 상속

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우, 상속 순서에 의해 결정됨
    
    (우선순위가o)
    
- 먼저상속 받는 다는건,, 가깝다는 뜻인듯..?
- 다중 상속 예시
    
    ```python
    class Person:
    	def __init__(self, name):
    		self.name = name
    	
    	def greeting(self):
    		return f'안녕, {self.name}'
    
    class Mom(Person): # 상속 1
    	gene = 'XX'
    	
    	def swim(self):
    		return '엄마가 수영'
    
    class Dad(Person):
    	gene = 'XY'
    	
    	def walk(self):
    		return '아빠가 걷기'
    
    class FirstChild(Dad, Mom):
    	def swim(self):
            return '첫째가 수영'
    
      def cry(self):
            return '첫째가 응애'
            
    baby1 = FirstChild('아가')
    print(baby1.cry()) # 첫째가 응애
    print(baby1.swim()) # 첫째가 수영
    print(baby1.walk()) # 아빠가 걷기
    print(baby1.gene()) # XY !!!!!!!!!!!!!!!!!!!!!
    
    ```
    
    ![image.png](attachment:e822b5c5-15a6-46a1-89b9-b49f78c84050:image.png)
    
    겹치면 먼저 상속 받는게 우선순위가 높음!!
    
    먼저 상속 받는다: class Firstchild(Dad, Mom): → Dad를 먼저 상속받는 것!
    
- 다이아몬드 문제
    
    
    ![image.png](attachment:646c653e-5d0d-415f-bf7d-5c26359a4437:image.png)
    
    ![image.png](attachment:e6470dd2-c8c6-46ef-9639-e240ad84edcc:image.png)
    
    - 파이썬에서의 해결책
        
        MRO(Method Resolution Order) 알고리즘 → 클래스 목록 생성
        
        - 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
        - 그래서, 속성이 D에서 발견되지 않으면, B에서 찾고, 거기에서도 발견되지 않으면, C에서 찾고, 이런식으로 진행됨
            
            ```python
            class D(B, C):
            	pass
            ```
            
            ![image.png](attachment:288d7b08-a85d-4856-a8f4-ce9487eb466a:image.png)
            

### MRO

:파이썬이 메서드를 찾는 순서에 대한 규칙. 메서드 결정 순서

### super()

: 부모 클래스(또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수

- super() 기능
    - 다중 상속 상황에서 특히 유용, MRO를 따르기 떄문에 여러 부모 클래스를 가진 자식 클래스에서 다음에 호출해야 할 부모 메서드를 순서대로 호출할 수 있게 함

```python
# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        super().__init__(name, age, number, email) # 여기서 self는 빼줘야됨
        Person.__init__(name, age, number, email) # 얘도 실행됨. super()랑 똑같음.
        # 단일 상속에서는 super()가 크게 필요하진 x
        # 부모 클래스의 이름이 바뀌어 버리면 위로 다 찾아다니면서 가져와야되는데, super()를 쓰면 그럴필요x

        '''
        super()를 통해 아래 네줄을 한줄로 줄임!!
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        '''
        self.student_id = student_id
```

- super의 2 가지 사용 사례
    1. 단일 상속 구조
        - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지관리하기 쉬움
        - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요
    2. 다중 상속 구조
        - MRO를 따른 메서드 호출
        - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지
- super() 사용 예시(다중 상속)
    
    ```python
    # 다중 상속
    class ParentA:
        def __init__(self):
            super().__init__() # 모든 객체는 사실 object라는 최상위 부모가 있음..  
            self.value_a = 'ParentA'
    
        def show_value(self):
            print(f'Value from ParentA: {self.value_a}')
    
    class ParentB:
        def __init__(self):
            self.value_b = 'ParentB'
    
        def show_value(self):
            print(f'Value from ParentB: {self.value_b}')
    
    class Child(ParentA, ParentB): # A를 먼저 상속받음음
        def __init__(self):
            super().__init__()  # ParentA 클래스의 __init__ 메서드 호출 -> super()는 MRO 알고리즘에 따른 순서에 의한 호출이므로
            self.value_c = 'Child'
    
        def show_value(self):
            super().show_value()  # ParentA 클래스의 show_value 메서드 호출
            print(f'Value from Child: {self.value_c}')
    
    # MRO 순서 상 child - A - B 순서임 -> super()는 이 로직을 보장하므로
    # ParentA에서 super()를 사용하면 B의 __init__을 가져옴
    # super() 호출이 child에서 시작이되니까 parentA에서도 super()호출이 가능한 것임
    # 그럼 child에서 super() 호출을 안하면 ParentA에서 먼저 super() 호출을 하면 B 말고 object에서 가져오나????????
    
    child = Child()
    child.show_value()
    """
    Value from ParentA: ParentA
    Value from Child: Child
    """
    
    print(child.value_c)  # Child
    print(child.value_a)  # ParentA
    print(
        child.value_b
    )  # AttributeError: 'Child' object has no attribute 'value_b'
    # value_a에서 MRO가 끊겨서 child는 value_b 가 없음음
    
    """
    <ParentA에 super().__init__()를 추가하면?>
    그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
    그러면 print(child.value_b)는 ParentB를 출력하게 됨
    
    print(child.value_b)  # ParentB
    """
    
    """
    <Child 클래스의 MRO>
    Child -> ParentA -> ParentB
    
    super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
    MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴
    
    따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
    """
    
    """
    1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
        1.	child = Child() 호출 시, Child.__init__()가 실행
        2.	Child.__init__() 내부에서 super().__init__()를 호출
            - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
        3.	ParentA.__init__()로 진입
    
    1.2. ParentA.__init__() 내부
    	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
    	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
        3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
    	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
    	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
    	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료
    
    1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
    	- child.value_a → 'ParentA'
    	- child.value_b → 'ParentB' 
    	- child.value_c → 'Child'
    """
    ```
    

- super()의 이점
    - 다중 상속 상황에서 super()는 다음에 호출해야 할 부모 메서드를 MRO 순서에 따라 결정하기 때문에, 명시적으로 특정 부모 클래스를 가리키지 않고도 올바른 순서로 부모 초기화나 메서드 호출 가능
    - 이를 통해 복잡한 상속 구조에서도 코드를 유연하고 깔끔하게 유지가능

- **ClassName.__mro__ 또는 ClassName.mro()** 를 확인해 MRO 순서 파악한 뒤 적절히 활용하는 연습을 하면, 보다 복잡한 상속 구조에서도 코드 관리 가능!!!!

- MRO의 필요 이유
    - 각 부모를 한 번만 호출하고, 우선순위에 영향 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성
    - 신뢰성있고, 확장성있는 클래스 설계 도움
    - 클래스 간의 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성과 유지보수성 향상

# 에러와 예외

## 디버깅

### 버그

: 소프트웨어에서 발생하는 오류 또는 결함. 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### Debugging

: 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정. 프로그램의 오작동 원인을 식별하여 수정하는 작업

- 디버깅 방법
    1. print 함수 활용
    2. 개발환경(text editor, IDE) 등에서 제공하는 기능
    3. python tutor 활용 …

### 에러

: 프로그램 실행 중에 발생하는 예외 황

- 파이썬의 에러 유형
    1. 문법에러(syntax error) : 프로그램의 구문이 올바르지 않은 경우 → 실행x
    2. 예외(exception): 프로그램 실행 중에 감지되는 에러 → 실행은 됨
        1. 내장 예외: 예외 상황을 나타내는 예외 클래스들
            
            → 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
            

### 예외 처리

: 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리되도록 하는 방법

- 예외처리 사용 구문
    - try : 예외가 발생할 수 있는 코드 작성
    - except: 예외가 발생했을 때 실행할 코드 작성
        
        ⇒ 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동
        
    - else: 예외가 발생하지 않았을 때 실행할 코드 작성
    - finally: 예외 발생 여부와 상관없이 항상 실행할 코드 작성

```python
try:
	x = int(input('숫자를 입력하세요: '))
	y = 10/x
except ZeroDivisionError:
	print('0으로 나눌 수 없습니다.')
```

### 복수 예외처리

```python
try:
	num = int(input('100으로 나눌 값을 입력하시오 : '))
	print(100/num)

# 한 번에 입력
except (ValueError, ZeroDivisionError):
	print('다시 입력하세요')
	
	
# 나눠서 입력
except ValueError:
	print('숫자를 입력하세요')
except ZeroDivisionError:
	print('0으로는 나눌 수 없습니다.')
except:
	print('에러가 발생했습니다.')
```

- 내장 예외의 상속 계층구조 주의
    
    ![image.png](attachment:225d2054-37d1-4faf-b25b-f61be5031721:image.png)
    
    - 내장 예외 클래스는 상속 계층 구조를 가지기 떄문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인할 수 있도록 작성해야 함
    
    ```python
    # 옳은 코드
    # 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
        print(100 / num)
    # 1) 구체적인 예외부터
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('숫자를 넣어주세요.')
    # 2) 마지막에 광범위한 예외(Exception)
    except Exception:
        print('에러가 발생하였습니다.')
    ```
    

- as 키워드
    - 예외 객체 : 예외가 발생했을 때 예외에 대한 정보를 담고 있는 객체
    
    → except 블록에서 예외 객체를 받아 상세한 예외 정보 활용가능
    
    ```python
    my_list = []
    
    try :
    	number = my_list[1]
    except IndexError 
    	
    ```
    
- try-except와 if-else
    - try-except와 if-else를 함께 사용 가능
        
        ```python
        try:
        	x = int(input('숫자를 입력하세요: '))
        	if x < 0:
        		print('음수는 허용되지 않습니다.')
        	else:
        		print('입력한 숫자:', x)
        except ValueError:
        	print('오류 발생')
        ```
        

- 예외처리와 값 검사에 대한 2가지 접근 방식
    1. EAFP(Easier to Ask for Forgiveness than Permission)
        
        : 예외 처리를 중심으로 코드를 작성하는 접근 방식 (try-except)
        
        → 일단 실행해. 그러고 나중에 에러가 발생하면 처리하겠다
        
    2. LBYL(Look Before You Leap)
        
        : 값 검사를 중심으로 코드를 작성하는 접근 방식 (if-else)
        
        → 에러를 먼저 고려하겠다. 
        
    
    ![image.png](attachment:88c051f0-4488-4d3f-a526-175eafac3701:image.png)