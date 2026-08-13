# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 가장 큰 수

# 01. str(list와 map)과 lambda를 이용하여 해결하기.
## 각 숫자들이 더해지거나 곱해지지 않도록 str형태로 변경
## str형태는 앞자리부터 비교하는 ASCII 비교가 진행됨
## 따라서 '6' > '10' 임 (6이 1보다 크기에)
## 추가로 x*3을 통해 '333' > '303030'을 구분할 수 있음
## 이를 통해 '3' > '30'을 추론할 수 있음

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer

# 02. map을 이용하지 않고 str로 바꾸기
## map을 사용하지 않는다면 numbers의 모든 원소들을 for를 이용해 str로 변경한다

def solution(numbers):
    str_num = []
    for x in numbers:
        str_num.append(str(x))
    str_num.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(str_num)
    if answer[0] == '0':
        return '0'
    return answer
