# <문제> 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input('N과 x를 입력하세요 : ').split())
array = list(map(int, input().split()))

answer = bisect_right(array, x) - bisect_left(array, x)

if answer > 0:
    print(answer)
else:
    print(-1)
