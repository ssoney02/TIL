T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for i in range(N)]
    c_sum = 0
    cnt = 0
    arr = [[0] * 10 for i in range(10)]
    print(arr)
    for _ in range(N):
        start_point = info[_][:2]
        end_point = info[_][2:4]
        color = info[_][-1]
    # print(start_point)
    for i in range(2):
        for j in range(2):
            print(start_point[i][j])
            arr[start_point[i][j]] += 1

    print(arr)

        # print(start_point)
    if c_sum == 3:
        cnt += 1
        pass