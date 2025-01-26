## sequence types

:여러 개의 값들을 순서대로 나열하여 저장하는 자료형 (but, 정렬은 xx)

### 1. str

[basic syntax1](https://www.notion.so/basic-syntax1-1805477005b0808ca2b9f4b1a4bf13dc?pvs=21) 

### 2. list: 여러 개의 값을 순서대로 저장(시퀀스 특징) 하는 변경 가능한(문자열과의 차이점) 시퀀스 자료형

- 가변!!
- 리스트 표현
    - 0개 이상의 객체 포함, 데이터 목록 저장
    - 어떤 자료형도 저장 가능
    - 대괄호([])로 표기

```python
my_list_1  []
my_list_2 = [1, 'a', 3, 'b', ['ab', 3]]
```

⚠️ 뒤집는 것 ≠ 내림차순 !!!!!!!!!!!!!

- 예제
    
    ```python
    my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
    
    #!!! 출력
    print(my_list[4][2])
    print(my_list[-1][-1])
    print(my_list[4][-1])
    ..
    
    #w 출력
    print(my_list[4][1][0])
    ```
    
    ```python
    my_list = [1,2,3]
    my_list[0] = 100
    >> [100,2,3]
    
    ```
    

➕ 리스트[주소1→요소주소1, 주소2→요소주소2, 주소3→요소주소3]

(리스트의 각 방은 주소를 따로 가지고 그 안에 들어가는 내용은 또 각자 따로 주소를 가짐.. 주소 안에 주소.. 이런느낌..)

→ 리스트의 요소 변경할 경우, 리스트[주소1→요소주소1, 주소2-요소주소4, 주소3→요소주소3]

리스트: 값들의 주소를 가지고 있는 형태.., 리스트의 주소가 바뀌는 것은 x

리스트 값의 주소는 연속x (가끔 컴퓨터가 최적화를 위해 연속하게 할 때가 있는데 원칙은 연속x)

### 3. tuple: 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형

- 튜플 표현
    - 0개 이상의 객체 포함, 데이터 목록 저장
    - 소괄호(())로 표기
    - 데이터는 어떤 자료형도 저장할 수 있음
    
    ❗리스트와의 차이점: 변경 불가능
    
    - 단일 요소 튜플을 만들 때는 반드시 trailing comma(후행쉼표)를 사용해야 함
        - Trailing Comma
            - 컬렉션의 마지막 요소 뒤에 붙는 쉼표
            - 일반적으로 작성은 선택사항임
            - 단, 하나의 요소로 구성된 튜플을 만들 때는 필수
            - Trailing comma 기본 규칙
                - 각 요소를 별도의 줄에 작성
                - 마지막 요소 뒤에 trailing comma 추가
                - 닫는 괄호는 새로운 줄에 배치
                    
                    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/e9e31a80-9934-4a1c-ba42-4703e83c8ace/image.png)
                    
        - 여러 개 일 때는 상관x
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/9fefce54-e631-45e4-888e-d71741df1a81/image.png)
        
        (1) → int
        
        (1,) → tuple
        
- 개발자가 직접 활용하는 타입은 x, 개발할 때 직접쓰는 경우 거의x
- 튜플의 불변 특성을 사용하여 내부 동작과 안전한 데이터 전달에 사용됨
    
    ex. 다중 할당, 값 교환, 그룹화, 함수 다중 반환 값 등
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/3714a7b7-fe89-4a98-a9a5-4ec341d6ab88/image.png)
    

### 4. range: 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형

range 기본구문: **range(시작 값, 끝 값, 증가 값)**

→ 함수 형태이면서 시퀀스 타입을 가짐..

- 모든 매개변수는 정수만 사용 가능
- range 매개변수별 특징
    - range(n): 0부터 n-1까지 1씩 증가
    - range(n, m): n부터 m-1까지의 1씩 증가
    - range(n, m, step): n부터 m-1까지 step 만큼 증가

- 증가 값 규칙
    - 기본 증가 값 = 1
    - 음수 증가 값 → 감소하는 수열 생성
    - 양수 증가 값 → 증가하는 수열 생성
    - 증가 값이 0이면 error!
