# 다른 시도... fail
T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input()))
    sorted_list = sorted(num_list)

    num_1 = sorted_list[:3]
    num_2 = sorted_list[3:]
    
    # print(num_1)
    # print(type(num_1))
    for i in range(2):
        if ((num_1[i] + 1) == num_1[i+1] and (num_2[i] +1) == num_2[i+1]) or ((num_1[i] + 1) == num_1[i+1] and len(set(num_2))== 1) or (len(set(num_1))== 1 and (num_2[i] +1) == num_2[i+1]) or (len(set(num_1)) == 1 and len(set(num_2)) == 1):
             result = 'true'
        
        else:
             result = 'false'

    # if len(set(num_1)) == 1 and len(set(num_2)) == 1:
    #         result = 'true'
        

    print(f'#{test_case} {result}')