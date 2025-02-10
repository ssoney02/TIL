import sys
sys.stdin = open("1210input.txt", "r")

T = 10
for tc in range(1, T+1):
    test_case = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    check_arr = [[0] * 100 for _ in range(100)]

    end_point = ladder[-1].index(2)
    initial_i = 99
    initial_j = end_point
    print(end_point)
    # 윗쪽확인을 가장 마지막에 시킴
    di = [0, 0, -1]
    dj = [1, -1, 0]

    def check_ladder(i, j):
        # 왔던 지점 좌표 따로 저장
        old_i = i
        old_j = j
        for k in range(3):
            check_i = i + di[k]
            check_j = j + dj[k]
            if 0 <= check_i < 100 and 0 <= check_j < 100:
                if check_i != old_i and check_j != old_j:
                    # 범위 벗어나는거 체크해야됨!!!!!!!!!!!!!!!!!!!!!!
                    # 왔던 곳으로 다시 가면 무한루프 걸림(예외처리)
                    if ladder[check_i][check_j] == 1:
                        # 새로운 좌표 중 값이 1인 곳으로 이동해야함
                        # i,j 값 갱신
                        i += di[k]
                        j += dj[k]
                        result = [i, j]
                        # print(result)
                        return result
                        break
    a = check_ladder(initial_i, initial_j)
    print(a)
    new_i = check_ladder(initial_i, initial_j)[0]
    new_j = check_ladder(initial_i, initial_j)[1]
    while True:
        check_ladder(new_i, new_j)
        new_i = check_ladder(new_i, new_j)
        new_j = check_ladder(new_i, new_j)
        if new_i < 0:
            break

    print(f'{tc} {j}')



