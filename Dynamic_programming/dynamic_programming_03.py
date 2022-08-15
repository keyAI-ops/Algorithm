# <문제> 효율적인 화폐 구성

def money(list_money, n, m):
    d = [10001]*(m+1)
    d[0] = 0
    
    for i in range(n):
        for j in range(list_money[i], m+1):
            if d[j-list_money[i]] != 10001:
                d[j] = min(d[j], d[j-list_money[i]]+1)

    if d[m] == 10001:
        return(-1)
    else:
        return(d[m])
