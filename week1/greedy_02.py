# <문제> 곱하기 혹은 더하기

data = input('숫자를 입력하세요 : ')

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)        


'''
num_arr = list(input('숫자를 입력하세요'))
ans = []

for i in num_arr:
    if i == '0' or i == '1':
        i = i+'+'
        ans.append(i)
    elif i >= '2':
        i = i+'*'
        ans.append(i)
            
ans = ''.join(ans)
print(ans)
'''