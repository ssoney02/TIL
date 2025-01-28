
def create_user(data_lst):
    user_list = []
    cnt = 0
    # 하나의 리스트를 인자로 받음
    # dummy_data 리스트를 순회해서 is_validation 함수 호출 -> 올바른 데이턴지 확인
    for data in data_lst:
        # -> 리턴 된 값이 False 면 데이터 자체를 None으로 대치 , 
        #   print(f'잘못된 데이터로 구성된 유저의 수는 {}개 입니다.')
        #   -> 잘못된거 개수는 False or 'blocked'반환될때마다 += 1
        #   -> blocked가 반환되면 해당 유저 정보는 user_list에 추가x (continue)
        #  ??False여도 user_list에 추가안하고 cnt+=1, blocked 여도 마찬가지... 맞나????
        # -> True면
        #    user_list.append()
        if is_validation(data) == True:
            user_list.append(data)
        elif is_validation(data) == 'blocked':
            cnt += 1

        else:
            # print(is_validation(data))
            for i in range(len(is_validation(data)[1])):
                #is_validation(data)[1] -> ['name', 'company']
                # data[is_validation(data)[1][i]] = None
                # print([is_validation(data)[1][i]])
                user_list.append(data)

                # 유저 리스트에 일단 해당 정보(딕셔너리)를 추가하고, 딕셔너리의['key'] = None
                # 유저리스트에 마지막으로(방금) 추가한 것의 뽑아낸 key들의 value를 none으로 치환하고 싶음
                user_list[-1][str(is_validation(data)[1][i])] = None
            cnt += 1
    
    print(f'잘못된 데이터로 구성된 유저의 수는 {cnt} 입니다.')
    print(user_list)




def is_validation(data):
    # create_user 함수에서 순회하며 넘긴 리스트 인자를 확인
    # False 반환 조건
    # 1. 리스트['blood_group'] not in blood_types 인지
    # 2. 리스트['company'] in black_list 인지
    # 3. '@' not in 리스트['mail']  인지
    # 4. len(리스트['name']) > 30 or <2 인지
    # 5. len(리스트['website']) < 1 인지
    # => False 반환 & return [keys] 단, 2번 위반의 경우, return 'blocked'&break
    err_data = []
    # (data['compnay'] in black_list) or
    
    # for key in data.keys():
        # 딕셔너리 하나를 순회하는 것
    if data['company'] in black_list:
        return 'blocked'
            # break

            
    else:
        if ( data['blood_group'] not in blood_types):
            err_data.append('blood_group')
        if ('@' not in data['mail']):
            err_data.append('mail')
        if ( len(data['name']) > 30 or len(data['name']) < 2):
            err_data.append('name')
        if ( len(data['website']) < 1 ):
            err_data.append('website')
        
    
        if len(err_data) == 0:
            return True
        elif len(err_data) > 0:
            return (False, err_data)
    
    

    
create_user(user_data)