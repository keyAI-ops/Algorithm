from typing import MutableSequence
import bisect

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
        
# 개선된 이진 삽입 정렬
def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스
        
        while True:
            pc = (pl+pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl <= pr else pr + 1
        
        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key
    
    
# 다음과 같이 모듈을 사용해 간단히 이진 삽입 정렬을 구현
def binary_insertion_sort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)
        # bisect.insort(a, x, lo, hi)를 호출하면 a가 이미 정렬된 상태를 유지하면서 a[lo]~a[hi] 사이에 x를 삽입