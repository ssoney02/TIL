T = int(input())

for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    # k: 한 번 충전으로 최대한 이동가능한 정류장 수
    # if k < stop_num[i+1]- stop_num[i]:  => 0
    stop_num = list(map(int, input().split()))

    bound_lst = []
    
    # 충전기가 최소 하나 이상 필요한 범주 정하기( 구간 기준)
    for j in range(1,n+1):
        if j % k == 0:
            bound_lst.append(j)
    print(bound_lst)
    
    for b in bound_lst:
        # if stop_num 
        if stop_num[]

    # for i in range(stop_num-1):
    #     if k < (stop_num[i+1] - stop_num[i]):
    #         result = 0
    #     else:
    #         # 최소 충전 횟수 
    #         # k의 배수 안에 최소 충전 가능 정류장 1곳 이상 (0이 아니면 됨)
    #         pass
    
    
        
        
        




    
