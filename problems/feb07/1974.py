T = int(input())

for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    new_puzzle = list(map(list, zip(*puzzle)))

    # print(puzzle)
    # print(new_puzzle)
    result = 1
    for i in range(9):
        for j in range(8):
            # 가로 줄 확인
            if puzzle[i][j] in puzzle[i][j+1:]:
                result = 0
                break
            # 세로 줄 확인
            if new_puzzle[i][j] in puzzle[i][j+1:]:
                result = 0
                break
    # 3x3 씩 확인.....
    d1 = [0, 3, 6]
    d2 = [0, 3, 6]
    # for m in [3, 6, 9]:
    #     for j in range(m):
    #         for k in [0, 3, 6]:
    #             for i in range(k, k+3):
    #                 print(puzzle[i][j])
    #                 if puzzle[i][j] in puzzle[i][j+1:]:
    #                     result = 0
    #                     break

    for m in range(2):
        for j in range(d1[m], d1[m+1]):
            for k in range(2):
                check = []
                for i in range(d1[k], d1[k+1]):
                    check.append(puzzle[i][j])
                    if puzzle[i][j] in check:
                        result = 0
                        break
    # for j in range(3):
    #     for i in range(d1[k+1], 6):
    #         if puzzle[i][j] in puzzle[i:][j+1:]:
    #             result = 0
    #             break
    # for j in range(3):
    #     for i in range(6, 9):
    #         pass
    # for j in range(3, 6):
    #     for i in range(0,3):
    #         pass
    print(f'#{tc} {result}')




