# <문제> 모험가 길드

n = int(input('인원수를 입력하세요 : '))

data = list(map(int, input('공포도를 입력하세요 : ').split()))
data.sort()

count = 0
result = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
        
print(result)