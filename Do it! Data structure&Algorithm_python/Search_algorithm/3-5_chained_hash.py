from __future__ import annotations
from typing import Any, Type
import hashlib

 
class Node: # 해시 구성 노드
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key   = key    
        self.value = value  
        self.next  = next   # 뒤쪽 노드를 참조

class ChainedHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity             # 해시 테이블 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        ''' sha256 : 256비트로 구성, 64자리 문자열 반환 / 블록체인의 블록을 암호화하는데 사용
            encode() : 바이트 문자열 생성
            hexdigest() : sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냄
        '''
        
    def search(self, key: Any) -> Any:
        # 키가 key인 원소를 검색하여 값을 반환
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 노드를 노드

        while p is not None:
            if p.key == key:
                 return p.value  # 검색 성공
            p = p.next           # 뒤쪽 노드를 주목

        return None              # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 원소를 삽입
        hash = self.hash_value(key)  # 삽입하는 키의 해시값
        p = self.table[hash]         # 주목하는 노드

        while p is not None:
            if p.key == key:
                return False         # 삽입 실패
            p = p.next               # 뒤쪽 노드에 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp      # 노드를 삽입
        return True                  # 삽입 성공

    def remove(self, key: Any) -> bool:
        # 키가 key인 원소를 삭제
        hash = self.hash_value(key)  # 삭제할 키의 해시값
        p = self.table[hash]         # 주목하고 있는 노드
        pp = None                   

        while p is not None:
            if p.key == key:  # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공
            pp = p
            p = p.next       # 뒤쪽 노드에 주목
        return False         # 삭제 실패(key가 존재하지 않음)

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')  # 해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()