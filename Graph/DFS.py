# 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          # 현재 정점 s를 출력함
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                DFS(vtx, adj, v, visited)


# 깊이 우선 탐색 테스트 프로그램
vtx =  ['A', 'B','C','D','E','F','G','H']
edge = [ [  0,  1,  1,  0,  0,  0,  0,  0],
         [  1,  0,  0,  1,  0,  0,  0,  0],
         [  1,  0,  0,  1,  1,  0,  0,  0],
         [  0,  1,  1,  0,  0,  1,  0,  0],
         [  0,  0,  1,  0,  0,  0,  1,  1],
         [  0,  0,  0,  1,  0,  0,  0,  0],
         [  0,  0,  0,  0,  1,  0,  0,  1],
         [  0,  0,  0,  0,  1,  0,  1,  0] ]

print('DFS(출발:A) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()



# 코드: 딕셔너리(리스트 기반) 깊이 우선 탐색(DFS, 재귀)
def DFS2(graph, v, visited):
    if v not in visited:             # v가 아직 방문되지 않았다면
        visited.add(v)               # v 방문 표시
        print(v, end=' ')            # v 출력
        for u in graph[v]:           # v의 모든 인접 정점 u에 대해
            if u not in visited:     # 방문하지 않은 정점이면
                DFS2(graph, u, visited)  # 재귀 호출 (순환)

# 그래프를 딕셔너리(리스트)로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'F'],
    'E': ['C', 'G', 'H'],
    'F': ['D'],
    'G': ['E', 'H'],
    'H': ['E', 'G']
}

visited = set()                       # 방문한 정점 기록용 집합
print("DFS2(출발:A): ", end='')
DFS2(graph, 'A', visited)
print()