### 파이썬 실행 방법

1. shell로 한 번에 한 명령어 씩 입력해서 실행
    
    python -i
    
2. 확장자가 .py인 파일에 작성된 파이썬 프로그램 실행

### 표현식: 코드 조각

### 값: 표현식이 평가된 결과

ex.

표현식: 3 + 5

값: 8

⇒ 표현식이 평가되어 값이 반환(return)됨

### 평가 : 표현식을 실행하여 값을 얻는 과정

→ 표현식을 순차적으로 평가하여 프로그램의 동작을 결정

### 문장: 실행 가능한 동작을 기술하는 코드

(조건문, 반복문, 함수 정의 등)

- 문장은 보통 여러 개의 표현식을 포함

### 타입: 변수나 값이 가질 수 있는 데이터의 종류

→ 어떤 종류의 데이터 인지, 어떻게 해석되고 처리되어야 하는지를 정의

→ 2 가지 요소로 이루어짐 : 1. 값(피연산자) 2. 값에 적용할 수 있는 연산(연산자)

### 데이터 타입

1. Numeric Type
    
    : int, float, complex(복소수)
    
2. Sequence Types : 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
    
    : list, tuple, range +) str..
    
    - **sequence types의 특징**
        1. 순서: 값들이 순서대로 저장(정렬x)
        2. 인덱싱: 각 값에 고유한 인덱스를 가지고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음
        3. 슬라이싱: 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
        4. 길이: len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
        5. 반복: 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
3. Text sequence type
    
    : str
    
    → 문자들의 순서가 있는(시퀀스 특징) + 변경 불가능한 시퀀스 자료형
    
    - 문자열 표현
        - 단일 문자나 여러 문자의 조합으로 이루어짐
        - **작은 따옴표(’)** 또는 큰따옴표(”)로 감싸서 표현 → 뭘써도 상관없으나, 섞어쓰지 xxx
        
4. non-sequence types
    
    : set, dict
    
5. 기타
    
    boolean, none, functions
    

→ 타입의 중요성 :데이터 타입에 맞는 연산을 수행할 수 있기 때문, 값들을 구분하고 어떻게 다뤄야 하는 지를 알 수 있음.

### 산술 연산자

//: 정수 나눗셈(몫)

%: 나머지

**: 지수 (거듭제곱)

### 연산자 우선순위

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/99413d6e-ee7f-441a-b945-dc87834e4882/image.png)

- 주의!
    
    ```python
    -2 ** 4
    >> -16
    ```
    
- 괄호를 써서 수행하는게 실수 방지 가능

### 변수: 값을 저장하기 위한 이름

⇒ 값을 참조하기 위한 이름

### 변수 할당: 표현식을 통해 변수에 값을 저장

```python
degrees = 36.5
#<할당문> 변수 degrees에 값 36.5를 할당했다.
```

### 할당문

1. 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소) 생성
2. 값의 메모리 주소를 ‘=’ 왼쪽에 있는 변수에 저장 (실제로는 값이 아니라 메모리 주소를 할당하는 것)
- 존재하지 않는 변수라면 → 새 변수 생성
- 기존에 존재했던 변수라면 → 기존 변수 재사용해서 변수에 들어있는 메모리 주소 변경

- 메모리 주소: 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재(컴퓨터가 알아서 처리함)

### 객체(object): 타입을 갖는 메모리 주소 내 값

→ “값이 들어있는 상자”

**변수** → 그 변수가 참조하는 객체의 메모리 주소를 가짐

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/3d4f4cd7-9f4e-4455-bbd1-4a1633723baa/image.png)

---

주의!)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/5ac461c9-7b29-4bd0-8e3b-82644b990218/image.png)

double에 값이 할당 된 이후에 number에 값이 재할당됨

double의 값은 여전히 20

---

### Data Types: 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성

### int:  정수 자료형

### float: 실수 자료형

→ 실수에 대한 근삿값

### 진수 표현

→ 접두어를 붙여서 표현함

- 2진수(binary) : 0b
- 8진수(octal) : 0o
- 16진수(hexadecimal): 0x

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/caedfba4-5655-40ce-89aa-7b23b1880bfb/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/0672b352-695f-48a2-80a4-cf797fe6e8c3/image.png)

### 부동소수점 에러(floating point rounding error)

: 컴퓨터가 실수를 표현하는 방식으로 인해 발생하는 작은 오차

→ 실수를 2진수로 변환하는 과정에서 발생하는 근사치 표현으로 인해 발생

⇒ sol) **decimal 모듈** 사용.. 등

### Escape sequence

:역슬래시 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합

\n: 줄 바꿈

\t: tab

\\: 백슬래시

\’: 작은 따옴표

\”: 큰 따옴표

### String interpolation: 문자열 내에 변수나 표현식을 삽입하는 방법(보간법)

### ⇒🌟f-string: 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하는 문법

→ 문자열에 파이썬 표현식의 값을 삽입할 수 있음

```python
print(f'Debugging {bugs} {counts} {area}')
```

### slicing 팁

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/792a184b-da6a-443e-9083-d8df079e3018/9aa5d803-237c-40e8-b6b5-be89782189af/image.png)

→ 사이를 중심으로 컷팅한다고 생각하면 덜헷갈림

**인터프리터** : 사용자의 명령어를 운영체제가 이해하는 언어로 바꿈