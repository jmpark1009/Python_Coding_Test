# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 스택큐/같은_숫자는_싫어

# 01. for과 if를 이용해서 문제 풀기
## for문 안에 arr의 str를 하나씩 answer list에 넣기
## 만약 answer가 비어있거나, answer의 마지막 값이 num과 다르면 삽입
def solution(arr):
    answer = []
    for num in arr:
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)
    return answer
