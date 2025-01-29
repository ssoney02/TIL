number_of_people = 0

number_of_book = 100

def increase_user():
    pass



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    user_info = {
        'name': name,
        'age' : age,
        'address' : address
    } 
    
    print(f'{name}님 환영합니다!')
    return user_info

many_user = list(map(create_user, name, age, address))



#many_user에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당
#info 인자: {name, age}
#info 인자에 사용될 딕셔너리: many_user, map 을 사용해 새로운 딕셔너리 생성 -> map 함수는 lambda로 구현


'''
def info_func(name, age):
    #many_user 딕셔너리 안에 있는 값만 가져오면됨, 순회는 map이 할 것것
    # many_user는 리스트임 -> 리스트 순회는 map이 하고, 각 딕셔너리의 key를 어케 뽑아오지?
    dict = {
        'name' : many_user['name'],
        'age' : many_user['age']
        }
'''


def rental_book(name, age):
    # print(f'age:{age}')
    number = age // 10
    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')
#     #딕셔너리의 'age'키의 값을 호출

# 함수 호출
# rental_book(**info)
# info 인자: {'name': , 'age': }

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book
    

# info인자에 사용될 딕셔너리
def info_making_func(lst):
    info = {
        'name': lst['name'],
        'age': lst['age']
        }
    return info

for lst in many_user:
    result = info_making_func(lst)
    # print(result)
    rental_book(**result)
    # print(lst)