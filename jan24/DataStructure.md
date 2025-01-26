## Data structure

### 데이터 구조(Data structure):  여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict 등)

= 자료 구조 : 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

### 메서드: 객체에 속한 함수

(종속!)

→ 객체의 상태를 조작하거나 동작 수행

- 메서드 특징
    1. 클래스 내부에 정의되는 함수
        - 클래스: 파이썬에서 ‘타입을 표현하는 방법’
    2. 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재

```python
#함수
def add(a,b):
	return a+b

#메서드
class Calculator:
	def add(self, a, b):
		return a+b
		
#함수 호출
add(1,2)

#메서드 호출
a = Calculator()
a.add(1,2)
```

### 메서드 호출 방법

⇒ 데이터타입객체.메서드()

ex. ‘hello’.capitalize()

- **문자열 조회/탐색 및 검증 메서드**
    1. **s.find(x)**: x의 첫 번째 위치를 반환. 없으면, -1을 반환
    2. **s.index(x)**: x의 첫 번째 위치를 반환. 없으면, 오류 발생
    3. **s.isupper()**: 문자열 내의 모든 문자가 대문자인지 확인
    4. **s.islower()**: 문자열 내의 모든 문자가 소문자인지 확인
    5. **s.isalpha()**: 문자열 내의 모든 문자가 알파벳인지 확인
        - 단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)

- 문자열 조작 메서드(새 문자열 반환)
    1. **s.replace(*old, new[,count]*):** 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
        - count를 안넣으면 여러 개 일치 시, 전체 다 바꿈
        
        ```python
        text = 'Hello, world! world world'
        new_text1 = text.replace('world', 'Python')
        new_text2 = text.replace('world', 'Python', 1) # 1은 바꿀 개수
        print(text) # Hello, world! world world (문자열은 불변. 원본자체가 바뀌진x)
        print(new_text1) # Hello, Python! Python Python
        print(new_text2) # Hello, Python! world world
        ```
        
    2. **s.strip(*[chars]*)**: 문자열의 시작과 끝에 있는 공백이나 특정 문자를 제거
        
        ```python
        text = '   Hello, world!    '
        new_text = text.strip()
        print(new_text) # 'Hello,world'
        ```
        
    3. **s.split(*sep=None, maxsplit=-1*)**: sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환
        
        ```python
        text = 'Hello, world!'
        words1 = text.split(',')
        words2 = text.split()
        print(words1) #['Hello', ' world!'] #,기준으로 나눠서 ,가 사라짐
        print(words2) #['Hello,', 'world!'] #공백 기준으로 나눠서 공백이 사라짐
        ```
        
    4. ***‘separator’*.join(*iterable*)**: iterable의 문자열을 연결한 문자열을 반환
        
        ```python
        words = ['Hello', 'world!']
        text = '-'.join(words)
        print(text) # 'Hello-world!'
        
        words = ['Hello', 'world!', '3', '100']
        ```
        
    5. s.caplitalize(): 가장 첫 번째 글자를 대문자로 변경
    6. s.title():  문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
    7. s.upper(): 모두 대문자로 변경
    8. s.lower(): 모두 소문자로 변경
    9. s.swapcase(): 대↔소문자 서로 변경
    

### 리스트

- 리스트 값 추가 및 삭제 메서드
    1. L.append(x): 리스트 마지막에 항목 x를 추가
        - 원본이 바뀜!!
        
        ```python
        my_list = [1,2,3]
        my_list.append(4)
        print(my_list) # [1,2,3,4]
        
        print(my_list.append(4)) # None -> 반환하는게 없음. 원본을 수정!!
        ```
        
        ⚠️ 앞에 문자열 조작 메서드에서는 새 문자열을 반환했음
        
    2. L.extend(*iterable*): iterable 의 모든 항목들을 리스트 끝에 추가 (+=와 같은 기능)
        
        ⚠️ 반복 가능한 객체가 아니면 추가 불가
        
        ```python
        my_list = [1,2,3]
        my_list.extend([4,5,6])
        #[4,5,6]을 하나하나 풀어서 추가함
        print(my_list) # [1,2,3,4,5,6]
        
        # append와의 비교
        #[4,5,6]을 하나로 취급해서 그대로 넣음
        my_list.append([4,5,6])
        print(my_list) #[1,2,3,4,5,6,[4,5,6]]
        # [1,2,3] += [4,5,6] 과 같은 동작
        ```
        
    3. .insert(*i,x*) : 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
        
        ```python
        my_list = [1,2,3]
        my_list.insert(1,5)
        print(my_list) # [1,5,2,3]
        ```
        
    4. .remove(x): 리스트에서 첫 번째로 일치하는 항목을 삭제
        
        ```python
        my_list = [1,2,3,2,2,2]
        my_list.remove(2)
        print(my_list) # [1,3,2,2,2]
        ```
        
    5. .pop(i): 리스트에서 지정한 인덱스의 항목을 제거하고 반환. 작성하지 않을 경우 마지막 항목을 제거
        
        ```python
        my_list = [1,2,3,4,5]
        
        item1 = my_list.pop() # item1에 할당. 반환값이 있다는 것!
        item2 = my_list.pop(0)
        
        print(item1) #5
        print(item2) #1
        print(my_list) = [2,3,4]
        ```
        
    6. .clear() : 리스트의 모든 항목을 삭제
        - 리스트 자체를 삭제하는 건 아님. 빈 리스트로 만드는 것 (반환은xxx)
        
        ```python
        my_list = [1,2,3]
        my_list.clear()
        print(my_list) # []
        ```
        
