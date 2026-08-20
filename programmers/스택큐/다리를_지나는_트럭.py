# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 스택큐/다리를_지나는_트럭

## 10kg까지 견디는 다리
## bridge_length 고려하기
## bridge_queue를 만들어보자
## 1) 다리길이 만큼의 0으로 채운 bridge_q 를 deque로 만든다.
## 2) 매 1초마다 time을 1씩 더하고, 트럭을 앞으로 한칸씩 옮겨주며, 다리의 맨 앞 칸을 비우고 cur_weight에서 해당 무게만큼 빼준다.
## 3) 새 트럭이 진입 여부를 확인한다. 만약 cur_weight + 다음 대기 트럭 무게의 합이 weight보다 작거나 같으면 진입시키고, 아니라면 트럭 대신 0을 넣는다.
## 4) 대기트럭도 없고, 다리위에도 트럭이 없다면 time을 return 한다. 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_q = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0
    cur_weight = 0
    
    while bridge_q:
        time += 1
        cur_weight -= bridge_q.popleft()
        
        if trucks:
            if cur_weight + trucks[0] <= weight:
                wait_truck = trucks.popleft()
                bridge_q.append(wait_truck)
                cur_weight += wait_truck
            else:
                bridge_q.append(0)
                
    return time
