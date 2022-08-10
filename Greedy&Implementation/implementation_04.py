# <문제> 문자열 재정렬

def solution(pro_str):
    alphabet_str = ""
    num_sum = 0
    
    for i in pro_str:
        if ord(i) >= 65 and ord(i) <= 90:
            alphabet_str += i
        else:
            num_sum += int(i)
    alphabet_str = "".join(sorted(alphabet_str))
    num_sum  = str(num_sum)
    result = alphabet_str + num_sum
    print(result)
    return result
solution("K1KA5CB7")
        
'''
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))
print(''.join(result))
'''