T = 10

for test_case in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2,n-2):
        height = []
        max_height = buildings[i]
        for j in [-2, -1, 1, 2]:
            height.append(buildings[i+j])
            if max_height < buildings[i+j]:
                max_height = buildings[i+j]
        second_height = 0
        # max 미사용
        for h in height:
            if h > second_height:
                second_height = h
        # max 사용
        # if max_height == buildings[i]:
        #     cnt += (max_height - max(height))
        if max_height == buildings[i]:
            cnt += (max_height - second_height)
            

        
    print(f'#{test_case} {cnt}')