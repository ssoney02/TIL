arr = [[0]*4 for _ in range(3)]
print(arr)

#########################################
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j])