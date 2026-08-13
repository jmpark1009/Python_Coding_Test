# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색/모의고사

## 각 list를 len(answer)만큼 반복하자
## 반복하여 list를 추가할 때마다 answer과 답을 비교하여 count를 더하자
def solution(answer):
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = count2 = count3 = 0

    for i in range(len(answer)):
        if list1[i % len(list1)] == answer[i]:
            count1 += 1
        if list2[i % len(list2)] == answer[i]:
            count2 += 1
        if list3[i % len(list3)] == answer[i]:
            count3 += 1

    scores = {1: count1, 2: count2, 3: count3}
    best = max(scores.values())
    result = [student for student, score in scores.items() if score == best]

    return sorted(result)
