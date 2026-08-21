# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 스택큐/주식가격

## 결과 리스트를 0으로 초기화 (길이는 prices와 동일)
## 기준이 되는 현재 시점 순회 (0번부터 n-1번까지)
## 현재 시점 바로 다음(i + 1)부터 끝까지 미래 가격 확인
## 1초 경과 반영 (가격이 떨어지더라도 1초는 유지된 것으로 봄)
## 가격이 떨어졌다면 추가 시간 계산 없이 즉시 중단 (break)             

def solution(prices):
    n = len(prices)                 # 예시는 n=5
    answer = [0] * n                # 예시는 [0,0,0,0,0]
    
    for i in range(n):              # 0부터 4까지 5번 반복
        for j in range(i + 1, n):   # i번 뒤부터 반복 진행
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer
            
            
