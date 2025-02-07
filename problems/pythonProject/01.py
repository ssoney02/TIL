import sys

sys.stdin = open('input.txt')


# 33
# => 홀수면 1, 짝수면 0
N = int(input())
result = 1 if N % 2 else 0
print(f'{result}')