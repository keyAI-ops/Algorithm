# <문제> 모험가 길드

def solution(n, data):
    data.sort()
    people_count = 0
    group_count = 0

    for i in data:
        people_count += 1
        if people_count >= i:
            group_count += 1
            people_count = 0
    return group_count

''' 문제해결
    - 공포도가 가장 낮은 순으로 정렬하여 하나씩 빼오면서 확인
    - 인원수가 공포도보다 크거나 같다면 그룹 하나 결성
'''