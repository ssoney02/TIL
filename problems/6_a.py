my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for k in my_set:
    if k in my_dict.keys():
        print(my_dict.get(k))
    else:
        print(None)

var = (1,2,3,'A')

my_dict[var] = '변수로도 키 설정 가능'

print(my_dict)

# 출력할 때마다 결과가 바뀜.. 딕셔너리는 순서가 없으므로!!!!! 가져올때마다 마음대로 가져옴!