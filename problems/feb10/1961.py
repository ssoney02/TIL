T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def rotate_arr(a):
        r_arr = list(map(list, zip(*a[::-1])))
        return r_arr

    rotate90 = rotate_arr(arr)
    # print(rotate90)
    rotate180 = rotate_arr(rotate90)
    # print(rotate180)
    rotate270 = rotate_arr(rotate180)

    final_arr = [[''] * 3 for _ in range(N)]
    # print(final_arr)
    for i in range(N):
        for j in range(N):
            final_arr[i][0] += str(rotate90[i][j])
            final_arr[i][1] += str(rotate180[i][j])
            final_arr[i][2] += str(rotate270[i][j])
    result = ''
    # print(f'#{tc} {final_arr}')
    for i in range(N):
        result += '\n'
        for j in range(3):
            result += (final_arr[i][j] + ' ')

    print(f'#{tc} {result}')
