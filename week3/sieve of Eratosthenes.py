# <에라토스테네스의 체 알고리즘>

import math

n = 1000

array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2  # 2배수부터 시작해서 배수가 n보다 작을때까지 반복
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
