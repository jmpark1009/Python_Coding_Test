# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 스택큐/올바른_괄호

## 1) stack이라는 빈 list준비
## 2-1) 만약 여는 괄호라면 stack에 append
## 2-2) 만약 닫는 괄호라면 stack이 비어있다면 즉시 False 반환
## 2-3) stack에 여는 괄호가 있다면 pop()으로 짝 제거
## 3) s값이 전부 끝났을 때 stack이 비어있는지 확인 -> 1개라도 있으면 false 
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
