# <문제> 왕실의 나이트

def solution(location):
    row = list(range(1,9))
    column = ['a','b','c','d','e','f','g','h']
    
    








'''
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
column = ['1', '2', '3', '4', '5', '6', '7', '8']

count = 0

loc = list(input('위치를 입력하시오 : '))

moves = [[2, 1],
         [2, -1],
         [-2, 1],
         [-2, -1],
         [-1, 2],
         [1, 2],
         [-1, -2],
         [1, -2]]

loc_row = row.index(loc[0])
loc_column = column.index(loc[1])

loc = [loc_row, loc_column]

for move in moves:
    current_loc = [loc[0] + move[0], loc[1] + move[1]]
    if current_loc[0] < 0 or current_loc[0] > 7 or current_loc[1] < 0 or current_loc[1] > 7:
        continue
    else:
        count += 1

print(count)
'''