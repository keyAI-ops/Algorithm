# <문제> 떡볶이 떡 만들기

n, m = map(int, input('떡의 개수와 떡의 길이를 입력하세요 : ').split())
dduk_list = list(map(int, input('떡의 개별 높이를 입력하세요 : ').split()))
dduk_list.sort()

mid = int((dduk_list[0]+dduk_list[-1])/2)

while True:
    list_a = []
    for i in dduk_list:
        if i > mid:
           list_a.append(i-mid)
           
    if sum(list_a) > m:
        mid += 1
    elif sum(list_a) < m:
        mid -= 1
    else:
        break

print(mid)