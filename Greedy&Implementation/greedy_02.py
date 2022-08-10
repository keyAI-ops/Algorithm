# <문제> 곱하기 혹은 더하기

def solution(num_str):   
    result = num_str[0]
    
    for i in range(1, len(num_str)):
        num = int(num_str[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result