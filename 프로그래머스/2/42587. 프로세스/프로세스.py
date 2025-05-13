# from collections import deque

def solution(priorities, location):
    answer = []
    queue = [(i, p) for (i, p) in enumerate(priorities)]
    
    while True and queue:
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        cur = queue.pop(0)
        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        # 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
        else: 
            answer.append(cur[0])
    return answer.index(location)+1