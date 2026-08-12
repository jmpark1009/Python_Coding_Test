# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 정렬/k번째수

# 01. 반복문 for를 사용하여 해결하기.
## commands의 형태에 주목할 필요가 있음.
## 파이썬은 0부터 시작한다는 점을 조심할 필요가 있음.
## list에서 값을 넣는 함수는 append임.
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

# 02. 리스트 컴프리헨션을 이용하여 해결하기.
## 위와 동일한 로직(각 command의 [i, j, k]로 구간 정렬 후 k-1번째 값 추출)을 한 줄로 축약함.
## for + append 대신 리스트 컴프리헨션으로 표현한 것 뿐, 동작과 시간복잡도는 위와 같음.
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
