'''
단순 정렬 : 가장 작은 원소를 골라 맨 앞에 위치 - 그 다음으로  작은 원소를 골라 정렬되지 않은 위치 중 맨 앞에 위치 - 반복
'''

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[j]