def solution(a, b):
    answer = 0
    ab, ba = str(a), str(b)
    if int(ab+ba) >= 2*a*b:
        answer = int(ab+ba)
    else:
        answer = 2*a*b
    return answer