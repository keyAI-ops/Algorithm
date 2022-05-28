# <투 포인터 알고리즘>
'''
1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스를 가리키도록 함.
2. 현재 부분 합이 M과 같다면 카운트함.
3. 현재 부분 합이 < M, end를 1 증가
4. 현재 부분 합이 >= M, start를 1 증가
5. 모든 경우 확인할 때까지 2~4 반복 
'''

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
