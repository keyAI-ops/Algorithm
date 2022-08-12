# DFS 소스코드 예제

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [], # 노드가 1번부터 시작하는 경우가 많기 때문에 인덱스 0은 비워둔다.
    [2, 3, 8],   
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

dfs(graph, 1, visited)