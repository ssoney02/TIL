T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # 버스 노선 개수
    a, b = map(int, input().split())
    p = int(input())
    c = []
    for j in range(p):
        c[j] = int(input())

    stop_lst = [0] * 5000
    

