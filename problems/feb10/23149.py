T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 일단 다 정렬해놓고..
    # 전체 리스트를 절반으로 나눠서
    # 절반은 오름차순
    # 절반은 내림차순
    # 인덱스 돌면서 하나씩 번갈아 새로운 리스트에 추가

    def selection_sort(a, n):
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, N):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return arr

    small_sort = selection_sort(arr, N)[:N//2]
    large_sort = selection_sort(arr, N)[N//2:]

    new_arr = []
    for i in range(N//2):
        new_arr.append(large_sort[-(i+1)])
        new_arr.append(small_sort[i])
    if arr[N//2] not in new_arr:
        new_arr.append(arr[N//2])
    str_arr = []
    for n in range(10):
        str_arr.append(str(new_arr[n]))
    result = ' '.join(str_arr)

    print(f'#{tc} {result}')