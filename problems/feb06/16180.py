T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num = int(input())

    cnt_lst = [0] * 10

    for _ in range(n):
        cnt_lst[num%10] += 1
        num //= 10

    max_cnt = cnt_lst[0]
    max_i = 0
    for i in range(10):
        if cnt_lst[i] >= max_cnt:
            max_cnt = cnt_lst[i]
            max_i = i
    
    print(f'#{test_case} {max_i} {max_cnt}')
    

