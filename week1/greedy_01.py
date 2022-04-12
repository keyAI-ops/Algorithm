# <문제> 1이 될 때까지

n = int(input('N을 입력하세요 : '))
k = int(input('K을 입력하세요 : '))

count = 0

while True:
    target = (n//k) * k
    count += (n-target)
    n = target
    
    if n < k:
        break
    count += 1
    n //= k
    
count += (n-1)
print(count)