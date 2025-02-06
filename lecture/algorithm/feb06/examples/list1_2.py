DATA = [0,4,1,3,1,2,4,1]
N = len(DATA)
COUNTS = [0] * 5 # max(DATA) + 1 만큼 정수 분류를 해놓고 개수 셀 리스트를 만듦

for i in range(N):
    COUNTS[DATA[i]] += 1
print(COUNTS)

for i in range(1,5):
    COUNTS[i] += COUNTS[i-1]

print(COUNTS)



##################################################
TEMP = [0] * N # 새로 정렬할 리스트 만들어줌
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1 # DATA[i]까지의 개수 1개 감소
    TEMP[COUNTS[DATA[i]]] = DATA[i] # DATA[i]까지 차지한 칸 수 중 가장 오른쪽 칸에 DATA[i] 할당

##################################################

# 순열
for i1 in range(1, 4):
    for i2 in range(1,4):
        if i1 != i2: # 앞에서 사용된 적 없는 숫자를 곱할 것
            for i3 in range(1,4):
                if i1 != i3 and i2 != i3:
                    print(i1, i2, i3)

arr = [2,3,7]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2: # 앞에서 사용된 적 없는 숫자를 곱할 것
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])

##################################################
# baby-gin 그리디
num = int(input())

#끝에 두칸은 인덱스 벗어나는 오류 발생 가능 -> if로 따로 경우 처리 해주는 대신 애초에 칸수를 두칸 늘려서 만들어줌
c = [0] * 12 # c[10], c[11]은 항상 0 -> 예외처리를 위한 것이기 때문에..

for _ in range(6): # 단순 반복 6회
    c[num%10] += 1 # num%10 -> 1의 자리 알아내기
    num //= 10 # num의 1의 자리 제거 (끊어서 받지 않고 그냥 숫자 하나로 받아옴)
print(c) # 각 숫자의 개수를 담은 리스트 생성
#끝에 두칸은 인덱스 벗어나는 오류 발생 가능 -> if로 따로 경우 처리 해주는 대신 애초에 칸수를 두칸 늘려서 만들어줌줌

i = 0
tri = run = 0
while i < 10: # 카드 번호 9까지
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue # triplete이 같은 수로 두번 있는 경우, 다시 확인해야됨
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -=1
        run += 1
        continue
    i += 1

if run + tri == 2: 
    print('Baby Gin')
else:
    print('lose')

##################################################



