# for문 안에서 pop

# <짝수만 뽑아내기>

## 1안. 홀수만 원래 리스트에서 pop 시키고 원래 리스트 반환

## 2안. 짝수만 pop해서 새로운 리스트에 추가해서 반환
.extend(_iterable_) 을 사용해서 요소 하나하나 추가하고 싶으면  
그냥 .extend([_요소_]) 로 넣어주면 됨  

```python
new_list.extend([n_list.pop(i)])
```

## 1안. idx 사용해서 for문 돌리기
### 1. deep copy 사용
원래 리스트 : n_list  
복사한 리스트: dummy_lst  

순회는 원래 리스트에서 하고, pop은 복사한 리스트에서 진행.  
복사한 리스트를 반환하면
for문에서 순회할 인덱스가 영향 받지 x

```python
immport copy

def even_elements(n_list):
    dummy_lst = copy.deepcopy(n_list)
    for i in range(len(n_list)):
        if n_list[i] % 2 != 0:
            dummy_lst.pop(dummy_lst.index(n_list[i]))

```

### 2. 역순 순회!!
인덱스를 뒤에서 부터 제거하면 <br>
전체 인덱스 순서에는 영향이 x

```python
def even_elements(n_list):
    new_list = []
    for i in range(len(n_list)-1, -1, -1):
        if n_list[i] % 2 == 0:
            new_list.extend([n_list.pop(i)])
    else:
        pass

    new_list.reverse() # 리스트 다시 뒤집기
    return new_list
```
## 2안. 요소 자체로 for문 돌리기
### .index() 사용해서 요소의 인덱스 번호 자체를 가져옴 -
-> 값이 변화해도 그때그때 인덱스 번호를 찾아오므로 영향x

```python
def even_elements(n_list):
    new_list = []
    for num in n_list:
        if  num % 2 != 0:
            n_list.pop(n_list.index(num))
        
        else:
            pass
    new_list.extend(n_list)
    return new_list
```