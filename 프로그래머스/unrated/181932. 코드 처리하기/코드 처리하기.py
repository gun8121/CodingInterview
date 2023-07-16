def solution(code):
    answer = ''
    mode = 0
    for i, word in enumerate(code):
        if mode == 0:
            if i%2 ==0 and word != '1':
                answer = answer + word
            elif word == '1':
                mode = 1
        else:
            if i%2 == 1 and word != '1':
                answer = answer + word
            elif word == '1':
                mode = 0
    if len(answer) == 0:
        return 'EMPTY'
    return answer

# mode 가 0일때
# code 를 순서대로 읽으면서 idx 가 