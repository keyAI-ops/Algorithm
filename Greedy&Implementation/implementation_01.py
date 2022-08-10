# <문제> 상하좌우

def solution(n, list_dir):
    x, y = 1,1
    dx = [0,0,-1,1]    
    dy = [-1,1,0,0]
    move = ['L','R','U','D']
    
    for i in list_dir:
        x += dx[move.index(i)]
        y += dy[move.index(i)]
        if x < 1 or y < 1 or x > n or y > n:
            x -= dx[move.index(i)]
            y -= dy[move.index(i)]
    return x, y

solution(5,['R','R','R','U','D','D'])

'''
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
''' 

