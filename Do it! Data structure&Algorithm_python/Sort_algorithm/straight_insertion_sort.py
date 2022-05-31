from typing import MutableSequence

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
            