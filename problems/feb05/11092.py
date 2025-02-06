T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num_lst = map(int, input().split())

    max_num = num_lst[0]
    min_num = num_lst[0]
    for num in num_lst:
        if num >= max_num:
            max_num = num
        if num < min_num:
            min_num = num
    print(f'{test_case} {abs(max_num-min_num)}')