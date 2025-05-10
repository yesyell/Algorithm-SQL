def solution(n, lost, reserve):
    # 집합으로 변환 (중복 제거 및 빠른 연산)
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 여벌을 가져왔지만 도난당한 학생 제거
    overlap = lost_set & reserve_set
    lost_set -= overlap
    reserve_set -= overlap
    
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)