# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 스택큐/프로세스

## 1) 대기중인 프로세스를 확인
## 2) 우선순위가 더 높은 프로세스가 있다면 다시 넣기
## 3) 없다면 pop하고 종료

### 자리를 알 수 있도록 튜플리스트를 만들기
### 리스트의 앞의 값을 pop으로 뽑아서, 리스트의 최대값과 비교하기
### 비교할 때 리스트 안에 더 높은 프로세스가 있다면 append, 없으면 반복하기
from collections import deque

def solution(priorities, location):
    queue = []
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
        
    queue = deque(queue)
    count = 0
    while queue:
        cur = queue.popleft()
        
        if queue and max(p[1] for p in queue) > cur[1]:
            queue.append(cur)
        else:
            count += 1
            if cur[0] == location:
                return count
