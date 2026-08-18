# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 해시/폰켓몬

## N마리 중 N/2마리를 가져감
## n/2를 저장 + 중복이 되지 않는 nums의 길이를 저장
## 만약 중복이 되지 않는 길이가 길면 => n/2
## 만약 중복이 되지 않는 길이가 짧으면 => 중복없는 길이

def solution(nums):
    n_half = len(nums) // 2
    unique = len(set(nums))
    answer = min(n_half, unique)
    return answer
