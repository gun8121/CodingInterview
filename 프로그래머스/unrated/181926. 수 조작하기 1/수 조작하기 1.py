def solution(n, control):
    answer = 0
    for i in control:
        if i == 'w':
            answer = answer + 1
        elif i == 's':
            answer = answer -1
        elif i == 'd':
            answer = answer + 10
        else:
            answer = answer - 10
    answer = answer + n   
    return answer