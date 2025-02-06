# 다른 시도... fail
T = int(input())

for test_case in range(1, T + 1):
     num = int(input())

# for i in range(len(num_list)):
#      if num_list[i] == num_list[i+1]

     c = [0] * 12

     for _ in range(6):
          c[num%10] += 1
          num //= 10
          print(c) # 각 숫자의 개수를 담은 리스트 생성

     i = 0
     tri = run = 0
     while i < 10:
          if c[i] >= 3:
               c[i] -= 3
               tri += 1
               continue
          if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
               c[i] -= 1
               c[i+1] -=1
               c[i+2] -=1
               run += 1
               continue
          i += 1

     if run + tri == 2:
          print(f'#{test_case} true')
     else:
          print(f'#{test_case} false')



