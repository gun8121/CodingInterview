def solution(my_strings, parts):
    answer = ''
    for i, val in enumerate(parts):
        s,e = val
        answer += my_strings[i][s:e+1]
    return answer