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

for tc in range(1, 11):
    N = int(input())
    n_high = list(map(int, input().split()))
    # 뷰가 좋은 집
    view = 0

    for i in range(2, N-2):
        # 기준이 될 건물, 좌우로 2개씩 가져와서 새 리스트 담기
        point = n_high[i]
        p_list = []
        # 좌 우로 2개씩 기준
        for j in range(i-2, i+3):
            # if n_high[j] != point:
            p_list.append(n_high[j])

        # print(p_list, point)

        # p_list 에서 가장 높은 건물이 기준 건물이 맞는지 확인.
        p_high = p_list[0]
        for p in p_list:
            if p > p_high:
                p_high = p

        # print(p_high, point)

        # 최고 높은 건물이 아니면 ? 스킵해
        

        # 맞으면 최고 높이 건물과의 최소차이 를 찾아
        if point == p_high:
            # 해당 건물 리스트만 잘 넘어오는거 확인
            # 두 번째 높은 애 찾기
            new_list = []
            print(f'p:{p_list}')
            for k in p_list:

                if k != point:
                    new_list.append(k)
            print(new_list)
            new_high = new_list[0]
            for new in new_list:
                if new > new_high:
                    new_high = new

            # 젤 높은애랑 두번째 높은애랑 차이 = 뷰가 좋은 가구수
            view_cnt = point - new_high
            view += view_cnt
        print(f'p:{p_list}')
    print(f"#{tc} {view}")