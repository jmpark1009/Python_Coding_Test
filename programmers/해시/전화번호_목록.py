# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 해시/전화번호_목록

## 각 list의 str을 sort를 통해 비슷한 것끼리 묶기
## for문을 사용해서 앞부분이 다른 자리의 접두어인지 확인
## 인접한 두 번호(i번째, i+1번째)만 순차적으로 비교
## 앞 번호의 길이만큼 뒷 번호의 시작 부분을 슬라이싱하여 접두어인지 비교
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        front = phone_book[i]
        next = phone_book[i + 1]
        
        if next[:len(front)] == front:
            return False  
    return True
