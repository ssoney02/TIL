# max 안쓴코드
T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    result = []
    for i in range(n):
        # boxes[n]이 되는 경우 고려! (제일 오른쪽 부분)
        if i == (n-1):
            cnt = 0
        else:
            right_num = boxes[i+1:]
            cnt = 0
            # print(f'r:{right_num}')
            for j in right_num:
                if boxes[i] > j:
                    cnt += 1 # boxes[i]보다 작은 것 개수 셈. cnt = 낙차
        result.append(cnt)
        answer = 0
        for r in result:
            if r > answer:
                answer = r
            
    # print(result)
    print(f'#{test_case} {answer}')

    '''
    max 사용 -> max(result)바로 출력
    '''