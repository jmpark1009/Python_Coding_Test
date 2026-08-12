# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 해시/완주하지 못한 선수

# 01. 파이썬 라이브러리 함수를 이용해서 해결하기.
## participant, completion은 list형태.
## 100,000명까지 될 수 있기에 반복문을 사용하면 너무 오래걸림.
## 동명이인이 있을 수 있기에 조심해야함.
## collections.Counter: {요소: 개수} 형태의 딕셔너리를 만들기.
from collections import Counter
def solution_counter(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# 02. 라이브러리를 사용하지 않고 for문으로 해결하기.
## 동명이인이라는 함정이 있기에, dict형태로 {요소: 개수}를 만드는게 좋아보임.
## Key를 이름, Value를 개수로 만들기.
def solution_loop(participant, completion):
    dict = {}
    for name in participant:
        if name in dict:
            dict[name] += 1
        else:
            dict[name] = 1
    for name in completion:
        dict[name] -= 1
    for name in dict:
        if dict[name] > 0:
            return name
