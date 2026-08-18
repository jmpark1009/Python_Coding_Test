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

# for과 if를 사용한 코드
def solution(nums):
    n_half = len(nums) // 2
    unique_list = []
    for x in nums:
        if x not in unique_list:
            unique_list.append(x)

    unique_count = len(unique_list)
    if unique_count > n_half:
        return n_half
    else:
        return unique_count
