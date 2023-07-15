def solution(a, b):
    s_a = str(a)
    s_b = str(b)
    answer = 0
    if s_a + s_b > s_b + s_a:
        answer = int(s_a + s_b)
    elif s_b + s_a > s_a + s_b:
        answer = int(s_b + s_a)
    else:
        answer = int(s_a + s_b)
    return answer