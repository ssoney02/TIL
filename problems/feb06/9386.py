T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    num = list(map(int, input()))
    cnt = 1
    new_idx = []
    cnt_lst = []
    if 1 not in num:
        print(f'#{test_case} {0}')
        continue
    else:

        for i in range(n-1):
            if num[i] == 1 and num[i+1] == 1:
                new_idx.append(i)
                new_idx.append(i+1)

        sorted_idx = list(set(new_idx))

        # 1이 있긴 한데 연속되지 않은 경우.. 예외처리
        if len(sorted_idx) == 0:
            cnt_lst.append(1)
        else:
            for j in range(len(sorted_idx)-1):
                if (sorted_idx[j+1] - sorted_idx[j]) == 1:
                    cnt += 1
                else:
                    cnt = 1
                cnt_lst.append(cnt)
    print(f'#{test_case} {max(cnt_lst)}')
