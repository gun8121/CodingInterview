def solution(numbers, n):
    answer = 0
    for idx, val in enumerate(numbers):
        if answer > n:
            return answer
        else:
            answer += val
    return answer