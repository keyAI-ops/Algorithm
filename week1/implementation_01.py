# <문제> 상하좌우

n = int(input('공간의 크기를 입력하세요 : '))

list_dir = input('방향을 입력하세요 : ').split()

x, y = 1, 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for i in list_dir:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
            
print(x, y)

