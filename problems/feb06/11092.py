T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num_lst = list(map(int, input().split()))

    max_num = num_lst[0]
    min_num = num_lst[0]
    max_result = 0
    min_result = 0
    for i in range(n):
        if num_lst[i] >= max_num:
            max_num = num_lst[i]
            max_result = i
        if num_lst[i] < min_num:
            min_num = num_lst[i]
            min_result = i

    print(f'#{test_case} {abs(max_result - min_result)}')