from collections import deque

def solution(jobs):
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[0])  # 요청 시간 기준 정렬
    dq = deque(jobs)
    
    cur = 0
    total_wait = 0
    available = []

    while dq or available:
        # 현재 시점에 도착한 작업 수집
        while dq and dq[0][0] <= cur:
            req, dur = dq.popleft()
            available.append((dur, req))  # 작업시간 기준으로 선택
        if available:
            # 소요시간이 가장 짧은 작업 선택
            available.sort()  # dur 기준 정렬
            dur, req = available.pop(0)
            cur += dur
            total_wait += (cur - req)
        else:
            # 가능한 작업 없으면 시간만 흐름
            cur += 1

    return total_wait // n