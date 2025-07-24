import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 기준 정렬
    heap = []
    
    cur, total_time, i = 0, 0, 0
    n = len(jobs)

    while i < n or heap:
        # 현재 시간까지 도착한 작업들 힙에 추가 (작업 시간 기준)
        while i < n and jobs[i][0] <= cur:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))  # (작업 시간, 요청 시간)
            i += 1
        
        if heap:
            work_time, req_time = heapq.heappop(heap)
            cur += work_time
            total_time += cur - req_time  # 대기 시간 누적
        else:
            # 대기할 작업이 없다면 시간 흐름
            cur = jobs[i][0]

    return total_time // n