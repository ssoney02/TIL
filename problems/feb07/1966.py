T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    for i in range(N-1,0,-1):
        for j in range(i):
            if num_lst[j] > num_lst[j+1]:
                num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]
        # print(num_lst)
    new_lst = []
    for n in num_lst:
        new_lst.append(str(n))
    result = ' '.join(new_lst)
    print(f'#{test_case} {result}')