- 리스트 탐색 및 정렬 메서드
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/e4f6f78b-2d4a-4c58-a212-a7d484e5be5d/image.png)
    
    1. **.index(x)**: 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
        
        ```python
        my_list = [1,2,3]
        index = my_list.index(2)
        print(index) # 1
        ```
        
    2. **.count(x)** : 리스트에서 항목 x의 개수를 반환
        
        ```python
        my_list = [1,2,2,3,3,3]
        count = my_list.count(3)
        print(count) #3
        ```
        
    3. **.reverse()** : 리스트의 순서를 역순으로 변경 (정렬x)
        
        ```python
        my_list = [1,3,2,8,1,9]
        my_list.reverse()
        print(my_list.reverse()) #None -> 반환은 x
        print(my_list) #[9,1,8,2,3,1]
        ```
        
    4. **.sort()** : 원본 리스트를 오름차순으로 정렬
        
        ```python
        my_list = [3,2,100,1]
        my_list.sort()
        print(my_list) # [1,2,3,100]
        
        # 내림차순 정렬
        my_list.sort(reverse=True)
        print(my_list) # [100,3,2,1]
        ```
        

## 복사

→ 모습만 같고 메모리의 다른 곳을 바라봐야됨 (서로 다른 객체!)

### 객체와 참조

**가변/불변 객체 개념**

1. Mutable(가변) 객체: 생성 후 내용을 변경할 수 있는 객체
    
    ex. 리스트(list), 딕셔너리(dict), 집합(set)
    
    - 예시
        
        ```python
        a = [1,2,3,4]
        b = a # 값을 할당한게 아니라, a가 가지고 있던 주소를 할당한 것
        b[0] = 100 # a,b는 같은 주소의 같은 리스트를 지정하므로 b를 바꾸면 a도 바뀜
        
        print(a) # [100,2,3,4]
        print(b) # [100,2,3,4]
        print(a is b) # True
        ```
        
    - 생성 후에도 내용 수정 가능
    - 객체 내용이 변경돼도 같은 메모리 주소 유지
2. Immutable(불변) 객체 : 생성 후 내용을 변경할 수 없는 객체
    
    ex. 정수(int), 실수(float), 문자열(str), 튜플(tuple)
    
    - 예시
        
        ```python
        a = 20
        b = a
        b = 10
        
        print(a) # 20
        print(b) # 10
        print(a is b) # False
        ```
        
    - 생성 후 그 값을 변경 할 수 x
    - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

- **변수 할당**: 객체에 대한 참조를 생성하는 과정
    - 변수는 객체의 메모리 주소를 가리키는 Label 역할을 함
    - ‘=’ 연산자를 사용하여 변수에 값을 할당
    - 할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성됨

**메모리 참조 방식**

- 변수는  객체의 ‘메모리 주소’를 저장
- 여러 변수가 동일한 객체를 참조 가능

- id() 함수를 사용한 메모리 주소 확인
    - id() 함수를 사용하여 객체의 메모리 주소 확인 가능
    - is 연산자를 통해 두 변수가 같은 객체를 참조하는지 확인 가능
    
    ```python
    x = [1,2,3]
    y = x
    z = [1,2,3]
    
    print(id(x))
    print(id(y))
    print(id(Z))
    ```
    
