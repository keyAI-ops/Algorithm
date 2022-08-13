# <문제> 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input('N과 x를 입력하세요 : ').split())
array = list(map(int, input().split()))


def count_by_range(a, x):
    right_index = bisect_right(a, x)
    left_index = bisect_left(a, x)
    print(right_index - left_index)


count_by_range(array, x)
