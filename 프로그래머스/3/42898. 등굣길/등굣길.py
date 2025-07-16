def solution(m, n, puddles):
    # dp[y][x]: (x, y) 지점까지 도달할 수 있는 경로 수
    dp = [[0]*(m+1) for _ in range(n+1)]
    puddles = set((x, y) for x, y in puddles)
    dp[1][1] = 1 # 시작점
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if (x, y) in puddles:
                dp[y][x] = 0 # 물웅덩이 → 지나갈 수 없음
            elif not (x==1 and y==1): # 시작점 제외
                # 왼, 위에서 올 수 있음
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return dp[n][m] % 1000000007