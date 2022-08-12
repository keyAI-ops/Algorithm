# 두 배열의 원소 교쳬

n, k = map(int, input('N, K를 입력하세요 : ').split())

while True:
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    if len(list_a) != n or len(list_b) != n:
        print('원소 개수가 맞지 않습니다! 다시 입력하세요!')
        continue
    else:
        break

list_a.sort()
list_b.sort(reverse=True)


for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        continue