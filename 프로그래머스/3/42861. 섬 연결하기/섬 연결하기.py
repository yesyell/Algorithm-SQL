import heapq

def solution(n, costs):
    graph = [[] for _ in range(n)]
    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    visited = [False] * n
    min_heap = [(0, 0)]  # (비용, 시작노드)
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_cost, next_node))

    return total_cost