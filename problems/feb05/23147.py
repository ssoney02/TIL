T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    results = []
    if n == 1:
        num = 0
    for i in range(n):
        # i 보다 오른쪽의 인덱스 중, 자기보다 작은 수만큼 떨어짐짐
        right_boxes = list(boxes[i+1:])
        # print(f'rightbox:{right_boxes}')
        if i == (n-1):
            results.append(0)
        else:
            cnt = 0
            for j in len(right_boxes):
                if boxes[i] > right_boxes[j]:
                    cnt += 1
                results.append(cnt)
        
    num = max(results)
    # print(num)
    # print(results)
    
    
    print(f'#{test_case} {num}')
        