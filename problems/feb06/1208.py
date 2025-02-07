# 가로길이는 항상 100
T = 10

for test_case in range(1, T+1):
    n = int(input()) # 덤프 횟수
    box_lst = list(map(int, input().split()))
    def dump():
        min_box = min(box_lst)
        max_box = max(box_lst)
        max_idx = box_lst.index(max_box)
        min_idx = box_lst.index(min_box)
        box_lst[max_idx] -= 1
        box_lst[min_idx] += 1
        # print(f'{min_box}, {max_box}, {max_idx}, {min_idx}')
        # print(box_lst)
        new_max = max(box_lst)
        new_min = min(box_lst)
        return (new_max - new_min)
    
    for i in range(n):
        result = dump()
        if result <= 1:
            break
    print(f'#{test_case} {result}')

# 다른 풀이
N = int(input())
data = list(map(int, input().split()))
for _ in range(N):
    max_idx = 0
    min_idx = 0
    for i in range(100):
        if data[i] > data[max_idx]:
            max_idx = i
        if data[i] < data[min_idx]:
            min_idx = i
    data[max_idx] -= 1
    data[min_idx] += 1
min_idx
max_idx
for i in range(100):
        if data[i] > data[max_idx]:
            max_idx = i
        if data[i] < data[min_idx]:
            min_idx = i

