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

# print(f'many user: {many_user}')

info = list(map(lambda lst: {'name' : lst['name'], 'age': lst['age']}, many_user))
print(info)

'''
info = dict(map(lambda lst: {'name' : lst['name'], 'age': lst['age']}, many_user))
{{'name': '김시습', 'age': 20}, {'name': '허균', 'age': 16}, {'name': '남영로', 'age': 52}, {'name': '임제', 'age': 36}, {'name': '박지원', 'age': 60}}
dict는 key-value 형태여야되는데, 리스트 형태로 넣을 수가 없음!!!
map 자체로 넘겨서 map object에서 꺼내든가,, 해야지 될 듯 map object에서 요소를 하나씩 꺼내는 방법이 있나?
print(f'info:{info}')
'''
#many_user에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당



#info 인자: {name, age}
#info 인자에 사용될 딕셔너리: many_user, map 을 사용해 새로운 딕셔너리 생성 -> map 함수는 lambda로 구현




def rental_book(lst):
    number = lst['age'] // 10
    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f"{lst['name']}님이 {number}권의 책을 대여하였습니다.")


def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book
    
list(map(rental_book, info)) # map함수 호출 됨
