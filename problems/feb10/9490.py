T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    b_list = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_cnt = 0

    for i in range(N):
        for j in range(M):
            cnt = b_list[i][j]
            for m in range(1, b_list[i][j]+1):
                for k in range(4):
                    new_i = i + di[k] * m
                    new_j = j + dj[k] * m
                    if 0 <= new_i < N and 0 <= new_j < M:
                        cnt += b_list[new_i][new_j]  # 여기까지만 적으면 인덱스 벗어났을 때 계속 탐색함
                    else:
                        break  # index 벗어났을 때 시간 훨씬 단축 가능

            max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')