- 값의 범위 규칙
    - 음수 증가 시 → 시작 값이 끝 값 보다 커야 함
    - 양수 증가 시 → 시작 값이 끝 값 보다 작아야 함
    
    ![(음수 증가) 시작 보다 끝 값이 작은 경우, 그냥 아무것도 생성되지 않음](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/b35c4011-1a8a-4d5d-a667-086e558154cb/image.png)
    
    (음수 증가) 시작 보다 끝 값이 작은 경우, 그냥 아무것도 생성되지 않음
    

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/41d8f9d5-2bdf-41ab-9af5-4974472fe521/image.png)

→ 위에꺼는 총 9번 동작 / 아래는 총 5번 동작 (하나씩 뱉어내는 것임)

## Non-sequence types

### 1. dict: key-value 쌍으로 이루어진 순서와 중복이 없는(key기준) 변경 가능한 자료형

- value값은 중복 가능
- 딕셔너리 표현
    - key는 변경 불가능한 자료형만 사용 가능 (str, int, float, tuple, range.. )
    - value는 모든 자료형 사용 가능
    - 중괄호({})로 표기
    
- 딕셔너리 사용
    
    : key를 통해 value에 접근
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/165af1c8-c331-472f-bbda-0133dc4ac7ca/image.png)
    
    - ‘list’는 딕셔너리의 몇 번 째 key?
        
        ❗key 간에는 순서xxxxxxx
        
    
    ```python
    print(my_dict['list'][1]) #2
    ```
    

### 2. set: 순서와 중복이 없는 변경 불가능한 자료형

- 수학에서의 집합과 동일한 연산 처리 가능
- 중괄호({})로 표기
    
    ⭐ 빈세트 만들기 → set()
    
    - 중괄호는 딕셔너리에서도 쓰기 때문에 ,, 딕셔너리한테 밀림
    - 세트 안에 요소가 있으면 그냥 중괄호 쓰면 됨

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/b54539ef-a415-4b2f-a164-8546d61abab9/image.png)

- 세트의 집합 연산
    
    ```python
    my_set_1 = {1,2,3}
    my_set_2 = {3,6,9}
    
    #합집합
    print(my_set_1 | my_set_2) #{1,2,3,6,9}
    
    #차집합
    print(my_set_1 - my_set_2) #{1,2}
    
    #교집합
    print(my_set_1 & my_set_2) #{3}
    ```
    

➕ 리스트를 set로 형변환 해주면 중복 다 사라짐..

→ 중복제거 용도로 set 많이 씀

→ list 보다 set가 빠름 (이유는 나중에,,)

## Other types

### None: 파이썬에서 ‘값이 없음’을 표현하는 자료형

- N → 반드시 대문자여야함

### Boolean: 참(True)와 거짓(False)을 표현하는 자료형

- 비교/논리 연산의 평가 결과로 사용됨
- 주로 조건/반복문과 함께 사용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/e1701eb2-868e-47f2-8859-dd6b6c9095ad/image.png)

## Collection

:여러 개의 항목 또는 요소를 담는 자료 구조

→ str, list, tuple, set, dict

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/9e0cd74a-6f08-4810-ab7c-bfc59f988bb9/image.png)

→ dict의 변경가능 여부는 값 얘기하는 것. key는 변경 불가

---

## 형변환

: 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

→ 암시적 형변환 / 명시적 형변환

### 암시적 형변환

- 정수와 실수의 연산에서 정수가 실수로 변환됨
- Boolean 과 Numeric Type에서만 가능

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/f3852e7b-e6be-4435-8aa5-d61ebca3649e/image.png)

→ True: 1, False: 0 으로 인식

### 명시적 형변환

:프로그래머가 직접 지정하는 형변환

→ 암시적 형변환이 아닌 모든 경우를 포함

- str → int : 형식에 맞는 숫자만 가능
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/0717c212-71be-4984-865d-383524c7f70c/image.png)
    
- int → str: 모두 가능
    
    ```python
    print(str(1) + '등') #1등
    ```
    

## 연산자

### 복합 연산자

: 연산과 할당이 함께 이뤄짐

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/772d4671-db87-4ef7-9874-4c3296ddc9f0/image.png)

### 비교 연산자

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/7110d5b3-cf9f-4c13-844c-d1f590113236/image.png)

1. **== 비교 연산자** : 값(데이터)가 같은지를 비교, ‘동등성(equality)’
    
    print(1 == True) >> True
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/3a8c5da0-7316-4a93-8529-d7a465583667/image.png)
    

1. **is 비교 연산자** : 객체 자체가 같은지를 비교, ‘식별성(identity)’
    - 두 변수가 동일한 메모리 주소(레퍼런스)를 가리키고 있을 때만 True
    - ==비교 연산자보다 엄격
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/49608036-3c91-4f1f-a02f-89fb1073d045/image.png)
    

