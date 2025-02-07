T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # cnt = 0
    arr = []
    result = []
    arr = [list(map(int, input().spllit())) for i in range(N)]

    # print(arr)
    max_val = -1
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni<N and 0<=nj<M:
                    cnt += arr[ni][nj]
                    # print(f'cnt={cnt}')
            max_val = max(max_val, cnt) # 굳이 리스트에 안넣어도됩!!!!!!!!!!!!!!!!!!!!!!!!!
    print(f'#{test_case} {max_val}')

