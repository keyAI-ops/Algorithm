# <문제> 개미 전사

def dynamic_ant(n, k):
    d = [0]*100

    d[0] = k[0]
    d[1] = max(k[0], k[1])

    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + k[i])   
        
    return d