- 이러한 동작 방식의 이유
    1. 성능 최적화
        - 불변 객체는 변경이 불가능. 여러 변수가 같은 객체를 안전하게 공유 가능
        - 가변 객체는 내용 수정이 빈번한 경우 새 객체를 생성하지 않고 직접 수정하여 성능 향상시킴
    2. 메모리 효율성
        - 불변 객체는 동일한 값을 가진 여러 객체가 메모리를 공유할 수 있어 효율적
        - 가변 객체는 크기가 큰 데이터를 효율적으로 수정 가능

### 얕은 복사(Shallow Copy)

: 객체의 최상위 요소만 새로운 메모리에 복사하는 방법

→ 내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨

(새로운 메모리로 복사하는게 아니라 참조만)

- 얕은 복사 구현 방법
    1. 리스트 슬라이싱
    2. copy() 메서드
    3. list() 함수
    
    ```python
    a = [1,2,3]
    b = a[:] # 슬라이싱
    c = a.copy() # copy메서드
    d = list(a) # list() 함수
    ```
    
- 얕은 복사의 한계
    - 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우
    
    ```python
    a = [1,2,[3,4,5]]
    b = a[:]
    
    b[0] = 999
    print(a) # [1,2,[3,4,5]]
    print(b) # [999,2,[3,4,5]]
    
    # a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨!!!
    b[2][1] = 100
    print(a) # [1,2,[3,100,5]]
    print(b) # [999,2,[3,100,5]]
    print(a[2] is b[2]) # True
    ```
    
- 1차원 리스트와 다차원 리스트에서의 차이점
    - 1차원 리스트: 얕은 복사로 충분히 독립적인 복사본을 만들 수 있음
    - 다차원 리스트: 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체를 참조

### 깊은 복사(Deep Copy)

: 객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법. 중첩된 객체까지 모두 새로운 객체로 생성됨

- copy 모듈에서 제공하는 deepcopy() 함수를 사용
    
    ```python
    import copy
    
    new_object = copy.deepcopy(original_object)
    ```
    
- 예시
    - 복잡한 중첩 객체 예시
        
        ```python
        print('\n복잡한 중첩 객체 깊은 복사')
        original = {
        	'a' : [1,2,3],
        	'b' : {'c': 4, 'd': [5,6]}
        	}
        
        copied = copy.deepcopy(original)
        
        print(f'원본: {original}') # {'a': [1,2,3], 'b': {'c':4, 'd':[5,6]}}
        print(f'복사본: {copied}') # {'a': [1,100,3], 'b': {'c':4, 'd':[500,6]}}
        print(original['b'] is copied['b']) # False
        
        				 
        ```
        

---

### ➕ 메서드 체이닝

: 여러 메서드를 연속해서 호출하는 방식

(순서는 작성하는것부터 실행됨)

- 예시
    - 문자열에서의 메서드 체이닝 예시
        
        ```python
        text = 'heLLo, woRld!'
        new_text = text.swapcase().replace('l','z')
        print(new_text) # HEzzO, WOrLD!
        ```
        
        - 코드는 다음 순서대로 실행됨
            1. text.swapcase(): 대소문자를 반전시킴
            2. .replace(’l’, ‘z’):  소문자 ‘l’을 ‘z’로 교체
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/bc4584d8-bccd-4ef9-a1d9-22737d89caab/image.png)
        

⚠️ 주의!!!

먼저 실행되는 메소든데, 반환값이 없는 경우

```python
result = numbers.append(7).extend([8,9]) # AttributeError
#.append()는 반환x -> None이 반환됨..
```

```python
# 리스트 조작에서 메서드 체이닝을 사용할 때는 각 메서드의 
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers) 
```

- 모든 메서드가 체이닝을 지원하는 것은x
    - 메서드가 객체를 반환할 때만 사용 가능
- None을 반환하는 메서드는 메서드 체이닝이 불가능
    
    ex. 리스트의 append(), sort()
    
- 메서드 체이닝을 사용할 때는 각 메서드의 반환 값을 잘 이해하고 있어야 함.

### ➕ 문자 유형 판별 메서드

- isdemical() : 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit(): isdemical()과 비슷하지만, 유니코드 숫자도 인식
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/ba851ca3-5d88-4550-9b49-4eac1c5751ba/image.png)
    
- isnumeric(): isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식
    
    (분수, 지수, 루트 기호도 숫자로 인식)
    

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/14815a73-485d-4817-8793-02478d45b8e7/image.png)