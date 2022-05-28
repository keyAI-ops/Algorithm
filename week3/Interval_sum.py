# <구간 합 빠르게 계산하기>

'''
    접두사 합 : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓는다. 
    P[3]은 인덱스 0~3까지의 부분합을 말한다.
    그래서 특정 구간 합을 구하기 위해선 P[right] - P[left-1]을 구하면 된다.    
'''
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])
