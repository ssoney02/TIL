T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for l in range(M):
                    new_i = i + k
                    new_j = j + l
                    cnt += arr[new_i][new_j]
            max_val = max(max_val, cnt)

    print(f'#{test_case} {max_val}')