def solution(num_list):
    answer = 0
    mult = 1

    for x in num_list:
        mult = mult * x
        
    if mult < sum(num_list)**2:
        answer = 1
    else:
        answer = 0
    return answer