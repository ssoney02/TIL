# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1|set2

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print('최소 2개의 셋이 필요합니다.')
    else:
        s2 = set()
        # print(sets)
        for s in sets:
            # print(s)
            s2 = s2.union(s) #리턴 해줘야됨!! 연산이니까..! 셋을 수정하는게 아님..
        return s2


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