- 왜 is 대신 ==를 사용해야 하나? (== 사용을 더 권장)
    - is 는 객체의 식별성(identities)을 비교 → 숫자나 문자열 같은 값 자체를 비교하려는 상황에서는 적절하지 x
    - is 연산자를 이용하면 코드 상에서 의도치 않게 False가 나오거나 파이썬 버전에 따라 내부 구현 차이 때문에 기대하는 결과가 달라질 수 있음
    - 예를 들어, 다음 코드에서 is를 사용하면 항상 False가 나오지만 실제로 데이터 값은 논리적으로 같기 떄문에 ==를 써야 의미가 더 맞음
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/20389a78-3638-4a6d-a77c-1c59fcef685c/image.png)
        
- is 연산자를 사용하는 경우
    
    1**. None 비교**
    
    - 같은 주소에 있는가? 라는 질문에 답해야 할 떄
    - 파이썬 공식 스타일 가이드 → None 비교할때 ==대신 is 사용하라고 구너장
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/7af18b3c-8ab2-428d-a427-70690a06e78b/image.png)
    
    **2. 싱글턴(Singleton) 객체** : 프로그램 전체에서 오직 1개만 존재하도록 만들어진 특별한 객체
    
    - None, True, False
    
    → 파이썬 전체에서 딱 1개만 사용됨, 새로 만들어지는게 아니라 미리 정해진 하나의 객체가 재사용 → 여러 곳에서 쓰더라도 같은 메모리 주소 가리킴
    
    1. 리스트나 객체 비교
        - 리스트 또는 다른 가변 객체 비교할 때
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/81975aed-3312-4626-83c6-3397b0082fe4/image.png)
        

### 논리 연산자

and : 논리곱 → 두 피연산자 모두 True인 경우에만 전체가 True

or: 논리합 → 두 연산자 중 하나라도 True 인 경우, 전체가 True

not: 논리부정 → 단일 피연산자를 부정

### 단축평가⭐

![F/T/5/0/0/0/5/3/3/0](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/19250aaa-a8a2-43d2-a240-48e828170c5c/image.png)

F/T/5/0/0/0/5/3/3/0

빈 문자열 → False

문자열 안에 문자가 들어있으면 → True

**(최종 평가 값이 반환되는게 원칙)**

‘b’ in vowels?

‘a’ in vowels?

- or 는 하나라도 True면 True 반환
- 풀이
    1. print((’a’ and ‘b’) in vowels)
        
        → ‘a’ and ‘b’ → True and True → True
        
        → ‘b’ 반환 ⇒ ‘b’ in vowels? ⇒ False
        
    2. print((’b’ and ‘a’) in vowels)
        
        → ‘b’ and ‘a’ → True and True → True
        
        → ‘a’반환 ⇒ ‘a’ in vowels? ⇒ True
        
    3. print(3 and 5) 
        
        → True and True → True ⇒ 5
        
    4. print(3 and 0)
        
        → True and False → False ⇒ 0 (얘는 끝까지 확인했음)
        
    5. print(0 and 3)
        
        → False and (단축평가) → False ⇒ 0
        
    6. print(3 or 0)
        
        → True or (단축평가) → True ⇒ 3
        
    7. print(5 or 3)
        
        → True or (단축평가) → True ⇒ 5
        

단축 평가 목적→ 최적화

- 단축평가 동작
    1. and
        - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정
            
            두 번째 피연산자는 평가되지 않고, 그 값이 무시됨
            
        - 첫 번째 피연산자가 True인 경우, 전체 표현식은 두 번째 피연산자에 의해 결정
            
            두 번쨰 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
            
    2. or
        - 첫 번째 피연산자가 True 인 경우, 전체 표현식은 True로 결정
            
            두 번째 피연산자 무시
            
        - 첫 번째 피연산자가 False인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정

### 멤버십 연산자

특정 값이 시퀀스나 다른 컬렉션에 속하는 지 여부를 확인

→ in / not in

### 시퀀스형 연산자

: +와 *는 시퀀스 간 연산에서 산술연산자일때와 다른 역할을 가짐

- +: 결합
- *: 반복

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/da2ae633-12ea-4f82-8ea5-7d0bd192b21c/image.png)

→ 괄호로 잘 묶어서 쓰는게 좋음

*커서 바꾸는 법 → insert