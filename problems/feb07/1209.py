import sys
sys.stdin = open("1209_input.txt", "r")

T = 10
for test_case in range(1, T+1):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_lst = []
    col_sum = crs_sum1 = crs_sum2 = 0
    for i in range(100):
        row_sum = 0
        crs_sum1 += arr[i][i]
        crs_sum2 += arr[i][99-i]

        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        sum_lst.append(row_sum)

        sum_lst.append(col_sum)
        col_sum = 0

    sum_lst.append(crs_sum1)
    sum_lst.append(crs_sum2)
    # 각 합 별로 초기화 되어야 하는 지점이 다름........
    print(f'#{tc} {max(sum_lst)}')
