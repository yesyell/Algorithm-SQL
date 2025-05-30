from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, list(input().strip()))) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([(0, 0, 1)])
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

while queue:
    x, y, d = queue.popleft()
    
    if x == n-1 and y == m-1:
        print(d)
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, d+1))