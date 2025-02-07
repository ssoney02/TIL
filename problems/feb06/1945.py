T = int(input())

for test_case in range(1, T+1):
    num = int(input())

    n_list = [2, 3, 5, 7, 11]
    result = []
    for n in n_list[::-1]:
        i = 0
        while num % n == 0:
            num //= n
            i += 1
        result.append(str(i))
    rev_result = result[::-1]
    print(rev_result)
    final = ' '.join(rev_result) # ' ' 에 join해도 맨 앞에 공백이 남진 않음... 왜지????
    # print(final)
    print(f'#{test_case} {final}' )
    # print(rev_result)
