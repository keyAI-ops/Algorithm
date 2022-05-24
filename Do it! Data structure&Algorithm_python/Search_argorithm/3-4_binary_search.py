# 선형검색
from typing import Any, Sequence

def bin_search(a:Sequence, key:Any) -> int:
    pl = 0
    pr = len(a)-1
    
    while True:
        pc = (pl+pr)//2
        
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc+1
        else:
            a[pc] > key
            pr = pc-1
        if pl > pr:
            break
        return -1