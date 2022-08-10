# <문제> 문자열 재정렬

from unittest import result


def solution(pro_str):
    alphabet_str = ""
    num_str = ""
    
    for i in pro_str:
        if ord(i) >= 65 and ord(i) <= 90:
            alphabet_str += i
        else:
            num_str += i
    alphabet_str = "".join(sorted(alphabet_str))
    num_str  = "".join(sorted(num_str))
    result = alphabet_str + num_str
    print(result)

solution("K1KA5CB7")
        
'''
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
'''