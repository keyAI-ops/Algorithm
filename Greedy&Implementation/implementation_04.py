# <문제> 문자열 재정렬

str_num = list(input('문자열을 입력하세요 : '))

str_num.sort()

result = 0
result2 = []

for i in str_num:
    if ord(i) < 65:
        result += int(i)
    else:
        result2.append(i)

result2 = ''.join(result2)
result3 = result2+str(result)

print(result3)
