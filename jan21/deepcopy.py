list_A = ['abc', 'def']

#shallow copy
#방법1
list_B = list_A.copy()

#방법2
list_B = list_A[:]

print(list_A) #['abc', 'def']
print(list_B) #['ghi', 'def']

#deep copy
#변형 객체 새로운 공간에 값을 복사해서 가져옴

import copy

list_A = ['abc', ['def', 'ghi']]
list_B = copy.deepcopy(list_A)
list_B[1][0] = ['GHI']

print(list_A, list_B) #['abc, ['def','ghi']], ['abc', ['ghi'],'ghi']]

