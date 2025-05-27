def solution(n, computers):
    visited = [0] * n # 각 컴퓨터의 방문 여부를 저장
    def dfs(node):
        visited[node] = 1  # 방문 처리
        for i in range(n):
            if computers[node][i]==1 and not visited[i]:
                dfs(i)
    answer = 0
    for i in range(n):
        if not visited[i]: # 아직 방문하지 않은 컴퓨터를 시작점으로 DFS
            dfs(i)
            answer += 1 # DFS가 끝날 때마다 하나의 네트워크 발견
    return answer