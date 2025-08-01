def solution(n):
    result = 0
    cols = set()  # 같은 열에 퀸이 있는지
    diag1, diag2 = set(), set()  # ↘ (row + col), ↙ (row - col)
    
    def backtrack(row):
        nonlocal result
        if row == n:
            result += 1
            return
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue # 충돌
            # 퀸 배치
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            backtrack(row + 1)
            # 퀸 제거
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
            
    backtrack(0)
    return result   