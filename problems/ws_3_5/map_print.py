# map으로 최종 출력

def rental_book(lst):
    # print(f'age:{age}')
    number = lst['age'] // 10
    decrease_book(number)
    print(f'남은 책의 수 : {number_of_book}')
    print(f"{lst['name']}님이 {number}권의 책을 대여하였습니다.")
#     #딕셔너리의 'age'키의 값을 호출

# 함수 호출
# rental_book(**info)
# info 인자: {'name': , 'age': }

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book
    
list(map(rental_book, info)) # map함수 호출 됨