# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# H-Index

# 01. sort과 for문을 이용하여 비교하기
## 입력값을 내림차순으로 sort(높은 인용 수부터 확인하기 위함)
## 논문을 하나씩 검사하며 H-Index 조건 비교
## citations[i]: 현재 논문의 인용 횟수
## i + 1: 지금까지 세어본 논문의 총 개수
## 인용 수가 논문 개수보다 작아지는 순간, 직전 논문 개수(i)가 H-Index가 됨
## 예외 처리: 모든 논문의 인용 수가 전체 논문 수 이상인 경우 (예: [10,8,7,6])

def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)
