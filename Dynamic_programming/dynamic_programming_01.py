n = int(input('식량창고의 개수를 입력하시오 : '))
k = list(map(int, input('식량의 개수를 입력하시오 : ').split()))

d = [0]*100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])