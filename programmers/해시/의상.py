# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
# 해시/의상

## clothes에서 [i, 1]값들은 전부 key로 와야함
## 그럼 key가 같은 value들의 count를 value에 넣어야함
## 그럼 dict = {'headgear': 2, 'eyewear':1}로 되며
## 아무것도 안 입는 경우를 제외한 (2+1)*(1+1) - 1로 계산을 해서 경우의 수를 구함

def solution(clothes):
    count = {}
    answer = 1
    for i in clothes:
        kind = i[1]
        if kind in count:
            count[kind] += 1
        else:
            count[kind] = 1
    
    answer = 1
    for j in count.values():
        answer *= (j + 1)
    return answer - 1
